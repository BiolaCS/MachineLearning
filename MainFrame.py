
import csv
import re
import numpy as np

# Input from the backend  
# f = open('Commune App Survey.csv')
# csv_f = csv.reader(f)

UserData = ['2018/03/11 11:46:20 PM MDT', 'Health habits', 'Administration (organizing things)', 'Faithful Serving', 'Leader', '80', '90', '100', '90', '90', '85', '90', '90', '100', '100', '90', '80', '100', '100', '100', '100', '90', '100', '80', '60', '90', '90', '80', '80', '80', '90', '90', '85', '50', '75', '90', '85', '90', '90', 'Adaptability', 'ENTJ', '100', '90', '80', '10', '40', '100']
userMB = UserData[40]
userMB = list(userMB)

mbTraits=[]
mbTraits=("E", "I", "S", "N", "T", "F", "J", "P")

w = len(mbTraits)
outputMB = [[0 for x in range(w)]]

for x in range(0, len(userMB)):
    for y in range(0, len(mbTraits)):
        if userMB[x]==mbTraits[y]:
            outputMB[0][y]=1

outputMB = np.asarray(outputMB)
print(outputMB)



outputSF=[]
strengthTraits=("Achiever", "Activator", "Adaptability", "Analytical", "Arranger", "Belief", "Command", "Communication", "Competition", "Connectedness", "Consistency", "Context", "Deliberative", "Developer", "Discipline", "Empathy", "Focus", "Futuristic", "Harmony", "Ideation", "Includer", "Individualization", "Input", "Intellection", "Learner", "Maximizer", "Positivity", "Relator", "Responsibility", "Restorative", "Self-Assurance", "Significance", "Strategic", "Woo")
userST = ("adaptability")

outputSF = [bool(re.search(userST, i, re.IGNORECASE)) for i in strengthTraits]

outputSF = np.asarray(outputSF)
outputSF =outputSF*1
print(outputSF)



    





 














# Learning happens here


# Output back to the backend

