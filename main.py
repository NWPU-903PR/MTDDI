from __future__ import division
from __future__ import print_function
from operator import itemgetter
from itertools import combinations
import time
import os
import pandas as pd
import random
import copy
import scipy.io as sio
import tensorflow as tf
import numpy as np
import networkx as nx
import scipy.sparse as sp
from sklearn import metrics
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_auc_score
from MTDDI.optimizer import Optimizer
from MTDDI.model import Model
from MTDDI.minibatch import EdgeMinibatchIterator
from MTDDI.utility import rank_metrics, preprocessing

# Train on CPU (hide GPU) due to memory constraints
# os.environ['CUDA_VISIBLE_DEVICES'] = "0"

# Train on GPU
# os.environ["CUDA_DEVICE_ORDER"] = 'PCI_BUS_ID'
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True

np.random.seed(0)

###########################################################


def get_accuracy_scores(edges_pos, edges_neg, edge_type):
    feed_dict.update({placeholders['dropout']: 0})
    feed_dict.update({placeholders['batch_edge_type_idx']: minibatch.edge_type2idx[edge_type]})
    feed_dict.update({placeholders['batch_row_edge_type']: edge_type[0]})
    feed_dict.update({placeholders['batch_col_edge_type']: edge_type[1]})
    rec = sess.run(opt.predictions, feed_dict=feed_dict)

    # def sigmoid(x):
    #     return 1. / (1 + np.exp(-x))

    def sigmoid(x):

        if x >= 0:
            return 1.0 / (1 + np.exp(-x))
        else:
            return np.exp(x) / (1 + np.exp(x))

    # Predict on test set of edges
    preds = []
    actual = []
    predicted = []
    edge_ind = 0
    for u, v in edges_pos[edge_type[:2]][edge_type[2]]:
        score = sigmoid(rec[u, v])
        preds.append(score)
        assert adj_mats_orig[edge_type[:2]][edge_type[2]][u,v] == 1, 'Problem 1'

        actual.append(edge_ind)
        predicted.append((score, edge_ind))
        edge_ind += 1

    preds_neg = []
    for u, v in edges_neg[edge_type[:2]][edge_type[2]]:
        score = sigmoid(rec[u, v])
        preds_neg.append(score)
        assert adj_mats_orig[edge_type[:2]][edge_type[2]][u,v] == 0, 'Problem 0'

        predicted.append((score, edge_ind))
        edge_ind += 1

    preds_all = np.hstack([preds, preds_neg])
    preds_all = np.nan_to_num(preds_all)
    labels_all = np.hstack([np.ones(len(preds)), np.zeros(len(preds_neg))])
    predicted = list(zip(*sorted(predicted, reverse=True, key=itemgetter(0))))[1]

    roc_sc = metrics.roc_auc_score(labels_all, preds_all)
    # aupr_sc = metrics.average_precision_score(labels_all, preds_all)
    precision,recall,pr_thresholds = precision_recall_curve(labels_all,preds_all)
    auprc_score = auc(recall,precision)

    all_F_measure = np.zeros(len(pr_thresholds))
    for k in range(0, len(pr_thresholds)):
        if (precision[k] + precision[k]) > 0:
            all_F_measure[k] = 2 * precision[k] * recall[k] / (precision[k] + recall[k])
        else:
            all_F_measure[k] = 0
    max_index = all_F_measure.argmax()
    threshold = pr_thresholds[max_index]

    fpr, tpr, auc_thresholds = roc_curve(labels_all, preds_all)
    auc_score = auc(fpr, tpr)
    predicted_score = np.zeros(shape=(len(labels_all), 1))
    predicted_score[preds_all > threshold] = 1
    confusion_matri = confusion_matrix(y_true=labels_all, y_pred=predicted_score)
    # print("confusion_matrix:", confusion_matri)
    f = f1_score(labels_all, predicted_score)
    accuracy = accuracy_score(labels_all,predicted_score)
    precision = precision_score(labels_all,predicted_score)
    recall = recall_score(labels_all,predicted_score)

    apk_sc = rank_metrics.apk(actual, predicted, k=50)

    return roc_sc, auprc_score,accuracy,precision,recall,f ,apk_sc


def construct_placeholders(edge_types):
    placeholders = {
        'batch': tf.placeholder(tf.int32, name='batch'),
        'batch_neg': tf.placeholder(tf.int32, name='batch_neg'),
        'batch_node':tf.placeholder(tf.int32,name = 'batch_node'),
        'adj_min_batch': tf.placeholder(tf.float32,name='adj_min_batch'),
        'sim_min_batch': tf.placeholder(tf.float32,name='sim_min_batch'),
        'batch_edge_type_idx': tf.placeholder(tf.int32, shape=(), name='batch_edge_type_idx'),
        'batch_row_edge_type': tf.placeholder(tf.int32, shape=(), name='batch_row_edge_type'),
        'batch_col_edge_type': tf.placeholder(tf.int32, shape=(), name='batch_col_edge_type'),
        'degrees': tf.placeholder(tf.int32),
        'dropout': tf.placeholder_with_default(0., shape=()),
    }
    placeholders.update({
        'adj_mats_%d,%d,%d' % (i, j, k): tf.sparse_placeholder(tf.float32)
        for i, j in edge_types for k in range(edge_types[i,j])})
    placeholders.update({
        'feat_%d' % i: tf.sparse_placeholder(tf.float32)
        for i, _ in edge_types})
    return placeholders

