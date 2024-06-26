# > FUNÇÔES

# append - adiciona elementos no final da lista

lista = [1,3,12,8,2]

print("Antes:",lista)

lista.append(3)

print("Depois:",lista)

# insert -insere elementos nos indices indicados parametro 1 indice 2 valor ele nao substitui se houver valor e sim empurra os elementos pra frente

lista.insert(2,10)
print("Depois Insert:",lista)

# extend -juntar listas ao final da lista em que a função foi usada

lista2=[50,25,35]

lista.extend(lista2)
print(lista)

# pop -  remover elementos espeficicados ou ultimo

lista.pop()

print("dpeois pop sem paramentro: ",lista)

# remove - ele romovo o elemento e não o indice (sempre remove apenas o primeiro que encontra)

lista.remove(50)
print("Depois remove: ", lista)

# count - contar quantas vezes uma variavel aparece

print("Quantidade do elemento 3: ",lista.count(3))

# index - diz o indice de um determinado elemento da lista

print("indice do elemento 12: ", lista.index(12))

# sort - metodo de ordenação da lista

lista.sort()
print(lista)


#ordenar de forma reversa
lista.sort(reverse=True)
print(lista)

# FUNCOES PARA LISTA

#len - conta quantos elementos tem na lista
print(len(lista))
#sum - soma todos os elementos da lista
print(sum(lista))
#min - retonra o menor valor
print(min(lista))
#max - retorna o maior elemento da lista
print(max(lista))