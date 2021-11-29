#16. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

eleitores = int(input("Digite o número total de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
votantes = 0
while (votantes < eleitores):
  voto = int(input("Digite 1 para votar no candidato 1, 2 para o candidato 2 e 3 para o candidato 3:"))
  if (voto == 1):
    candidato1 +=+ 1
  elif (voto == 2):
    candidato2 += 1
  elif (voto == 3):
    candidato3 += 1
  votantes += 1
print("O candidato 1 teve", candidato1, "votos.")
print("O candidato 2 teve", candidato2, "votos.")
print("O candidato 3 teve", candidato3, "votos.")