###########################################################

test_size = 0.20
val_size = 0.05

num_drugs =  2926 
n_drugdrug_rel_types =11

filename = "./data/adj_absor.csv"
adj_absor = pd.read_csv(open(filename) )    

filename = "./data/adj_activity_antag.csv"
adj_activity_antag = pd.read_csv(open(filename) )  

filename = "./data/adj_activity_syn.csv"
adj_activity_syn = pd.read_csv(open(filename) )  

filename = "./data/adj_activity_tox.csv"
adj_activity_tox = pd.read_csv(open(filename) )  

filename = "./data/adj_adv.csv"
adj_adv = pd.read_csv(open(filename) )    

filename = "./data/adj_excre.csv"
adj_excre = pd.read_csv(open(filename) )  

filename = "./data/adj_meta.csv"
adj_meta = pd.read_csv(open(filename) )  

filename = "./data/adj_pd_antag.csv"
adj_pd_antag = pd.read_csv(open(filename) )   

filename = "./data/adj_pkd.csv"
adj_pkd = pd.read_csv(open(filename) )   

filename = "./data/adj_pd_syn.csv"
adj_pd_syn = pd.read_csv(open(filename) )   

filename = "./data/adj_serum.csv"
adj_serum = pd.read_csv(open(filename) )    


drug_drug_adj_list = []
drug_drug_adj_list.append(sp.csr_matrix(adj_absor))
drug_drug_adj_list.append(sp.csr_matrix(adj_activity_antag))
drug_drug_adj_list.append(sp.csr_matrix(adj_activity_syn))
drug_drug_adj_list.append(sp.csr_matrix(adj_activity_tox))
drug_drug_adj_list.append(sp.csr_matrix(adj_adv))
drug_drug_adj_list.append(sp.csr_matrix(adj_excre))
drug_drug_adj_list.append(sp.csr_matrix(adj_meta))
drug_drug_adj_list.append(sp.csr_matrix(adj_pd_antag))
drug_drug_adj_list.append(sp.csr_matrix(adj_pd_syn))
drug_drug_adj_list.append(sp.csr_matrix(adj_pkd))
drug_drug_adj_list.append(sp.csr_matrix(adj_serum ))


drug_degrees_list = [np.array(drug_adj.sum(axis=0)).squeeze() for drug_adj in drug_drug_adj_list]
                     

# data representation
adj_mats_orig = { 
    (0, 0): drug_drug_adj_list,
}
degrees = {
    0: drug_degrees_list    ###?????ADD??
}


n_drugs = adj_absor.shape[0]
drug_feat = sp.identity(n_drugs)
drug_nonzero_feat, drug_num_feat = drug_feat.shape
drug_feat = preprocessing.sparse_to_tuple(drug_feat.tocoo())

###xsimilarity matrix
filename = "drug_similarity.csv"
drug_similarity= pd.read_csv(open(filename) )    ###filename路径中还有中文名字的时候需要加open（）
drug_similarity = drug_similarity.iloc[:,:].values

num_feat = {
       0: drug_num_feat,
}
nonzero_feat = {
    0: drug_nonzero_feat,
}
feat = {
    0: drug_feat,
}

edge_type2dim = {k: [adj.shape for adj in adjs] for k, adjs in adj_mats_orig.items()}
edge_type2decoder = {
    (0, 0):'dedicom',     
}

edge_types = {k: len(v) for k, v in adj_mats_orig.items()}
num_edge_types = sum(edge_types.values())
print("Edge types:", "%d" % num_edge_types)

