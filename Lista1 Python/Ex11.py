#11.Faça um programa completo utilizando classes e métodos que:
#a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#	i. tipoCombustivel.
#	ii. valorLitro
#	iii. quantidadeCombustivel
#b. Possua no mínimo esses métodos:
#	i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
#quantidade de litros que foi colocada no veículo
#	ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
#mostra o valor a ser pago pelo cliente.
#	iii. alterarValor( ) – altera o valor do litro do combustível.
#	iv. alterarCombustivel( ) – altera o tipo do combustível.
#	v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#c. OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível
#total na bomba.

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
       

  