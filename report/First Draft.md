Table of Contents

1. Acknowledgement
2. Introduction
3. Literature Review 
4. Methodology
5. Conclusion
6. References
7. Appendix

**Abstract**

The purpose of this paper is to present an empirical comparison of various classification techniques on text such as Chatclay's  Rasa (SVC),Chatclay's Word2Vec similarity,word movers distance,support vector classifiers n-gram,Logistic Regression,LSTM's This techniques are evaluated on a benchmark of various text classification problem instances that include personally curated datasets as well as datasets obtained from Kaggle,Twitter etc . The results are analyzed from multiple goal perspectives- accuracy, F-measure, precision, and recall, since each is appropriate in different situations.

**Literature Review :**

The use of this data for research on text categorization requires a detailed understanding of the real world constraints under which the data was produced.It was essential that various preprocessing steps were taken in order to apply the training alogrithm to the concerned text.This included 

Under the Hood :

1. word2vec similarity :
2. Word Movers Distance :
3. Custom Support Vector Classifiers :
4. Logistic Regression : 

**Introduction** : 

Benchmarking algorithms for intent classification: 

Here's summary of different techniques I've used for *Intent *classification. 

All the algorithms were subject to the same training and testing data under the Travel domain. This data can be found in the same folder. The code for the results below is available here. 

**Key: **

word2vec similarity: This is a custom implementation of sentence similarity that is currently deployed on Yolochat.

word mover's distance: Utilises spaCy's 300-dimensional word2vec vectors to calculate similarity b/w sentences. Implemented using textacy. Here's a good explanation for this: link 

Custom SVC: A custom implementation of the Support Vector Classifier using scikit-learn. Utilises the most of the default parameters and a Linear kernel to find the Support Vectors. This also tries to incorporate n-grams which is missing in the rasa implementation. As shown below, 2-grams gave the best accuracy (71%) and were the fastest (0.16s)

Logistic Regression: Probably the simplest classification algorithm, this was also implemented using scikit-learn. Gave decent results (63%) and was relatively fast(0.24s)

**Travel Data Performance**

|           **Algorithm**            | **Accuracy** | **Time Taken** |
| :--------------------------------: | ------------ | -------------- |
|     **Chatclay - Rasa (SVC)**      | 62%          | N/A            |
| **Chatclay - word2vec similarity** | 60%          | 12.69s         |
|     **word mover's distance**      | 67.2%        | 2.45 s         |
|      **Custom SVC : 1-gram**       | 69%          | 0.16s          |
|      **Custom SVC : 2-gram**       | 71%          | 0.16s          |
|      **Custom SVC : 3-gram**       | 65%          | 0.16s          |
|      **Custom SVC : 5-gram**       | 63.8%        | 0.16s          |
|      **Custom SVC : 7-gram**       | 63.7%        | 0.16s          |
|      **Logistic Regression**       | 63.8%        | 0.24s          |

