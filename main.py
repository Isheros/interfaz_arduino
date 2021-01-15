#!/usr/bin/python
# -*- coding: utf-8-*-
import math
import crayons
import msvcrt
from arduino_connection import Arduino_Connection

def print_bar (current, total, prefix = '', unit ='m', char_length = 100):
    progress = '█'
    filledLength = int(char_length * current // total)
    bar = progress * filledLength + '-' * (char_length - filledLength) 
    if current < 25:
      temp = crayons.blue(f'\r{prefix} |{bar}| {current}{unit}')
    elif current >= 25 and current < 50:
      temp = crayons.green(f'\r{prefix} |{bar}| {current}{unit}')
    elif current >= 50 and current < 75:
      temp = crayons.yellow(f'\r{prefix} |{bar}| {current}{unit}')
    elif current >= 75 and current <= 100:
      temp = crayons.red(f'\r{prefix} |{bar}| {current}{unit}')

    print(temp, end ="\r")


if __name__ == "__main__":
  # Inicializamos conexion con arduino
  arduino = Arduino_Connection(8, 101,  'COM2')
  arduino.open_arduino_connection()

  # Logo de escom 
  with open('escom_logo.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
      print(l,end = '')
    print()
  print(crayons.blue('                                     ESCOM'))
  # Datos del alumno
  print(crayons.green('Boleta: '),'2017631241',crayons.green('Grupo: '),'3CV1')
  print(crayons.yellow('Carlos Pimentel González'))

  # Barra en 0 para inicializar 
  print('Presiona ENTER para salir')
  print_bar(0, 100, prefix = 'Temperatura:', unit='°C', char_length = 50)

  # Loop para pedir valores continuamente y actualizar la barra
  while True:
    output = arduino.get_arduino_val()
    print_bar(math.floor(output), 100, prefix = 'Temperatura:', unit='°C',char_length = 50)
    # Si detecta ENTER sale del loop
    if msvcrt.kbhit():
      if ord(msvcrt.getch()) == 13:
        arduino.close_arduino_connection
        break
