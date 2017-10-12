shortVowels = ['I', 'Y', 'E', '/', 'A', '{', '&', 'Q', 'O', '}', 'V', 'U', '@']
longVowels = ['i', 'y', 'e', '&', 'a', 'o', 'u', "E", "U", "O", "A", "@"]
def syllableSplit(line):
    words = line.split(' ')
    for word in words:
        pass
        # TODO: Wait for vowelReplacer to be complete


g = open('syllableCorpus.txt', 'w')
with open('vowelReplaced.txt', 'r') as f:
    line = f.readline()
    while line!='':
        editedLine = syllableSplit(line)
        g.write(line.replace(' ', ''))
        line = f.readline()
