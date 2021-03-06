#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from sklearn.metrics import accuracy_score
'''
t0 = time()
clf = svm.SVC(kernel='linear')
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
print accuracy_score(labels_test, clf.predict(features_test))
print "testing time:", round(time()-t1, 3), "s"
'''

'''
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
'''

'''
print "small dataset"
t0 = time()
clf = svm.SVC(kernel='linear')
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
print accuracy_score(labels_test, clf.predict(features_test))
print "testing time:", round(time()-t1, 3), "s"
'''

'''
print
print "rbf c=10.0"
t0 = time()
clf = svm.SVC(kernel='rbf', C=10.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
print accuracy_score(labels_test, clf.predict(features_test))
print "testing time:", round(time()-t1, 3), "s"

print
print "rbf c=100.0"
t0 = time()
clf = svm.SVC(kernel='rbf', C=100.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
print accuracy_score(labels_test, clf.predict(features_test))
print "testing time:", round(time()-t1, 3), "s"

print
print "rbf c=1000.0"
t0 = time()
clf = svm.SVC(kernel='rbf', C=1000.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
print accuracy_score(labels_test, clf.predict(features_test))
print "testing time:", round(time()-t1, 3), "s"
'''
print
print "rbf c=10000.0"
t0 = time()
clf = svm.SVC(kernel='rbf', C=10000.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print accuracy_score(labels_test,pred )
print "testing time:", round(time()-t1, 3), "s"
print pred[10]
print pred[26]
print pred[50]

import numpy as np
print "no of chris mails predicted : "
print np.count_nonzero(pred==1)
#########################################################


