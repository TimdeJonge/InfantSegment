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
        line = line.split(';')
        words.append(line[1])
        validStr = ""
        for char in line[2]:
            if char != "\'":
                validStr += char
        validData.append(validStr)
        testData.append(line[3][:-1])
        line = f.readline()

ruleCount = {"NoRule" : 0, "Default" : 0, "Exception": 0, "NoConsonant" : 0,  "ShortVowel" : 0, "OneConsonant" : 0, "StopConsonant1" : 0, "StopConsonant2" : 0}
goodRule = {"NoRule" : 0, "Default" : 0, "Exception": 0, "NoConsonant" : 0,  "ShortVowel" : 0, "OneConsonant" : 0, "StopConsonant1" : 0, "StopConsonant2" : 0}
badWords = []
for i in range(11650):
    [baseWord, ourGuess, trueWord, rulesUsed, useValid] = compare(validData[i], testData[i])
    if False in useValid:
        with open('badWords.txt', 'a') as f:
            f.write(ourGuess + ', ' + trueWord + '\n')
        badWords.append([ourGuess, trueWord])
    for i in range(len(rulesUsed)):
        ruleCount[rulesUsed[i]] += 1
        if useValid[i]:
            goodRule[rulesUsed[i]] += 1

print(ruleCount, goodRule, "\n", badWords)
print(len(badWords))
for rule in ruleCount:
    print(rule, ruleCount[rule] - goodRule[rule])
# TODO: Document my code because really this is horrible for anyone not me

with open('testresult.csv', 'w') as f:
    f.write("Valid Words, Our Guess, True Results \n")
    for i in range(len(testData)):
        f.write(words[i] + "," + syllableSplit(testData[i])[0] + "," + validData[i] + "\n")


