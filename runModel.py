from __future__ import print_function

import csv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import pandas as pd
import pickle


# Get features and labels from csv file

# Organize data to be used for running


#Running Models:

# (1) Run model on change of habits data:

# load the model from disk
loaded_cohModel = pickle.load(open('finalized_cohModel.sav', 'rb'))

#X_test and Y_test are the data from the app
cohPrediction = loaded_cohModel.score(X_test, Y_test)
print(cohPrediction)

# (2) Run model on Small Group data:

# load the model from disk
loaded_SmallGroupModel = pickle.load(open('finalized_SmallGroupModel.sav', 'rb'))

#X_test and Y_test are the data from the app
SmallGroupPrediction = loaded_SmallGroupModel.score(X_test, Y_test)

print(SmallGroupPrediction)

# (3) Run model on Serve Group data:

# load the model from disk
loaded_ServeGroupModel = pickle.load(open('finalized_ServeGroupModel.sav', 'rb'))

#X_test and Y_test are the data from the app
ServeGroupPrediction = loaded_ServeGroupModel.score(X_test, Y_test)

print(ServeGroupPrediction)

# (4) Run model on Positive Qualities data:

# load the model from disk
loaded_pqModel = pickle.load(open('finalized_pqModel.sav', 'rb'))

#X_test and Y_test are the data from the app
pqPrediction = loaded_pqModel.score(X_test, Y_test)

print(pqPrediction)

# return cohPrediction, SmallGroupPrediction, ServeGroupPrediction, pqPrediction
