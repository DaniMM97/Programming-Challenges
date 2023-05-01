### 19 - CONVERSOR TIEMPO ###
'''
Crea una función que reciba días, horas, minutos y segundos (en enteros) y retorne su resultado en milisegundos.
'''

print('CONVERSOR TIEMPO')

input_days = int(input('days: '))
input_hours = int(input('hours: '))
input_minutes = int(input('minutes: '))
input_seconds = int(input('seconds: '))

def time_converter(days:int, hours:int, minutes:int, seconds:int):

    mil_days = days * 24 * 60 * 60 * 1000
    mil_hours = hours * 60 * 60 * 1000
    mil_minutes = minutes * 60 * 1000
    mil_seconds = seconds * 1000

    miliseconds = mil_days + mil_hours + mil_minutes + mil_seconds
    return miliseconds

print(time_converter(input_days, input_hours, input_minutes, input_seconds), 'miliseconds')