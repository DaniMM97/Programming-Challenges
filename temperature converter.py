### 42 - CONVERSOR DE TEMPERATURA ###
'''
Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
- En caso contrario retornará un error.
'''

print('CONVERSOR DE TEMPERATURA')

unidad = input("Escribe 'F' para convertir a Celsius; y 'C' para convertir a Fahrenheit: ").upper()
grados = float(input('Indica la temperatura a convertir (en número): '))

def temp_conversor(unidad, grados):

    if "F" in unidad:
        temp_celsius = (grados - 32) / 1.8          
        return f'{temp_celsius:0.2f} ºC'      # 2 decimales

    elif "C" in unidad:
        temp_fahrenheit = grados * 1.8 + 32          
        return f'{temp_fahrenheit:0.2f} ºF'

    else:
        return 'Error'
    
print(temp_conversor(unidad, grados))      