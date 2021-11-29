#6.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por
#extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

lista = []
listaMes=['Janeiro','Fevereiro', 'Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
for i in range(1,13):
  temp = float (input("Digite a Temperatura do Mes_%d : " %i))
  lista.append(temp)
mediaAnual = sum(lista)/len(lista)
print("Temperatura Média Anual:",mediaAnual)
print("Meses com temperaturas acima da media:\n")
for j,n in enumerate(lista):
  if (lista[j] >= mediaAnual):
    print(j+1, ' - ', listaMes[j],'Temperatura: %0.2f '%lista[j])