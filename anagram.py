### 1 - ANAGRAMA ###
'''
Escribe una función que reciba dos palabras y retorne True or False según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

print('ANAGRAMA')

def anagram(first_word, second_word):

    if first_word.lower() == second_word.lower():  
        return False
    else: 
        return sorted(first_word.lower()) == sorted(second_word.lower())   #ordena las letras alfabéticamente

print(anagram('Roma', 'Amor'))
