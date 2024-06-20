# > ESTRUTURAS DE CONTROLE DE FLUXO

# > Estruturas condicionais 

idade = 18

if idade >=18:
  print("Voce é maior de idade!")

  # a saida ou retorno fica na prxima linhja iniciando com alguns espaços a identação faz parte do codigo.

  # o Phyton nao usa parenteses nem chaves para conter o if e else o ao invés disso ele usa : indicando que a condição vem logo após

else:
  print("Voce é menor de idade")


media = 7

if media >=7:
  print("APROVADO(A)")
elif media >=5:  #no python nao existe else if é elif
  print("RECUPERAÇÃO")
else:
  print("REPROVADO(A)")

presenca=70


if media >=7 and presenca >=70:
  print("APROVADO!")
else:
  print("REPROVADO")


