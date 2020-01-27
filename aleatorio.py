# - -*- coding: utf-8 -*-
# #Les comparto mi versión del juego.
#
#Creo que puedo mejorar la redacción, pero no encuentro palabras sencillas para decir que puede escoger el intervalo donde estará el número aleatorio.
#
#**Adiciones:**
#
#1. Agregué un poco de texto antes y después para crear una motivación para empezar y terminar el juego.
#
#2. Agregué un "error" si es que decide ingresar un número decimal.
#
#**Nota: **Me costó más de 4 horas hacerlo porque soy un super novato, pero me dio mucho gusto cuando logré hacer que el programa hiciera lo que yo quería.

# - -*- coding: utf-8 -*-
import random


def run():
    print ('\nBienvenido a:')
    print ('-------------------------+-----------------------------------------+--------------------------')
    print ('*************************| A D I V I N A  L A  C O N T R A S E Ñ A |**************************')
    print ('-------------------------+-----------------------------------------+--------------------------')
    print ('\n¡Esta computadora ha sido atacada por un virus que borrrá todos los archivos! \n ')
    print ('El programador que lo disñeo creo una contraseña secreta que elimina al virus por completo')
    print ('El malvado programador del virus no es tan malvado, así que dejó estas pistas para encontrar la contraseña secreta:')
    print (' \n1. La contraseña es un número entero.')
    print('2. Tu podrás escoger entre cuáles números se encuentra la contraseña (límite inferior y límite superior).')
    print('')
    print('¡Es tu deber encontrar la contraseña secreta!')
    number_found = False

    low_number = (input('\n'+'Ingresa el intervalo menor: ' + '\n'))
    while type(low_number) != int:
        print ('\n' + str(low_number)  + ' no es un número entero, por favor ingresa solo números enteros.')
        low_number = (input('\n' + 'Vuelve a ingresar el intervalo menor (recuerda que debe ser entero): ' + '\n'))

    high_number = (input('\n' + 'Ingresa el intervalo mayor: ' + '\n'))
    while high_number < low_number:
        print('El intervalo mayor no puede ser más pequeño que el intervalo menor')
        high_number = (input('\n' + 'Vuelve a ingresar el intervalo mayor (recuerda que debe ser mayor que '+ str(low_number) +' ): ' + '\n'))
    while type(high_number) != int:
        print ('\n' + str(high_number)  + ' no es un número entero, por favor ingresa un solo enteros.')
        high_number = (input('\n' + 'Vuelve a ingresar el intervalo mayor (recuerda que debe ser entero): ' + '\n'))

    print('\n'+'La contraseña que debes adivinar está entre '+ str(low_number) + ' y ' + str(high_number) + '.')

    random_number = random.randint(low_number,high_number)

    while not number_found:
        number = int(raw_input('\n' + 'Adivina la contraseña: '))

        if number == random_number:
            print('\n¡Felicidades, encontraste la contraseña!\n :::VIRUS ELIMINADO:::')
            number_found = True
        elif number > random_number:
            print ('Pista: La contraseña es más pequeña que ' + str (number) + '.')
        else:
            print('Pista: La contraseña es más grande.' + str (number) + '.')

if __name__ == '__main__':
    run()