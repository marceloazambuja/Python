import re
L=[]
with open('Text4.txt', 'r') as f:
    for line in f:
        sequence = (re.findall(r'^t+\w*', line))
        L.append(sequence)

print("\n##### Sequences: ", L)