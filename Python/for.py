# >FOR

for varial in range(10):
  print(varial)

#a variavel do inicio é a que vai ser automaticamente incrementada e rande define a regra

for var2 in range (1,5):
  print(var2)

# nesse segundo exemplo a var2 vai iniciar em 1 como definido no parametro de range e terminar em menor que 5

for var3 in range(1,12,3):
  print(var3)

#quando se acrecenta o terceiro paramentro ele dis de quantas em quatas casas vai ser pulado


soma = 0

for i in range(1,4):
  nota = float(input(f"Informe a nota {i}: "))
  soma = soma + nota

print(soma/3)

#para adicionar uma variavel dentro de um texto antes das aspas adicinar o f e dentro de aspas colocar a variavel entre chaves

