with open('Text4.txt', 'r') as f:
    sEachLine = f.readlines()

L_words=[]
for line in sEachLine:
    sEachWord = line.split(" ")
    L_words.append(sEachWord)
    print(sEachWord)

x=0

print ("\n\n###### Agora imprimir cada item da lista, resultado é identico: ")
while x<len(L_words):
    print(L_words[x])
    x+=1

print("\n\n###### Tamanho da L_words: %d\n\n" % len(L_words))