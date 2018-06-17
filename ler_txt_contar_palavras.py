from collections import Counter

with open('Text3.txt') as f:
    ocorrencias = Counter(f.read().split())
    print('\n##### Mais comuns: ', Counter(ocorrencias).most_common(2))

print("\n\n##### Total de Ocorrências:", ocorrencias)
#print(ocorrencias)

print ('\n\n##### Total de Palavras: ', sum(ocorrencias.values()), '\n\n')


#print("##### Palavras mais comuns:")
#import re
#words = re.findall(r'\w+', open('Text3.txt').read().lower())
#print(Counter(ocorrencias).most_common(2))

#cnt = Counter()
#for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#    cnt[word] += 1
#print (cnt)