# > LISTAS

#preenchendo listas
notas = [10,5,3]

#criando listas vazias
lista =[]

#criando lista vazia com funçao
lista2 = list()

#listas no python aceitam diferentes tipos de dados

lista3 = ["alan",2,3.65,False]

lista_de_listas = [notas, lista, lista2,lista3]

#fatiamento listas (indexação)

print(lista3[0])
print(lista3[1])
print(lista3[2])

#o python tambem aceita indexação de numeros negativos ele vai pegar do final para o inicio

#slices (pedaços da lista)

lista4 = [45,56,65,95,87,98,45]

print(lista4[0:3]) #nesse exemple vai do 0 até o menor que indice 3
print(lista4[3:6])

print(lista4[0:6:2])# o terceiro parametro é o de quantas em quantas casas vai pular


# > PERCORRENDO COM FOR

#percorrendo colocando a lista no lugar do range

for elemento in lista4:
  print(elemento)

#podemos usar a funcao 'len'para retornar o tamanho da lista

print("Tamanho da lista: ",len(lista4))

#percorrendo pelo indice:

for i in range(len(lista4)):
    print(lista4[i])



