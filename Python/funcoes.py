# criando funcções no Python - "def" cria funcção

def saudacao(nome):
  print(f"Seja bem vindo {nome}!")
  print("É um prazer ter voce aqui :D")

saudacao('Alan')

# com mais de um paramentro

def saudacao(nome, curso):
  print(f"Seja bem vindo {nome}!")
  print(f"É um prazer ter voce aqui no curso de {curso} :D")

saudacao('Alan','Python')

# definindo um paramentro default na função

def saudacao(nome, curso="Cobra"):
  print(f"Seja bem vindo {nome}!")
  print(f"É um prazer ter voce aqui no curso de {curso} :D")

saudacao('Jojo')

#funcoes com retorno

def soma(n1,n2):
  return n1+n2

resultado = soma(5,7)
print(resultado)

def calculadora(n1,n2,op='+'):
  if op == "+":
    return soma(n1,n2)
  elif op == "-":
    return n1-n2

resultado = calculadora(10,20,"+")
print(resultado)

resultado = calculadora(10,20,"-")
print(resultado)