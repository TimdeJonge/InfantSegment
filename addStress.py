longVowels = ['i', 'y', 'e', '|', 'a', 'o', 'u', '#', '$', '3', ')']
shortVowels = ['I', 'Y', 'E', '/', 'A', '{', 'Q', '&', 'O', '}', 'V', 'U', '@']
borrowedVowels = ['!', '(', '*', 'c', 'q', 'O', '<', '~', '^']
diphthongs = ['K','L','M','1','2','4','5','6','7','8','9','W','B','X']
vowels = longVowels + shortVowels + borrowedVowels + diphthongs
mostVowels = longVowels + shortVowels[:-1] + borrowedVowels + diphthongs


def addStress(word):
    ruleUsed = "OneSyllable"
    if '-' not in word:
        outString = ''
        for letter in word:
            if letter in vowels:
                outString += "\'"
            outString += letter
        return outString
    else:
        syllables = word.split('-')
        stressed = -1
        if word[:2] in ["Af", "IN", "me", "na", "Op", "tu"]:
            stressed = 0
            ruleUsed = "WOW"
        if word[:3] == "Ant":
            stressed = 0
            ruleUsed = "WOW"
        for i in range(len(syllables)):
            for letter in syllables[i]:
                if letter in diphthongs and syllables[i][-1] not in vowels and stressed == -1:
                    stressed = i
                    ruleUsed = "SuperStressD"
                if letter in longVowels and syllables[i][-1] not in vowels and stressed == -1:
                    stressed = i
                    ruleUsed = "SuperStressL"

        if word[-1] in mostVowels and '@' not in syllables[len(syllables) - 2] and stressed == -1:
            stressed = len(syllables) - 2
            ruleUsed = "EndVowel"
        if syllables[-2][-1] not in vowels and '@' not in syllables[len(syllables) - 2] and stressed == -1:
            stressed = len(syllables) - 2
            ruleUsed = "OtherRule"
        elif stressed == -1 and len(syllables) == 2 and '@' not in syllables[0]:
            stressed = 0
            ruleUsed = "TwoSyllables"
        elif stressed == -1:
            ruleUsed = "Default"
            lenSyl = len(syllables)
            for i in range(lenSyl):
                if '@' not in syllables[i] and 'IN' not in syllables[i]:
                    stressed = i

    counter = 0
    wordOut = ''
#    for syllable in syllables:
#        if stressed == counter:
#            wordOut += "\'"
#        wordOut+= syllable + "-"
#        counter += 1
    for syllable in syllables:
        if stressed == counter:
            for letter in syllable:
                if letter in vowels:
                    wordOut += "\'"
                wordOut += letter
        else:
            wordOut += syllable
        counter += 1
    return wordOut

if __name__ == '__main__':
    g = open('stress.txt','w')
    with open('sylSplit.txt', 'r') as f:
        line = 'a'
        for _ in range(50000):
            line = f.readline()[:-1]
            words = line.split(' ')
            lineOut = ''
            for word in words:
                lineOut += addStress(word) + ' '
            g.write(lineOut + '\n')


# TODO: Clean up code
