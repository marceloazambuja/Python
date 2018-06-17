manipulador = open('Text.txt','r')
textoNovoArquivo = ''
for linha in manipulador:
    linha=linha.rstrip()
    textoNovoArquivo += linha.replace("ta","#")
    print (linha)

print("##########################")
print (textoNovoArquivo)

manipulador.close()

fileWrite = open('Text2.txt',"w")

fileWrite.write(textoNovoArquivo)

fileWrite.close()