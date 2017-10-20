longVowels = ['i', 'y', 'e', '|', 'a', 'o', 'u', '#', '$', '3', ')']
shortVowels = ['I', 'Y', 'E', '/', 'A', '{', 'Q', '&', 'O', '}', 'V', 'U', '@']
borrowedVowels = ['!', '(', '*', 'c', 'q', 'O', '<', '~', '^']
diphthongs = ['K','L','M','1','2','4','5','6','7','8','9','W','B','X']
vowels = longVowels + shortVowels + borrowedVowels + diphthongs
mostVowels = longVowels + shortVowels[:-1] + borrowedVowels + diphthongs


def addStress(word):
    ruleUsed = "OneSyllable"
    if '-' not in word:
        for letter in word:
            if letter in mostVowels:
                return ["\'" + word, ruleUsed]
        return [word, ruleUsed]
        # TODO: Add stress to the vowel, not to the syllable in case 1 syllable

    else:
        print("WOW")
        syllables = word.split('-')
        stressed = -1
        for i in range(len(syllables)):
            for letter in syllables[i]:
                if (letter in diphthongs or letter in longVowels) and syllables[i][-1] not in vowels and stressed == -1:
                    stressed = i
                    ruleUsed = "SuperStress"
        if (word[-1] in mostVowels or syllables[-2][-1] not in vowels) and '@' not in syllables[len(syllables) - 2] and stressed == -1:
            stressed = len(syllables) - 2
            ruleUsed = "EndVowel"
        elif stressed == -1 and len(syllables) == 2 and '@' not in syllables[1]:
            stressed = 1
            ruleUsed = "TwoSyllables"
        elif stressed == -1:
            ruleUsed = "Default"
            for i in range(len(syllables)):
                if '@' not in syllables[i]:
                    stressed = i

    counter = 0
    wordOut = ''
    for syllable in syllables:
        if stressed == counter:
            wordOut += "\'"
        wordOut+= syllable + "-"
        counter += 1
    return [wordOut[:-1], ruleUsed]
# CURRENT CODE KEPT ALIVE FOR TESTING, BELOW CODE IS FOR ACTUAL WORK

#    for syllable in syllables:
#        if stressed == counter:
#            for letter in syllable:
#                if letter in vowels:
#                    wordOut += "\'"
#                wordOut += letter
#        else:
#            wordOut += syllable
#        counter += 1
#    print(wordOut)
#    return wordOut
if __name__ == '__main__':
    print(addStress('aN-G@-brAxt'))

if False:
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
