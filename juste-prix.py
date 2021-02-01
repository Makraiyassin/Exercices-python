import statistics
from random import shuffle
import random

# Exercice: juste prix

prix = random.randrange(1, 1000)
nombre = int(input("choisissez un nombre entre 1 et 1000: "))

while nombre != prix:
    if nombre < prix:
        print("votre nombre est trop petit")
        nombre = int(input("choisissez-en un autre: "))
    elif nombre > prix:
        print("votre nombre est trop grand")
        nombre = int(input("choisissez-en un autre: "))
print("vous avez trouver le juste prix")
