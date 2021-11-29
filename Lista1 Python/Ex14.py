#14. Faça um programa que solicite dois valores e imprima todos os pares entre o menor valor e o maior valor. Caso
#os números digitados sejam iguais, enviar mensagem ao usuário e imprimir os pares de 1 a 10 como exemplo.

def imprime_pares(maior,menor):

  if menor!=maior:
    for i in range (menor,maior):   
        if i%2==0:
          print(i)  
  else:
    print("Numeros iguais")
    for i in range (1,10):
        if i%2==0:  
          print(i) 

num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))
if num1>num2:
  imprime_pares(num1,num2)
else:
  imprime_pares(num2,num1)
