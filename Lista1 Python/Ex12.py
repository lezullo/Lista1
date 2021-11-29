#12. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o  do mês por extenso

data = input("Digite a data de nascimento (dd/mm/aaaa): ")
lista_data = data.split("/")
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes_extenso = meses[int(lista_data[1])-1]
print(lista_data[0] + " de " + mes_extenso + " de " + lista_data[2])