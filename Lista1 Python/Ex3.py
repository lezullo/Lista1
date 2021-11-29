#3. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

n=0
vetor=[[],[],[]]
while	(n<20):
    numero	=	int(input('Digite	um	número:	'))     
    vetor[0].append(numero)
    if numero%2 ==0:
      vetor[1].append(numero)
    else:
      vetor[2].append(numero)
    n +=1

print("Todos os numeros:",vetor[0])
print("Pares:",vetor[1])
print("Impares:",vetor[2])
	