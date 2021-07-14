MTDDI: a graph convolutional network framework for predicting Multi-Type Drug-Drug Interactions
YueHua Feng; ShaoWu Zhang; Qing-Qing Zhang; Chu-Han Zhang; Jian-Yu Shi




The link to the article is:     https://www.researchsquare.com/article/rs-397281/v1




This repository contains code and data to run the MTDDI algorithm. MTDDI is a a novel end-to-end deep learning-based predictive method 
for predict DDIs as well as its types. The encoder derived from deep relational graph convolutional networks to capture the structural
relationship between multi-type DDI entries, and the the tensor-like decoder to uniformly model both single-fold interactions and multi-fold 
interactions to reflect the relation between DDI types. See our paper for details on the algorithm.


Requirements

Decagon is tested to work under Python 3.

Recent versions of Tensorflow, sklearn, networkx, numpy, and scipy are required. All the required packages can be installed using the following command:

$ pip install -r requirements.txt



License

Decagon is licensed under the MIT License.
