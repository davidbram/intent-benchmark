import spacy
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC

parser = spacy.load('en_core_web_lg')
TRAIN = pd.read_csv('../datasets/travel train.csv')
TEST = pd.read_csv('../datasets/travel test.csv')

def tokenizeText(sample):
    tokens = parser(sample)
    return tokens.vector

#     tokens = parser(sample)
#     lemmas = []
#     for tok in tokens:
#         lemmas.append(tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
#     tokens = lemmas
#     #tokens = [word.lemma_ for word in tokens if word.lemma_ != "-PRON-"]
#     #tokens = [tok for tok in tokens if tok not in set(SYMBOLS)|STOP_WORDS]

#     while "" in tokens:
#         tokens.remove("")
#     while " " in tokens:
#         tokens.remove(" ")
#     while "\n" in tokens:
#         tokens.remove("\n")
#     while "\n\n" in tokens:
#         tokens.remove("\n\n")

#     return tokens


def append_vectors(row):
    sample = row[0]
    vector = tokenizeText(sample)
    size = len(vector)
    row['vector'] = vector
    #row['size'] = size
    return row


def featurize(dataset):
    dataset = dataset.apply(append_vectors, axis = 1)
    return dataset


training_data = featurize(TRAIN)
X_train = training_data['vector']
y_train = training_data['intent']

clf = LinearSVC()
X_train = np.array(list(X_train), dtype=np.float)

clf.fit(X_train, y_train)
def append_svc_response(row):
    utterance = row['vector']
    ip = utterance.reshape(1,-1)
    #ip = np.array(list(utterance),dtype = np.float)
    #ip = pd.Series(utterance)

    response = clf.predict(ip)[0]

    try:
        row['predicted'] = response
        """
        if response[2]:
            row['predicted_score'] = response[2]
        else:
            row['predicted_score'] = 0
        """


        #print("q = {}, ans = {}" .format(utterance,response))

    except Exception as e:
        row['predicted'] = None
        #row['predicted_score'] = 0
        print("q = {}, ans = {}" .format(utterance,None))

    return row

def label_correct_responses(row):
    expected = row['expected intent']
    predicted = row['predicted']

    if expected == predicted:
        row['Correct'] = 1
    else:
        row['Correct'] = 0

    return row

def svc_test(test, write = False):
    test = test.apply(append_svc_response, axis = 1)
    test = test.apply(label_correct_responses, axis = 1)
    print(test['Correct'].mean())

    if write:
        test.to_csv('Word2vec with SVC.csv')

    return test

test_featurized = featurize(TEST)
#test_featurized

test_output = svc_test(test_featurized, False)
#print(test_output)

def predict(utterance):
    row = pd.DataFrame({'utterance':[utterance]})
    row = featurize(row)
    test_input = np.array(list(row['vector']), dtype=np.float)
    response = clf.predict(test_input)[0]
    return response

# r = pd.DataFrame({'utterance':[utterance]})
# r = featurize(r)
# #ip = pd.Series(r['vector'])
# ip = np.array(list(r['vector']), dtype=np.float)

# clf.predict(ip)
# #response = clf.predict(ip)[0]
# #response

# utterance = "places to eat"
# print(predict(utterance))
