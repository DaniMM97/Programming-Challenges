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
                if num % i == 0:        #si resto = 0 -> divisible y no primo
                    is_divisible = True 

            if is_divisible == False:   #es primo
                print(num)

prime()


print('Opción 2: List Comprehension')

for num in range(2,101):
    if all(num % i != 0 for i in range(2,num)):
       print (num)



print('Opción 3: evitas el if > 1 empezando en 2')

def prime():

    for num in range(2, 101):       #alternativa: (3, 101, 2) así coges solo impares (pares siempre no primos)
                                    #o si (1, 101) metes un 'if num > 1:' justo abajo
        prime = True

        for i in range(2, num):     #se % por todos los números entre 2 y el mismo
            if num % i == 0:        #si resto = 0 -> divisible y no primo
                prime = False

        if prime:                   # == True
            print(num)

prime()


print('Opción 4: Seleccionas solo impares (pares nunca son primos)')

def prime():

    for num in range(3, 101, 2):    #o si (1, 101) metes un 'if num > 1:' justo abajo
                                    
        prime = True

        for i in range(3, num): 
            if num % i == 0:     
                prime = False

        if prime:                
            print(num)

prime()