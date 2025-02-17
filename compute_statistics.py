# -*- coding: utf-8 -*-
"""compute_statistics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19seSbKbfDhXsPoi2Z2lnYSKKA7QXqlKv
"""

#Google Drive Connection
from google.colab import drive
drive.mount('/content/drive')

filename ="/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Problema 1/TC1.txt"

def read_numbers_from_file(filename):
   numbers = []
   with open(filename, 'r') as file:
    for line in file:
      try:
        numbers.append(float(line.strip()))
      except ValueError:
                print(f"Error: Invalid data '{line.strip()}' ignored.")
   return numbers
   numbers

numbers = read_numbers_from_file(filename)

import time
start_time = time.time()

import statistics
longitud = len(numbers)
media =  sum(numbers)/len(numbers)
mediana = statistics.median(numbers)
moda = statistics.mode(numbers)
desvi = statistics.stdev(numbers)
varianza = statistics.variance(numbers)
tiempo_t = time.time() - start_time

resultado = (
        f"Longitud: {longitud}\nMedia: {media}\nMediana: {mediana}\n"
        f"Moda: {moda}\nDesviación Estándar: {desvi}\nVarianza: {varianza}\n"
        f"Tiempo transcurrido: {tiempo_t:.6f} segundos"
 )
 print(resultado)

with open("StatisticsResults.txt", "w") as output_file:
        output_file.write(resultado)

pip install pylint

!pylint "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Problema 1/compute_statistics.ipynb"