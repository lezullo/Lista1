#4. Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,

#Opção1
class Aluno1:
    def __init__(self, nome, nota1=0, nota2=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def get_media(self):
        return (self.nota1 + self.nota2)/2

vetor_media=[]
for i in range(5):
    nome	= (input('Digite	o Nome do aluno:'))
    nota1	=	float(input('Nota 1:'))  
    nota2	=	float(input('Nota 2:'))          
    aluno=Aluno1(nome,nota1,nota2)
    media=aluno.get_media()
    if(media>=7.0):
      vetor_media.append(media)

print(len(vetor_media))

#---------------------------------------------------------------------------------------------------------
#Opção2
vetor_media=[]
for i in range(5):
    nome	= (input('Digite	o Nome do aluno:'))
    nota1	=	float(input('Nota 1:'))  
    nota2	=	float(input('Nota 2:'))      
    media=(nota1 + nota2)/2
   if(media>=7.0):
      vetor_media.append(media)

print(len(vetor_media))