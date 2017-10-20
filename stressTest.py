from addStress import addStress

testData = []
validData = []
words = []
wordcount = []

def compare(trueWord):
    syllableCount = trueWord.count("-") + 1
    temp = ''
    for letter in trueWord:
        if letter != "\'":
            temp += letter
    baseWord = temp
    [ourGuess, ruleUsed] = addStress(baseWord)
    useValid = False
    for i in range(len(trueWord)):
        if trueWord[i] == "\'":
            if ourGuess[i] == "\'":
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
        wordcount.append(int(line[0]))
        validData.append(line[2])
        testData.append(line[3][:-1])
        line = f.readline()

ruleCount = {"SuperStressD": 0, "SuperStressL": 0, "Default": 0, "EndVowel": 0, "OneSyllable": 0, "TwoSyllables": 0, "OtherRule": 0, "WOW": 0}
goodRule = {"SuperStressD": 0, "SuperStressL": 0, "Default": 0, "EndVowel": 0, "OneSyllable": 0, "TwoSyllables": 0, "OtherRule": 0, "WOW": 0}
badWords = []
trueGood = 0
total = 0
for i in range(11650):
    [baseWord, ourGuess, trueWord, ruleUsed, useValid] = compare(validData[i])
    if not useValid:
        # with open('badStress.txt', 'a') as f:
            # f.write(ourGuess + ', ' + trueWord + ', ' + ruleUsed + '\n')
        badWords.append([ourGuess, trueWord])
    ruleCount[ruleUsed] += wordcount[i]
    total += wordcount[i]
    if useValid:
        trueGood += wordcount[i]
        goodRule[ruleUsed] += wordcount[i]
print(trueGood, total, trueGood/total)
print(ruleCount, goodRule, "\n", badWords)
print(len(badWords))
for rule in ruleCount:
    print(rule, goodRule[rule]/ruleCount[rule])

# TODO: Document my code because really this is horrible for anyone not me



