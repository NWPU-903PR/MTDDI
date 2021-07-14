from __future__ import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
import scipy.sparse as sp
import random
from ..utility import preprocessing
flags = tf.app.flags
FLAGS = flags.FLAGS
np.random.seed(123)


class EdgeMinibatchIterator(object):
    """ This minibatch iterator iterates over batches of sampled edges or
    random pairs of co-occuring edges.
    assoc -- numpy array with target edges
    placeholders -- tensorflow placeholders object
    batch_size -- size of the minibatches
    """
    def __init__(self, adj_mats, drug_DBP_similarity,feat, edge_types, batch_size, test_size,val_size):
        self.adj_mats = adj_mats
        self.drug_DBP_similarity=drug_DBP_similarity
        self.feat = feat
        self.edge_types = edge_types
        self.batch_size = batch_size
        self.test_size = test_size  ##self.val_test_size
        self.val_size = val_size
        self.mutiple_neg_sample = FLAGS.mutiple_neg_sample
        self.num_edge_types = sum(self.edge_types.values())

        self.iter = 0
        self.freebatch_edge_types= list(range(self.num_edge_types))
        self.batch_num = [0]*self.num_edge_types
        self.current_edge_type_idx = 0
        self.edge_type2idx = {}
        self.idx2edge_type = {}
        r = 0
        for i, j in self.edge_types:
            for k in range(self.edge_types[i,j]):
                self.edge_type2idx[i, j, k] = r
                self.idx2edge_type[r] = i, j, k
                r += 1

        self.train_edges = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        self.val_edges = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        self.test_edges = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        self.test_edges_false = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        self.val_edges_false = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        self.train_edges_neg = {edge_type: [None] * n for edge_type, n in self.edge_types.items()}

        # Function to build test and val sets with val_test_size positive links
        self.adj_train = {edge_type: [None]*n for edge_type, n in self.edge_types.items()}
        for i, j in self.edge_types:
            for k in range(self.edge_types[i,j]):
                print("Minibatch edge type:", "(%d, %d, %d)" % (i, j, k))
                self.mask_test_edges((i, j), k)

                print("Train edges=", "%04d" % len(self.train_edges[i,j][k]))
                print("Val edges=", "%04d" % len(self.val_edges[i,j][k]))
                print("Test edges=", "%04d" % len(self.test_edges[i,j][k]))

    def preprocess_graph(self, adj):
        adj = sp.coo_matrix(adj)
        if adj.shape[0] == adj.shape[1]:
            adj_ = adj + sp.eye(adj.shape[0])
            rowsum = np.array(adj_.sum(1))
            degree_mat_inv_sqrt = sp.diags(np.power(rowsum, -0.5).flatten())
            adj_normalized = adj_.dot(degree_mat_inv_sqrt).transpose().dot(degree_mat_inv_sqrt).tocoo()
        else:
            rowsum = np.array(adj.sum(1))
            colsum = np.array(adj.sum(0))
            rowdegree_mat_inv = sp.diags(np.nan_to_num(np.power(rowsum, -0.5)).flatten())
            coldegree_mat_inv = sp.diags(np.nan_to_num(np.power(colsum, -0.5)).flatten())
            adj_normalized = rowdegree_mat_inv.dot(adj).dot(coldegree_mat_inv).tocoo()
        return preprocessing.sparse_to_tuple(adj_normalized)

    def _ismember(self, a, b):
        a = np.array(a)
        b = np.array(b)
        rows_close = np.all(a - b == 0, axis=1)
        return np.any(rows_close)

    def mask_test_edges(self, edge_type, type_idx):
        self.adj_mats[edge_type][type_idx] = sp.csr_matrix(self.adj_mats[edge_type][type_idx])
        edges_all, _, _ = preprocessing.sparse_to_tuple(self.adj_mats[edge_type][type_idx])
        num_test = max(50, int (np.floor(edges_all.shape[0] * self.test_size)))
        num_val = max(50, int(np.floor(edges_all.shape[0] * self.val_size)))

        all_edge_idx = list(range(edges_all.shape[0]))
        np.random.shuffle(all_edge_idx)

        val_edge_idx = all_edge_idx[:num_val]
        val_edges = edges_all[val_edge_idx]

        test_edge_idx = all_edge_idx[num_val:(num_val + num_test)]
        test_edges = edges_all[test_edge_idx]

        train_edges = np.delete(edges_all, np.hstack([test_edge_idx, val_edge_idx]), axis=0)

        non_link_number = 0
        non_link_position = []
        for i in range(0,self.adj_mats[edge_type][type_idx].shape[0]):
            for j in range(i+1,self.adj_mats[edge_type][type_idx].shape[1]):
                if self.adj_mats[edge_type][type_idx][i,j] == 0:
                    non_link_number = non_link_number + 1
                    non_link_position.append([i,j])
        non_link_position = np.array(non_link_position)
        non_link_index = np.arange(0,non_link_number)
        random.shuffle(non_link_index)

        test_no_link_index = non_link_index[0:num_test*self.mutiple_neg_sample]
        test_no_link_index.sort()
        test_edges_false = non_link_position[test_no_link_index]

        val_no_link_index = non_link_index[num_test*self.mutiple_neg_sample:(num_test*self.mutiple_neg_sample)+ num_val*self.mutiple_neg_sample]
        val_no_link_index.sort()
        val_edges_false = non_link_position[val_no_link_index]

        train_no_link_index = non_link_index[(num_test*self.mutiple_neg_sample)+ num_val*self.mutiple_neg_sample:]
        train_edges_neg = non_link_position[train_no_link_index]        #
        #
        # test_edges_false = []
        # while len(test_edges_false) < len(test_edges):
        #     if len(test_edges_false) % 1000 == 0:
        #         print("Constructing test edges=", "%04d/%04d" % (len(test_edges_false), len(test_edges)))
        #     idx_i = np.random.randint(0, self.adj_mats[edge_type][type_idx].shape[0])
        #     idx_j = np.random.randint(0, self.adj_mats[edge_type][type_idx].shape[1])
        #     if self._ismember([idx_i, idx_j], edges_all):
        #         continue
        #     if test_edges_false:
        #         if self._ismember([idx_i, idx_j], test_edges_false):
        #             continue
        #     test_edges_false.append([idx_i, idx_j])
        #
        # val_edges_false = []
        # while len(val_edges_false) < len(val_edges):
        #     if len(val_edges_false) % 1000 == 0:
        #         print("Constructing val edges=", "%04d/%04d" % (len(val_edges_false), len(val_edges)))
        #     idx_i = np.random.randint(0, self.adj_mats[edge_type][type_idx].shape[0])
        #     idx_j = np.random.randint(0, self.adj_mats[edge_type][type_idx].shape[1])
        #     if self._ismember([idx_i, idx_j], edges_all):
        #         continue
        #     if val_edges_false:
        #         if self._ismember([idx_i, idx_j], val_edges_false):
        #             continue   #'''if self._ismember([idx_i, idx_j], test_edges_false):   ##验证集的负样本和测试集的负样本设为不同
        #
        #     val_edges_false.append([idx_i, idx_j])
                
            
        # Re-build adj matrices
        data = np.ones(train_edges.shape[0])
        adj_train = sp.csr_matrix(
            (data, (train_edges[:, 0], train_edges[:, 1])),
            shape=self.adj_mats[edge_type][type_idx].shape)
        self.adj_train[edge_type][type_idx] = self.preprocess_graph(adj_train)

        self.train_edges[edge_type][type_idx] = train_edges
        self.val_edges[edge_type][type_idx] = val_edges
        self.val_edges_false[edge_type][type_idx] = val_edges_false
        self.test_edges[edge_type][type_idx] = test_edges
        self.test_edges_false[edge_type][type_idx] = test_edges_false
        self.train_edges_neg[edge_type][type_idx] = train_edges_neg

    def end(self):
        finished = len(self.freebatch_edge_types) == 0
        return finished

    def update_feed_dict(self, feed_dict, dropout, placeholders):
        # construct feed dictionary
        feed_dict.update({
            placeholders['adj_mats_%d,%d,%d' % (i,j,k)]: self.adj_train[i,j][k]
            for i, j in self.edge_types for k in range(self.edge_types[i,j])})
        feed_dict.update({placeholders['feat_%d' % i]: self.feat[i] for i, _ in self.edge_types})
        feed_dict.update({placeholders['dropout']: dropout})

        return feed_dict

    def batch_feed_dict(self, batch_edges, batch_neg_edges, batch_node, adj_min_batch,sim_min_batch,batch_edge_type, placeholders):
        feed_dict = dict()
        feed_dict.update({placeholders['batch']: batch_edges})
        feed_dict.update({placeholders['batch_neg']: batch_neg_edges})
        feed_dict.update({placeholders['batch_edge_type_idx']: batch_edge_type})
        feed_dict.update({placeholders['batch_node']: batch_node})
        feed_dict.update({placeholders['adj_min_batch']: adj_min_batch})
        feed_dict.update({placeholders['sim_min_batch']: sim_min_batch})
        feed_dict.update({placeholders['batch_row_edge_type']: self.idx2edge_type[batch_edge_type][0]})
        feed_dict.update({placeholders['batch_col_edge_type']: self.idx2edge_type[batch_edge_type][1]})

        return feed_dict

    def next_minibatch_feed_dict(self, placeholders):
        """Select a random edge type and a batch of edges of the same type"""
        while True:
           if len(self.freebatch_edge_types) > 0:
               self.current_edge_type_idx = np.random.choice(self.freebatch_edge_types)
           else:
               self.current_edge_type_idx = np.random.choice(range(0,1))   ####(0,11)
               self.batch_num[self.current_edge_type_idx] = 0


           i, j, k = self.idx2edge_type[self.current_edge_type_idx]
           if self.batch_num[self.current_edge_type_idx] * self.batch_size \
                  <= len(self.train_edges[i,j][k]) - self.batch_size + 1:
               break
           elif self.current_edge_type_idx in self.freebatch_edge_types:
                # print("current_edge_type_idx" + str(self.current_edge_type_idx))
                self.freebatch_edge_types.remove(self.current_edge_type_idx)
                # print("freebatch_edge_types" + str(self.freebatch_edge_types))
                self.current_edge_type_idx = 0


        self.iter += 1
        start = self.batch_num[self.current_edge_type_idx] * self.batch_size
        self.batch_num[self.current_edge_type_idx] += 1
        batch_edges = self.train_edges[i,j][k][start: start + self.batch_size]
        batch_neg_edges = self.train_edges_neg[i, j][k][self.mutiple_neg_sample*start: self.mutiple_neg_sample*(start + self.batch_size)]

        # node1 = [batch_edges[t][0] for t in range(len(batch_edges))]
        # node2 = [batch_edges[t][1] for t in range(len(batch_edges))]
        node1_neg = [batch_neg_edges[t][0] for t in range(len(batch_neg_edges))]
        node2_neg = [batch_neg_edges[t][1] for t in range(len(batch_neg_edges))]
        # batch_node = list(set(node1 + node2 +node1_neg +node2_neg))
        batch_node = list(set(node1_neg + node2_neg))
        batch_node.sort()
        adj_min_batch = self.adj_mats[(i,j)][k][batch_node].toarray()[:][:,batch_node]
        sim_min_batch = self.drug_DBP_similarity[batch_node][:][:,batch_node]

        return self.batch_feed_dict(batch_edges, batch_neg_edges,batch_node,adj_min_batch,sim_min_batch,self.current_edge_type_idx, placeholders)




    def num_training_batches(self, edge_type, type_idx):
        return len(self.train_edges[edge_type][type_idx]) // self.batch_size + 1

    def val_feed_dict(self, edge_type, type_idx, placeholders, size=None):
        edge_list = self.val_edges[edge_type][type_idx]
        if size is None:
            return self.batch_feed_dict(edge_list, edge_type, placeholders)
        else:
            ind = np.random.permutation(len(edge_list))
            val_edges = [edge_list[i] for i in ind[:min(size, len(ind))]]
            return self.batch_feed_dict(val_edges, edge_type, placeholders)

    def shuffle(self):
        """ Re-shuffle the training set.
            Also reset the batch number.
        """
        for edge_type in self.edge_types:
            for k in range(self.edge_types[edge_type]):
                self.train_edges[edge_type][k] = np.random.permutation(self.train_edges[edge_type][k])
                self.batch_num[self.edge_type2idx[edge_type[0], edge_type[1], k]] = 0
        self.current_edge_type_idx = 0
        self.freebatch_edge_types = list(range(self.num_edge_types))

        self.iter = 0