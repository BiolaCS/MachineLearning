
userMB = ("I", "N", "T", "J")
userMB = list(userMB)

w, h = 8, 2;
outputMB = [[0 for x in range(w)] for y in range(h)]

mbTraits=[]
mbTraits=("E", "I", "S", "N", "T", "F", "J", "P")

for x in range(0, w):
    outputMB[0][x]=mbTraits[x]

for x in range(0, len(userMB)):
    for y in range(0, len(mbTraits)):
        if userMB[x]==mbTraits[y]:
            outputMB[1][y]=1

print(outputMB)


print("---------------")
userPT = ("Achiever", "Analytical", "Command", "Restorative", "Woo")
userPT = list(userPT)

w, h = 34, 2;
outputPT = [[0 for x in range(w)] for y in range(h)]
personalityTraits=[]
personalityTraits=("Achiever", "Activator", "Adaptability", "Analytical", "Arranger", "Belief", "Command", "Communication", "Competition", "Connectedness", "Consistency", "Context", "Deliberative", "Developer", "Discipline", "Empathy", "Focus", "Futuristic", "Harmony", "Ideation", "Includer", "Individualization", "Input", "Intellection", "Learner", "Maximizer", "Positivity", "Relator", "Responsibility", "Restorative", "Self-Assurance", "Significance", "Strategic", "Woo")

for x in range(0, w):
    outputPT[0][x]=personalityTraits[x]

for x in range(0, len(userPT)):
    for y in range(0, len(personalityTraits)):
        if userPT[x]==personalityTraits[y]:
            outputPT[1][y]=1

print(outputPT)

