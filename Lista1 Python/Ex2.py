#2. Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.

def count_consonants(str):
  consonants=0
  show=[]
  str.lower()
  for i in str:
      if i not in "aeiou" and i.isalpha():
            consonants=consonants+1
            show.append(i)
  print('The Consonants:',show)
  print('\nThe number of consonant:', consonants)
  
        
str=input("Please enter a string: ")
count_consonants(str)
