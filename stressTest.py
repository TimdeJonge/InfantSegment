from addStress import addStress

validData = []
words = []
wordCount = []

# We can either count each word once, or weighted by frequency. For weighted, use True, else, False.
countingType = True

def compare(trueWord):
    """Compare the verified stressed version of a word to our guess. Return our guess, the rule used to determine this,
        and the evaluation of these rules."""
    temp = ''
    for letter in trueWord:
        if letter != "\'":
            temp += letter
    baseWord = temp
    [ourGuess, ruleUsed] = addStress(baseWord)
    temp = ''
    for letter in trueWord:
        if letter != "-":
            temp += letter
    trueWord = temp
    useValid = False
    if trueWord.index('\'') == ourGuess.index("\'"):
        useValid = True
    else:
        useValid = False
    return [baseWord, ourGuess, ruleUsed, useValid]

with open('testset.csv', 'r') as f:
    f.readline()
    line = f.readline()
    while line != '':
        line = line.split(';')
        wordCount.append(int(line[0]))
        words.append(line[1])
        validData.append(line[2])
        line = f.readline()

ruleCount = {"SuperStressD": 0, "SuperStressL": 0, "Default": 0, "EndVowel": 0, "OneSyllable": 0, "TwoSyllables": 0,
             "OtherRule": 0, "Exception": 0}
goodRule = {"SuperStressD": 0, "SuperStressL": 0, "Default": 0, "EndVowel": 0, "OneSyllable": 0, "TwoSyllables": 0,
            "OtherRule": 0, "Exception": 0}
totalGood = 0
totalCount = 0


for i in range(11650):
    trueWord = validData[i]
    [baseWord, ourGuess, ruleUsed, useValid] = compare(trueWord)
    if not useValid:
         with open('badStress.txt', 'a') as f:
             f.write(ourGuess + ', ' + trueWord + ', ' + ruleUsed + '\n')
    if countingType:
        incValue = wordCount[i]
    else:
        incValue = 1
    ruleCount[ruleUsed] += incValue
    totalCount += incValue
    if useValid:
        totalGood += incValue
        goodRule[ruleUsed] += incValue

print(ruleCount)
print(goodRule, '\n')
for rule in ruleCount:
    print(rule + ":", "%.2f" % (goodRule[rule]*100 / ruleCount[rule]) )
print("Total success: ", "%.2f" % ((totalGood-goodRule["OneSyllable"])*100 / (totalCount - ruleCount["OneSyllable"])))

# TODO: Document my code because really this is horrible for anyone not me



