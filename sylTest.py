from syllables import syllableSplit

testData = []
validData = []
words = []
wordCount = []

# We can either count each word once, or weighted by frequency. For weighted, use True, else, False.
countingType = True


def compare(trueWord, baseWord):
    """Compare the verified split version of a word to our guess. Return our guess, the rules used to determine this,
        and the evaluation of these rules."""

    # trueWord still involves a stress mark, but we're not testing for that yet.
    # We first remove the apostrophe, then test on.
    temp = ''
    for letter in trueWord:
        if letter != "\'":
            temp += letter
    trueWord = temp
    useValid = [True]

    [ourGuess, rulesUsed] = syllableSplit(baseWord)
    # this works since vowels are agreed on. Since syllable splits take up 1 character, any reasonable model will
    # end up at the same indexes for vowels, and so this testing is independent per syllable.
    for i in range(len(trueWord)):
        if trueWord[i] == "-":
            if ourGuess[i] == "-":
                useValid.append(True)
            else:
                useValid.append(False)
    return [ourGuess, rulesUsed, useValid]


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
        wordCount.append(int(line[0]))
        line = f.readline()

ruleCount = {"NoRule": 0, "Default": 0, "Exception": 0, "NoConsonant": 0,  "ShortVowel": 0, "OneConsonant": 0,
             "StopConsonant": 0}
goodRule = {"NoRule": 0, "Default": 0, "Exception": 0, "NoConsonant": 0,  "ShortVowel": 0, "OneConsonant": 0,
            "StopConsonant": 0}
badWords = []
f = open('badWords.txt', 'w')
for i in range(11650):
    baseWord = testData[i]
    trueWord = validData[i]
    [ourGuess, rulesUsed, useValid] = compare(trueWord, baseWord)
    if False in useValid:
        f.write(str(wordCount[i]) + ', ' + ourGuess + ', ' + trueWord + ', ' + str(rulesUsed) + '\n')
    for i in range(len(rulesUsed)):
        if countingType:
            ruleCount[rulesUsed[i]] += wordCount[i]
            if useValid[i]:
                goodRule[rulesUsed[i]] += wordCount[i]
        else:
            ruleCount[rulesUsed[i]] += 1
            if useValid[i]:
                goodRule[rulesUsed[i]] += 1
f.close()

print(ruleCount)
print(goodRule, '\n')
for rule in ruleCount:
    print(rule + ":", "%.2f" % (goodRule[rule]*100 / ruleCount[rule]) )

totalCount = 0
totalGood = 0
for rule in goodRule:
    if rule != "NoRule":
        totalGood += goodRule[rule]
        totalCount += ruleCount[rule]

print("Total success: ", "%.2f" % (totalGood*100 / totalCount))