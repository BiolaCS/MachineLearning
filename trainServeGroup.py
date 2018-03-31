from __future__ import print_function
import csv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


fileName = 'SurveyServeGroup.csv'

# Get data from csv for reading
fullCSV= np.array(list(csv.reader(open(fileName, "r"))))

colCount = fullCSV.shape[1]

# Organize data to be used for training

# Changing the type from string to int.
fullCSV = fullCSV.astype(np.int)

# Split data into labels (Y) and Features (X)
Y = fullCSV[:, 0]
X = fullCSV[:, 1:colCount]


# Train and test Models

# (1) Ensemble with Random Forests (sklearn)

# Random Forest Parameters

# Train test splitting data set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3 ,random_state=0)

# Model fitting
forest = RandomForestClassifier(n_estimators=500)
forest.fit(X_train,y_train)

# Test Random Forest
# Model score
print( 'The Score is: ')
print(forest.score(X_test,y_test))

# save the model to disk
filename = 'finalized_ServerGroupModel.sav'
pickle.dump(model, open(filename, 'wb'))

# Multilayer Perceptron (Tensorflow)


# K Nearest Neighbor?


# Regression Tree? (CART)


# Hybrid NN and Ensemble?
