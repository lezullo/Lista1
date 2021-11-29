#5. Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos

vetor_aluno=[]
sum_altura=0
qtd=0
for i in range(3):
    idade	= int(input('Digite a idade do aluno:'))
    altura	= float(input('Digite a altura do aluno:'))
    sum_altura += altura
    if idade>13:
      vetor_aluno.append(altura)
    

sum_altura=sum_altura/3
for i in vetor_aluno:
  if i<sum_altura:
    qtd +=1
print('Altura média:',sum_altura)
print('Quantidade:', qtd)
