def vowelReplace(line):
    oldVowels = ['i','y','e','|','a','o','u',')','!','(','*','<']
    newVowels = ['i:', 'y:', 'e:', '&:', 'a:', 'o:', 'u:', "E:", "i::", "y::", "U:", "O:"]
    for i in range(len(oldVowels)):
        line = line.replace(oldVowels[i], newVowels[i])
    return(line)

g = open('vowelReplaced.txt', 'w')
with open('corpus.txt', 'r') as f:
    line = f.readline()
    while line!='':
        editedLine = vowelReplace(line)
        g.write(editedLine)
        line = f.readline()