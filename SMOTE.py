# Isaiah Bernados
# SMOTE for Commune App
# Last Revised 3/29/2018

# This code seeks to apply the SMOTE algorithm to the data retrieved from Surveys
# so that we will have more data to train on.

import csv
import numpy as np
from collections import Counter
from imblearn.over_sampling import SMOTE

# Choose a file name to SMOTE that data.

fileName = 'SurveySmallGroup.csv'
#fileName = 'SurveyPositiveQualities.csv'
#fileName = 'SurveyServeGroup.csv'
#fileName = 'SurveyChangeOfHabits.csv'

# Get data from csv for reading
fullCSV= np.array(list(csv.reader(open(fileName, "r"))))


colCount = fullCSV.shape[1]

# Changing the type from string to int.
fullCSV = fullCSV.astype(np.int)

# Split data into labels (Y) and Features (X)
Y = fullCSV[:, 0]
X = fullCSV[:, 1:colCount]

print('Original dataset shape {}'.format(Counter(Y)))

# SMOTE algorithm on data
sm = SMOTE(ratio = 'all', random_state=42)
X_res, Y_res = sm.fit_sample(X, Y)

print('Resampled dataset shape {}'.format(Counter(Y_res)))

# Concatenating features to labels for output to csv file.
fullRes = X_res
fullRes = np.insert(fullRes,0,Y_res, axis = 1)

Printing to csv
fd = open(fileName, 'a')
np.savetxt(fd,  fullRes, fmt='%1.0f', delimiter=",")
fd.close()
