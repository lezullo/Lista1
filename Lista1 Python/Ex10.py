#10. Implemente a classe Funcionário com um nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
#Crie o método aumentar_salario(percentual_aumento) que aumente o salário do funcionário em uma certa porcentagem. 
#Escreva um pequeno programa que teste sua class

class Funcionario():
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def getNome(self):
    return self.nome
  
  def getSalario(self):
    return self.salario

  def aumentarSalario(self, porcentagemDeAumento=0):
    self.salario += self.salario * (porcentagemDeAumento)/100
    
x = Funcionario("Any", 1000)
print("Nome: ", x.getNome(), ", Salario", x.getSalario())
x.aumentarSalario(10)
print("Nome: ", x.getNome(), ", Salario", x.getSalario())