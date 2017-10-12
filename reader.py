g = open('nospacecorpus.txt', 'w')

with open('corpus.txt', 'r') as f:
    line = f.readline()
    while line!='':
        g.write(line.replace(' ', ''))
        line = f.readline()