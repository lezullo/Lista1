#1. Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as notas lidas e a respectiva média.

#Duvida: Qual dessas duas opções seriam a mais adequada para o que foi pedido? Ou teria alguma outra melhor? Fiquei com essa dúvida.

#Opção1
class Aluno1:
    def __init__(self, nome, nota1=0, nota2=0, nota3=0,nota4=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

        txt = 'Nome: ' + self.nome
        txt += '\nNotas: %2.1f, %2.1f, %2.1f, %2.1f' % (self.nota1, self.nota2, self.nota3, self.nota4)
        txt += '\nMédia: %2.1f' % ((self.nota1+ self.nota2+ self.nota3+ self.nota4)/4)
        return (print(txt))

a1 = Aluno1('João Pedro',10,9,10,9)
a2 = Aluno1('Ana',9,9,9,9)

#Opção2
class Aluno2:
    def __init__(self, nome, nota1=0, nota2=0, nota3=0,nota4=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def get_media(self):
        return (self.nota1 + self.nota2 + self.nota3 +self.nota4)/4

    def __str__(self):
        txt = 'Nome: ' + self.nome
        txt += '\nNotas: %2.1f, %2.1f, %2.1f, %2.1f' % (self.nota1, self.nota2, self.nota3, self.nota4)
        txt += '\nMédia: %2.1f' % self.get_media()
        return txt

a3 = Aluno2('Pedro Torees',8,10,10,9)
a4 = Aluno2('Maria Luiza',7,7.5,9,9)
print(a4.__str__())
