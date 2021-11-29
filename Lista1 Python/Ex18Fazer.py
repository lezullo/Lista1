#18. Implemente uma classe chamada Carro de acordo com as seguintes regras:
#a. um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque;
#b. o consumo é especificado no construtor e o nível de combustível inicial é 0;
#c. forneça um método andar( ) que simula o ato de dirigir o veículo por uma certa distância, reduzindo nível de combustível no tanque de gasolina;
#d. forneça um método obterGasolina( ), que retorna o nível atual de combustível;
#e. forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:
  def __init__(self, consumo):
    self.consumo = consumo
    self.nivelCombustivel = 0
  
  def andar(self, distancia):
    temp = distancia/self.consumo
    self.nivelCombustivel -= temp
    
  def obterGasolina(self):
    return self.nivelCombustivel
  
  def adicionarGasolina(self, qtd):
    self.nivelCombustivel += qtd
    
meucarro = Carro(10)
meucarro.adicionarGasolina(50)
print("\nNivel atual de combustivel:" ,meucarro.obterGasolina())
meucarro.andar(300)
print("Info:",vars(meucarro))
print("\nNivel atual de combustivel:" ,meucarro.obterGasolina())
