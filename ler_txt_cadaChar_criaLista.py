with open('Text4.txt', 'r') as f:
    cEachChar = f.read()

L=[]
for char in cEachChar:
    L.append(char)

print("###### Impressao de cada item da L:")
x=0
iCountSequence=0
while x < len(L):
    print(L[x])
    if (L[x]=='t' and L[x+1]=='e'):
        iCountSequence+=1
    x+=1
    

print("\n##### Tamanho da L_eachChar: %d\n\n" % len(L))
print("\n##### Count Sequence of 'te': %d\n\n" % iCountSequence)