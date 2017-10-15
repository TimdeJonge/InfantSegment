longVowels = ['i', 'y', 'e', '|', 'a', 'o', 'u', '#', '$', '3', ')']
shortVowels = ['I', 'Y', 'E', '/', 'A', '{', 'Q', '&', 'O', '}', 'V', 'U', '@']
borrowedVowels = ['!', '(', '*', 'c', 'q', 'O', '~', '^']
diphthongs = ['K','L','M','1','2','4','5','6','7','8','9','W','B','X']
vowels = longVowels + shortVowels + borrowedVowels + diphthongs
mostVowels = longVowels + shortVowels[:-1] + borrowedVowels + diphthongs


def addStress(word):
    if '-' not in word:
        return(word)
    else:
        syllables = word.split('-')
        stressed = -1
        for i in range(len(syllables)):
            for letter in syllables[i]:
                if (letter in diphthongs or letter in longVowels) and syllables[i][-1] not in vowels and stressed == -1:
                    stressed = i
        if (word[-1] in mostVowels or syllables[-2][-1] not in vowels) and stressed == -1:
                stressed = len(syllables) - 2
        elif stressed == -1 and len(syllables) == 2 and '@' not in syllables[1]:
                stressed = 1
        elif stressed == -1:
                stressed = 0

    counter = 0
    wordOut = ''
    for syllable in syllables:
        if stressed == counter:
            wordOut += '\''
        wordOut += syllable
        counter += 1
    print(wordOut)
    return wordOut
# TODO: Evaluate how to deal with a open syllable with long vowel
# TODO: Ponder whether to get stronger exceptions on @


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
