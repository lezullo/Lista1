#7. Crie uma classe para representar datas com as seguintes regras:
#a. deve ter três atributos: o dia, o mês e o ano;
#b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos;
#c. encapsule cada um dos atributos;
#d. forneça o método __str__ para retornar uma representação da data como string. Considere que a data
#deve ser formatada mostrando o dia, o mês e o ano separados por barra (/);
#e. forneça uma operação para avançar uma data para o dia seguinte.

class bombaCombustivel():  
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel=quantidadeCombustivel

    def abastecerPorValor(self, valorPago):
        quantlitros = valorPago/self.valorLitro
        self.quantidadeCombustivel = self.quantidadeCombustivel + (quantlitros)
        return quantlitros

    def abastecerPorLitro(self, quantidadeLitros):
        valorPago = quantidadeLitros*self.valorLitro
        self.quantidadeCombustivel = self.quantidadeCombustivel + quantidadeLitros
        return valorPago

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        return self.valorLitro

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade
        return self.quantidadeCombustivel

Jose = bombaCombustivel('gasolina', 7.05, 15 )
Jose.abastecerPorLitro(10)
print(Jose.abastecerPorValor(10))
print(Jose.quantidadeCombustivel)
       

  
