print("PDAMED")
print()

print("DATA")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

#data = dia, mes, ano

print()

print("CADASTRO")
print()

nome = input("Nome:")
print()

docIdent = input("Documento de Identificação:")
print()

print("Data De Nascimento")
print()

#VARIÁVEIS DATA DE NASCIMENTO
diaNasc = int(input("Dia:"))
mesNasc = int(input("Mês:"))
anoNasc = int(input("Ano:"))

print()

#VARIÁVEIS IDADE
anosIdade = ano - anoNasc
mesIdade = mes - mesNasc

print("Idade:", anosIdade, "Anos e", mesIdade, "Meses")
print()

#IDOSO - acima de 60 anos
#CRIANÇA - abaixo de 12 anos
#SEM PREFERÊNCIA - entre 13 e 59 anos

if anosIdade < 12:
  print("PREFERÊNCIA CRIANÇA")
elif anosIdade >= 60:
  print("PREFERÊNCIA IDOSO")
else:
  print("SEM PREFERÊNCIA POR IDADE")

print()

print("ENTRADA")
print()

print("AMBULÂNCIA  |  RECEPÇÃO")
print()


#Variáveis de Classificação de Risco
morte = int();
atendimento = int();
gravidade = int();
classificacao = int();
evolucaoMorte = int();


print("Risco de evolução para morte?") #Pergunta 1
print("1- Sim | 2- Não")
morte = int(input())
print()

if morte == 1:
  print("Necessidade de atendimento imediato?") #Pergunta 2
  print("1- Sim | 2- Não")
  atendimento = int(input())
  print()


  if atendimento == 1:
    classificacao = "EMERGÊNCIA"
    print(classificacao)
    print()
    print("Caso gravíssimo, com necessidade atendimento imediato e risco de morte.")
    print()

  else:
    print("Risco significativo de evoluir para morte?") #Pergunta 3
    print("1- Sim | 2- Não")
    evolucaoMorte = int(input())
    print()

    if evolucaoMorte == 1:
      classificacao = "MUITA URGÊNCIA"
      print(classificacao)
      print()
      print("Caso grave e risco significativo de evoluir para morte.")
      print()

    else:
      classificacao = "URGÊNCIA"
      print(classificacao)
      print()
      print("Caso de gravidade moderada, necessidade de atendimento médico, sem risco imediato.")
      print()

else:
  print("Gravidade?") #Pergunta 4
  print("1- Baixa | 2- Média | 3- Nenhuma")
  gravidade = int((input()))
  print()

  if gravidade == 2:
    classificacao = "URGÊNCIA"
    print(classificacao)
    print()
    print("Caso de gravidade moderada, necessidade de atendimento médico, sem risco imediato.")
    print()

  elif gravidade == 1:
    classificacao = "POUCA URGÊNCIA"
    print(classificacao)
    print()
    print("Caso para atendimento preferencial nas UPAS")
    print()

  elif gravidade == 3:
    classificacao = "SEM URGÊNCIA"
    print(classificacao)
    print()
    print("Caso para atendimento no posto de saúde ou UPA mais próxima da residência.\nAtendimento de acordo com o horário de chegada.\n- Queixas crônicas; resfriados; contusões; escoriações; dor de garganta; ferimentos que não requerem fechamento e outros.")
    print()