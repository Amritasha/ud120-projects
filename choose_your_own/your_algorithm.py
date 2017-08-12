#!/usr/bin/python


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

print "KNeighbors"
print
from sklearn.neighbors import KNeighborsClassifier
t0 = time()
clf = KNeighborsClassifier(n_neighbors=13, weights='distance', algorithm='auto')
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "testing time:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
print "accuracy_score: ", accuracy_score(labels_test, pred)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
