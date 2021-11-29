#13.Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
#vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
#são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram
#ignorados. Faça um programa que leia uma sequência de caracteres e diga se esta é um palíndromo ou não

frase = input('Digite uma frase : ')
frase = frase.replace(" ", "")
numero_de_letras = len(frase)
normal = frase[0:numero_de_letras]
inverso = frase[numero_de_letras::-1]
if normal == inverso :
    print ('Essa frase é um palindromo')
else:
    print ('Essa frase não é um palidromo')