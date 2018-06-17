manipulador = open('Text.txt','r')
print("\nMétodo read():\n")
print(manipulador.read())

manipulador.seek(0) # Volta para o início do arquivo

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)
print("\nMétodo readlines():\n")
print(manipulador.readlines())

manipulador.close()