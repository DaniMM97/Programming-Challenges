### 2 - FIBONACCI ###
'''
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
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
        next = fib              

fibonacci()


#u otra opción (hasta el nº 1000)
'''
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
fib(1000)
'''