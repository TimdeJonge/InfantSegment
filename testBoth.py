from addStress import addStress
from syllables import syllableSplit
# All code patched together from sylTest or stressTest, documented there
testData = []
validData = []
words = []
wordCount = []

# We can either count each word once, or weighted by frequency. For weighted, use True, else, False.
countingType = True

with open('testset.csv', 'r') as f:
    f.readline()
    line = f.readline()
    while line != '':
        line = line.split(';')
        wordCount.append(int(line[0]))
        words.append(line[1])
        validStr = ""
        for char in line[2]:
            if char != "-":
                validStr += char
        validData.append(validStr)
        testData.append(line[3][:-1])
        line = f.readline()


totalCount = 0
totalGood = 0

def compare(baseWord, trueWord):
    ourGuess = addStress(syllableSplit(baseWord)[0])[0]
    if trueWord.index('\'') == ourGuess.index('\''):
        return [True, ourGuess]
    else:
        return [False, ourGuess]
f = open('badBoth.txt', 'w')
for i in range(11650):
    baseWord = testData[i]
    trueWord = validData[i]
    [result, ourGuess] = compare(baseWord, trueWord)
    if countingType:
        incValue = wordCount[i]
    else:
        incValue = 1

    totalCount += incValue
    if result:
        totalGood += incValue
    else:
        f.write(ourGuess + ', ' + trueWord + '\n')

print("Total success: ", "%.2f" % (totalGood * 100 / totalCount))