###########################################################
#
# Settings and placeholders
#
###########################################################

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_integer('neg_sample_size', 6, 'Negative sample size.')
flags.DEFINE_integer('mutiple_neg_sample', 1, 'mutiple of neg_sample')
flags.DEFINE_float('learning_rate', 0.001, 'Initial learning rate.')
flags.DEFINE_integer('epochs', 20, 'Number of epochs to train.')
flags.DEFINE_integer('hidden1',1024, 'Number of units in hidden layer 1.')
flags.DEFINE_integer('hidden2', 128, 'Number of units in hidden layer 2.')
flags.DEFINE_integer('hidden3', 128, 'Number of units in hidden layer 3.')
flags.DEFINE_integer('hidden4', 128, 'Number of units in hidden layer 4.')
flags.DEFINE_float('weight_decay', 0, 'Weight for L2 loss on embedding matrix.')
flags.DEFINE_float('dropout', 0.0, 'Dropout rate (1 - keep probability).')
flags.DEFINE_float('max_margin', 0.1, 'Max margin parameter in hinge loss')
flags.DEFINE_integer('batch_size', 400, 'minibatch size.')
flags.DEFINE_boolean('bias', True, 'Bias term.')
flags.DEFINE_float('gamma',1,'weight of cross_entroy loss')
flags.DEFINE_float('alpha',0.02,'weight of similarity loss'   )
# Important -- Do not evaluate/print validation performance every iteration as it can take
# substantial amount of time
PRINT_PROGRESS_EVERY = 150

print("Defining placeholders")
placeholders = construct_placeholders(edge_types)

###########################################################
#
# Create minibatch iterator, model and optimizer
#
###########################################################

print("Create minibatch iterator")
minibatch = EdgeMinibatchIterator(
    adj_mats=adj_mats_orig,
    drug_similarity=drug_similarity,
    feat=feat,
    edge_types=edge_types,
    batch_size=FLAGS.batch_size,
    test_size=test_size,
    val_size=val_size
)

print("Create model")
model = Model(
    placeholders=placeholders,
    num_feat=num_feat,
    nonzero_feat=nonzero_feat,
    edge_types=edge_types,
    decoders=edge_type2decoder,
)

print("Create optimizer")
with tf.name_scope('optimizer'):
    opt = Optimizer(
        embeddings=model.embeddings,
        latent_inters=model.latent_inters,
        latent_varies=model.latent_varies,
        degrees=degrees,
        edge_types=edge_types,
        edge_type2dim=edge_type2dim,
        placeholders=placeholders,
        batch_size=FLAGS.batch_size,
        margin=FLAGS.max_margin
    )

print("Initialize session")
sess = tf.Session()
sess.run(tf.global_variables_initializer())
feed_dict = {}

###########################################################
#
# Train model
#
###########################################################

print("Train model")
for epoch in range(FLAGS.epochs):

    minibatch.shuffle()
    itr = 0
    while not minibatch.end():
        # Construct feed dictionary
        feed_dict = minibatch.next_minibatch_feed_dict(placeholders=placeholders)
        feed_dict = minibatch.update_feed_dict(
            feed_dict=feed_dict,
            dropout=FLAGS.dropout,
            placeholders=placeholders)

        t = time.time()

        # Training step: run single weight update
        outs = sess.run([opt.opt_op, opt.cost, opt.batch_edge_type_idx], feed_dict=feed_dict)
        train_cost = outs[1]
        batch_edge_type = outs[2]

        if itr % PRINT_PROGRESS_EVERY == 0:
            val_auc, val_auprc,val_accuracy,val_precision,val_recall,val_f,val_apk = get_accuracy_scores(
                minibatch.val_edges, minibatch.val_edges_false,
                minibatch.idx2edge_type[minibatch.current_edge_type_idx])

            print("Epoch:", "%04d" % (epoch + 1), "Iter:", "%04d" % (itr + 1), "Edge:", "%04d" % batch_edge_type,
                  "train_loss=", "{:.5f}".format(train_cost),
                  "val_roc=", "{:.5f}".format(val_auc), "val_auprc=", "{:.5f}".format(val_auprc),
                  "accuracy=", "{:.5f}".format(val_accuracy), "precision=", "{:.5f}".format(val_precision),
                  "recall=", "{:.5f}".format(val_recall), "f1=", "{:.5f}".format(val_f),
                  "val_apk=", "{:.5f}".format(val_apk), "time=", "{:.5f}".format(time.time() - t))

        itr += 1

print("Optimization finished!")

for et in range(num_edge_types):
     roc_score, auprc_score,accuracy,precision,recall,f, apk_score = get_accuracy_scores(
         minibatch.test_edges, minibatch.test_edges_false, minibatch.idx2edge_type[et])
     print("Edge type=", "[%02d, %02d, %02d]" % minibatch.idx2edge_type[et])
     print("Edge type:", "%04d" % et, "Test AUROC score", "{:.5f}".format(roc_score))
     print("Edge type:", "%04d" % et, "Test AUPRC score", "{:.5f}".format(auprc_score))
     print("Edge type:", "%04d" % et, "Test accuracy score", "{:.5f}".format(accuracy))
     print("Edge type:", "%04d" % et, "Test precision score", "{:.5f}".format(precision))
     print("Edge type:", "%04d" % et, "Test recall score", "{:.5f}".format(recall))
     print("Edge type:", "%04d" % et, "Test f1 score", "{:.5f}".format(f))
     print("Edge type:", "%04d" % et, "Test AP@k score", "{:.5f}".format(apk_score))
     print()

