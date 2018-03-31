import csv
import pickle

# Get features and labels from csv file

# Organize data to be used for running

# just a test:
X = [[75,85,94,100,65,50,80,40,75,95,90,80,80,80,90,100,99,85,75,65,70,70,50,40,60,60,80,100,20,30,100,50,70,100,70,100,75,60,40,70]]

#Running Models:

# (1) Run model on change of habits data:

# load the model from disk
loaded_cohModel = pickle.load(open('finalized_cohModel.sav', 'rb'))

#X_test and Y_test are the data from the app
cohPrediction = loaded_cohModel.predict(X)

print(cohPrediction)

# Classifications for Change of Habits:
# 1 == Consistent Motivation
# 2 == Finding Peace
# 3 == Being Involved in Community
# 4 == Health Habits
# 5 == Balancing Time with Electronics and Life
# 6 == Money Management

# (2) Run model on Small Group data:

# load the model from disk
loaded_SmallGroupModel = pickle.load(open('finalized_SmallGroupModel.sav', 'rb'))

#X_test and Y_test are the data from the app
SmallGroupPrediction = loaded_SmallGroupModel.predict(X)

print(SmallGroupPrediction)

# Classifications for Small Group:
# 1 == Leader
# 2 == Prayer Warrior
# 3 == Normal Member
# 4 == Relational Leader

# (3) Run model on Serve Group data:

# load the model from disk
loaded_ServeGroupModel = pickle.load(open('finalized_ServeGroupModel.sav', 'rb'))

#X_test and Y_test are the data from the app
ServeGroupPrediction = loaded_ServeGroupModel.predict(X)

print(ServeGroupPrediction)

# Classifications for Serve Group:
# 1 == Administration
# 2 == Hospitality
# 3 == Outreach
# 4 == Evangelism
# 5 == Teaching

# (4) Run model on Positive Qualities data:

# load the model from disk
loaded_pqModel = pickle.load(open('finalized_pqModel.sav', 'rb'))

#X_test and Y_test are the data from the app
pqPrediction = loaded_pqModel.predict(X)

print(pqPrediction)

# Classifications for Positive Qualities:
# 1 == Gentleness
# 2 == Wisdom
# 3 == Faithuful Servant
# 4 == Recognizing Faults and Encourage Change
# 5 == Evangelism
# 6 == Good Life Decisions

# return cohPrediction, SmallGroupPrediction, ServeGroupPrediction, pqPrediction
