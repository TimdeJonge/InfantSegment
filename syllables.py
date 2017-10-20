longVowels = ['i', 'y', 'e', '|', 'a', 'o', 'u', '#', '$', '3', ')']
shortVowels = ['I', 'Y', 'E', '/', 'A', '{', 'Q', '&', 'O', '}', 'V', 'U']
borrowedVowels = ['!', '(', '*', 'c', 'q', '<', 'O', '~', '^']
diphthongs = ['K','L','M','1','2','4','5','6','7','8','9','W','B','X']
vowels = longVowels + shortVowels + borrowedVowels + diphthongs + ['@']
stopConsonant = ["p", "b", "t", "d", "k", "g", "G", "v", "s"]



def syllableSplit(word):
    tempString = ''
    outString = ''
    letterCounter = 0
    rulesUsed = []
    ruleUsed = "NoRule"
    for letter in word:
        tempString+=letter
        if letter in vowels:
            if outString == '':
                outString += tempString

            else:
                # SPECIAL CASES
                if tempString[:3] == 'rts':
                    outString += tempString[:2] +'-' + tempString[2:]

                    ruleUsed = "Exception"
                elif tempString[:3] == 'mbt':
                    outString += tempString[:2] + '-' + tempString[2:]

                    ruleUsed = "Exception"
                elif tempString[:4] == 'lfts':
                    outString += tempString[:3] + '-' + tempString[3:]

                    ruleUsed = "Exception"
                elif tempString[:3] == 'rwt':
                    outString += tempString[:2] + '-' + tempString[2:]

                    ruleUsed = "Exception"
                # GENERAL CASES @
                elif len(tempString) == 1:
                    outString += '-' + tempString

                    ruleUsed = "NoConsonant"

                elif tempString[0] in stopConsonant and outString[-1] == '@':
                    outString += '-' + tempString
                    ruleUsed = "StopConsonant2"
                elif len(tempString) == 2:
                    outString += '-' + tempString
                    ruleUsed = "OneConsonant"


                elif outString[-1] in shortVowels:
                    outString += tempString[0] + '-' + tempString[1:]

                    ruleUsed = "ShortVowel"
                else:
                    outString += tempString[0] + '-' + tempString[1:]
                    ruleUsed = "Default"
            tempString = ''
            rulesUsed.append(ruleUsed)
        letterCounter += 1
    outString += tempString
    return [outString, rulesUsed]

if __name__ == '__main__':
    g = open('sylSplit.txt', 'w')
    with open('corpus.txt', 'r') as f:
        line = f.readline()[:-1]
        while line != '':
            lineOut = ''
            words = line.split(' ')
            for word in words:
                lineOut += syllableSplit(word)[0] + ' '
            g.write(lineOut + '\n')
            line = f.readline()[:-1]


