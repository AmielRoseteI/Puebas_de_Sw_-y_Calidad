# -*- coding: utf-8 -*-
"""wordCount.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gcBXw4wtRJ6_kiFm9BBVhvt8TWFUeIH3
"""

#Google Drive Connection
from google.colab import drive
drive.mount('/content/drive')

filename ="/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Problema 1/TC1.txt"

def read_words_from_file(filename):
   words = []
   with open(filename, 'r') as file:
    for line in file:
        words.extend(line.strip().split())
   return words

words = read_words_from_file(filename)
print(words)

import time
start_time = time.time()

def count_word_frequencies(words):
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

tiempo_t = time.time() - start_time

word_counts = count_word_frequencies(words)
resultado = [f"{word}: {count}" for word, count in sorted(word_counts.items())]
resultado.append(f"Time Elapsed: {tiempo_t:.6f} seconds")

print(resultado)
print("Tiempo transcurrido:", (tiempo_t), "segundos.")

resultado_f = "\n".join(resultado)
with open("wordCount.txt", "w") as output_file:
        output_file.write(resultado_f)

pip install pylint

!pylint "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Problema 3/wordCount.ipynb"