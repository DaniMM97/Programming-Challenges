### 6 - INVIERTIENDO CADENAS ###
'''
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

print('INVIERTIENDO CADENAS')

def reverse(word):

    reversed_text = ''              #vacío pq luego lo completamos       

    for index in range(0, len(word)):   #revertir el sentido del 'for' 

        reversed_text += word[len(word) - index - 1]    # -1 para llegar a la última posición, sino estaría 'out of range', no existiría ese último número
                                                        #1º: posición 10 (11-0-1), pq en index se cuenta el 0, pero en len() no, entonces letra 11 es index 10 / con el for... pos 9 - 8...
    return reversed_text

print(reverse('Hello World'))