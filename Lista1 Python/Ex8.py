#8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia dinheiro para a vítima?"
#e. "Já trabalhou com a vítima?"
#No final, o programa deve emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita";
#entre 3 e 4, como "Cúmplice", e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


op = 1
while (op ==1):
  lista = []
  print(" Interrogatório:\n")
  lista.append(int(input("Telefonou para a vítima ? 1- SIM ou 0-NAO :" )))
  lista.append(int(input("Esteve no local do crime? 1- SIM ou 0-NAO :" )))
  lista.append(int(input("Mora perto da vítima? 1- SIM ou 0-NAO : ")))
  lista.append(int(input("Devia para a vítima? 1- SIM ou 0-NAO : " )))
  lista.append(int(input("Já trabalhou com a vítima? 1- SIM ou 0-NAO : " )))
  if (sum(lista) <2):
   print("\n Pessoa Inocente \n")
  elif (sum(lista) == 2):
      print("\n Pessoa Suspeita \n")
  elif ( 3 <=sum(lista)<= 4 ):
      print("\n Pessoa Cúmplice \n")
  else:
      print("\n Pessoa Assassino \n ")
  op = int(input("Deseja Interrogar outra Pessoa ? 1- SIM ou 2 - NAO :"))
print("\n")