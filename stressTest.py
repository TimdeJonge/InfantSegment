from addStress import addStress

testData = []
validData = []
words = []

def compare(trueWord):
    temp = ''
    for letter in trueWord:
        if letter != "\'":
            temp += letter
    baseWord = temp
    [ourGuess, ruleUsed] = addStress(baseWord)
    useValid = False
    for i in range(len(trueWord)):
        if trueWord[i] == "'":
            if ourGuess[i] == "-":
                useValid = True
            else:
                useValid = False
    return [baseWord, ourGuess, trueWord, ruleUsed, useValid]

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

ruleCount = {"SuperStress" : 0, "Default" : 0, "EndVowel" : 0, "OneSyllable" : 0, "TwoSyllable" : 0}
goodRule = {"SuperStress" : 0, "Default" : 0, "EndVowel" : 0, "OneSyllable" : 0, "TwoSyllable" : 0}
badWords = []
for i in range(10):
    [baseWord, ourGuess, trueWord, ruleUsed, useValid] = compare(validData[i])
    print(baseWord, ourGuess, trueWord, ruleUsed, useValid)
    if not useValid:
        with open('badStress.txt', 'a') as f:
            f.write(ourGuess + ', ' + trueWord + '\n')
        badWords.append([ourGuess, trueWord])
    for i in range(len(ruleUsed)):
        ruleCount[ruleUsed] += 1
        if useValid:
            goodRule[ruleUsed] += 1

print(ruleCount, goodRule, "\n", badWords)
print(len(badWords))
for rule in ruleCount:
    print(rule, ruleCount[rule] - goodRule[rule])


# TODO: diagnose ShortVowel rule
# TODO: Document my code because really this is horrible for anyone not me



