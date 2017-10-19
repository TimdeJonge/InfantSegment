from syllables import syllableSplit

testData = []
validData = []
words = []

def compare(trueWord, baseWord):
    [ourGuess, rulesUsed] = syllableSplit(baseWord)
    temp = ''
    for letter in trueWord:
        if letter != "\'":
            temp += letter
    trueWord = temp
    counter = 0
    useValid = [True]
    for i in range(len(trueWord)):
        if trueWord[i] == "-":
            counter += 1
            if ourGuess[i] == "-":
                useValid.append(True)
            else:
                useValid.append(False)
    return [baseWord, ourGuess, trueWord, rulesUsed, useValid]

with open('testset.csv', 'r') as f:
    f.readline()
    line = f.readline()
    while line != '':
        line = line.split(',')
        words.append(line[1])
        validStr = ""
        for char in line[2]:
            if char != "\'":
                validStr += char
        validData.append(validStr)
        testData.append(line[3][:-1])
        line = f.readline()
print(len(testData))

ruleCount = {"NoRule" : 0, "Default" : 0, "Exception": 0, "NoConsonant" : 0,  "ShortVowel" : 0, "OneConsonant" : 0}
goodRule = {"NoRule" : 0, "Default" : 0, "Exception": 0, "NoConsonant" : 0,  "ShortVowel" : 0, "OneConsonant" : 0}
badWords = []
for i in range(3180):
    [baseWord, ourGuess, trueWord, rulesUsed, useValid] = compare(validData[i], testData[i])
    if False in useValid:
        badWords.append(trueWord)
    for i in range(len(rulesUsed)):
        ruleCount[rulesUsed[i]] += 1
        if useValid[i]:
            goodRule[rulesUsed[i]] += 1

print(ruleCount, goodRule, "\n", badWords)

for rule in ruleCount:
    print(rule, ruleCount[rule] - goodRule[rule])
# TODO: Increase size of dataset
# TODO: diagnose ShortVowel rule
# TODO: Document my code because really this is horrible for anyone not me

with open('testresult.csv', 'w') as f:
    f.write("Valid Words, Our Guess, True Results \n")
    for i in range(len(testData)):
        f.write(words[i] + "," + syllableSplit(testData[i])[0] + "," + validData[i] + "\n")

