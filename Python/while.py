# > Estruturas de repetição (laços)

#WHILE

numsort = 9

numesc = int(input("informe um numero entre 1 e 20: "))

while numesc != numsort:
  print("Você errou tente novamente!")
  numesc = int(input("informe um numero entre 1 e 20: "))

print("Parabens voce acertou!")


# > Estrutura controlavel (usar contador)aparentemente o phyton nao entende i++

i=0

while i<=5:
  print(i)
  i=i+1
