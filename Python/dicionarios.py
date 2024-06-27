# > DICIONARIO

# parecido com lista só da nomes aos indices atraves de chaves

#criando um dicionario

dicionario = {} #cria um dicionario vazio
dicionario = dict() #cria um dicionario vazio
dicionario = {'nome': 'Alan','idade':33,'altura': 1.77}

print(dicionario)

print(dicionario['altura']) #imprimir elemento especifico

dicionario['programador']=True

print(dicionario)

#percorrer um dicionario

for variavel in dicionario:
  print(variavel) # esse formato imprime apenas a chave

for chave in dicionario:
  print(chave,dicionario[chave]) # esse formato imprime a chave e o valor

#como verificar se uma chava existe dentro do dicionario

print('peso' in dicionario)
print('altura' in dicionario)