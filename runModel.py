import csv
import pickle
import sys
# Get features and labels from csv file

# Organize data to be used for running


if __name__ == '__main__':

	if len(sys.argv) > 1:
		
		if sys.argv[1] != '':
			# test case (so you dont have to enter a bunch of stuff)
			if sys.argv[1] == "sample":
				print("sample")
				X = [[75,85,94,100,65,50,80,40,75,95,90,80,80,80,90,100,99,85,75,65,70,70,50,40,60,60,80,100,20,30,100,50,70,100,70,100,75,60,40,70]]
			else:
				# Need to strip the userID off the front
				strippedInput = sys.argv[29:]
				X = [[strippedInput]]
			#Running Models:

			# (1) Run model on change of habits data:

			# load the model from disk
			loaded_cohModel = pickle.load(open('finalized_cohModel.sav', 'rb'))

			#X_test and Y_test are the data from the app
			cohPrediction = loaded_cohModel.predict(X)

			print(cohPrediction)

			# Classifications for Change of Habits:
			cohArray = []

			cohArray.append("Consistent Motivation")
			cohArray.append("Finding Peace")
			cohArray.append("Being Involved in Community")
			cohArray.append("Health Habits")
			cohArray.append("Balancing Time with Electronics and Life")
			cohArray.append("Money Management")

			# (2) Run model on Small Group data:

			# load the model from disk
			loaded_SmallGroupModel = pickle.load(open('finalized_SmallGroupModel.sav', 'rb'))

			#X_test and Y_test are the data from the app
			SmallGroupPrediction = loaded_SmallGroupModel.predict(X)

			print(SmallGroupPrediction)

			SmallGroupPredictionArray = []
			# Classifications for Small Group:
			SmallGroupPredictionArray.append("Leader")
			SmallGroupPredictionArray.append("Prayer Warrior")
			SmallGroupPredictionArray.append("Normal Member")
			SmallGroupPredictionArray.append("Relational Leader")

			# (3) Run model on Serve Group data:

			# load the model from disk
			loaded_ServeGroupModel = pickle.load(open('finalized_ServeGroupModel.sav', 'rb'))

			#X_test and Y_test are the data from the app
			ServeGroupPrediction = loaded_ServeGroupModel.predict(X)

			print(ServeGroupPrediction)

			ServeGroupPredectionArray = []
			# Classifications for Serve Group:
			ServeGroupPredectionArray.append("Administration")
			ServeGroupPredectionArray.append("Hospitality")
			ServeGroupPredectionArray.append("Outreach")
			ServeGroupPredectionArray.append("Evangelism")
			ServeGroupPredectionArray.append("Teaching")

			# (4) Run model on Positive Qualities data:

			# load the model from disk
			loaded_pqModel = pickle.load(open('finalized_pqModel.sav', 'rb'))

			#X_test and Y_test are the data from the app
			pqPrediction = loaded_pqModel.predict(X)

			print(pqPrediction)

			pqPredictionArray = []
			# Classifications for Positive Qualities:
			pqPredictionArray.append("Gentleness")
			pqPredictionArray.append("Wisdom")
			pqPredictionArray.append("Faithuful Servant")
			pqPredictionArray.append("Recognizing Faults and Encourage Change")
			pqPredictionArray.append("Evangelism")
			pqPredictionArray.append("Good Life Decisions")

			file = open("../PostListener/singleOutput.txt", "a")
			file.write(sys.argv[1][:28] + '\n')
			file.write(cohArray[cohPrediction[0]] + '\n')
			file.write(SmallGroupPredictionArray[SmallGroupPrediction[0]] + '\n')
			file.write(ServeGroupPredectionArray[ServeGroupPrediction[0]] + '\n')
			file.write(pqPredictionArray[pqPrediction[0]] + '\n')
		else:
			print("Argument present but empty")
	else:
		print("No arguments were passed")

