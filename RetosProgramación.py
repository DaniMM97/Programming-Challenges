### 0 - FIZZBUZZ ###
'''
Enunciado: Escribe un programa que muestre por consola (con un print) los números
de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), 
sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

print('FIZZBUZZ')

def fizzbuzz():

    for i in range(1, 101):    
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
fizzbuzz()

print()


### 1 - ANAGRAMA ###
'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

print('ANAGRAMA')

def anagram(first_word, second_word):

    if first_word.lower() == second_word.lower():  
        return False
    else: 
        return sorted(first_word.lower()) == sorted(second_word.lower())   #ordena los números alfabéticamente

print(anagram('Roma', 'Amor'))   #input antes y aquí pones las variables del input

print()


### 2 - FIBONACCI ###
'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
'''

print('FIBONACCI')

def fibonacci():

    prev = 0
    next = 1

    for i in range(0, 50):      #de 0 a 50(49), hay 50 números
        print(prev, end=' ')             #(a) 0 / 1 / 1 / 2
        fib = prev + next       #(b) 0+1 / 1+1 / 1+2 / 2+3
        prev = next             #(a) 1 / 1 / 2 / 3     (Esto es lo que pasa al print())
        next = fib              #(b) 0+1 / 1+1 / 1+2 / 2+3

fibonacci()

print()

#or (hasta el nº 1000)
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
fib(1000)
print()


### 3 - NÚMEROS PRIMOS ###
'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

print('NÚMEROS PRIMOS')

def prime():

    for num in range(101):

        if num > 1:

            is_divisible = False

            for i in range(2, num):     #se % por todos los números entre 2 y el mismo
                if num % i == 0:        #es una división sin resto (divisible ok)
                    is_divisible = True 

            if is_divisible == False:
                print(num)

prime()
print()


#LISTA N PRIMOS
def prime():

    for num in range(2, 101):       #(3, 101, 2) así coges solo impares (pares siempre no primos)
                                    #o si (1, 101) metes un 'if num > 1:' justo abajo.

        prime = True

        for i in range(2, num):     #se % por todos los números entre 2 y el mismo
            if num % i == 0:        #es una división sin resto (divisible ok)
                prime = False

        if prime:                   # == True
            print(num)

prime()
print()


            #List Comprehension
for num in range(2,101):
    if all(num % i != 0 for i in range(2,num)):
       print (num)
print()


### 4 - ÁREA DE UN POLÍGONO ###
'''
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
'''


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

print()


### 19 - CONVERSOR TIEMPO ###
'''
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
'''

print('CONVERSOR TIEMPO')

def time_converter(days:int, hours:int, minutes:int, seconds:int):

    mil_days = days * 24 * 60 * 60 * 1000
    mil_hours = hours * 60 * 60 * 1000
    mil_minutes = minutes * 60 * 1000
    mil_seconds = seconds * 1000

    miliseconds = mil_days + mil_hours + mil_minutes + mil_seconds
    return miliseconds

input_days = int(input('days: '))
input_hours = int(input('hours: '))
input_minutes = int(input('minutes: '))
input_seconds = int(input('seconds: '))

print(time_converter(input_days, input_hours, input_minutes, input_seconds), 'miliseconds')


### 42 - CONVERSOR DE TEMPERATURA ###
'''
Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
  y su unidad ("C" o "F").
- En caso contrario retornará un error.
'''

print('CONVERSOR DE TEMPERATURA')

def temp_conversor(unidad, grados): #no está bin del todo, pq aquí separamos el nº de ºC/F, lo suyo sería todo junto
                                    #puedes poner un try y except también...
    if "ºF" in unidad:
        temp_celsius = (grados - 32) / 1.8          
        return f'{temp_celsius:0.2f} ºC'  #2 decimales

    elif "ºC" in unidad:
        temp_fahrenheit = grados * 1.8 + 32          
        return f'{temp_fahrenheit:0.2f} ºF'

    else:
        return 'Error'
    #puedes incluir un input tanto de C/F como del número, y ya incluirlo en el print
print(temp_conversor('ºC', 34))

print()