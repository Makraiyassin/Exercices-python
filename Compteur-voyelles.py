import statistics
from random import shuffle
import random

# Exercice Function: Compteur de voyelle

def get_vowels_numbers(word):
    compteur = 0
    for letter in word:
        if letter in ["a","e","i","o","u"]:
            compteur += 1
    print("votre mot contient {} voyelles".format(compteur))
mot = input("entrez un mot afin que nous comptions ses voyelles: ")
get_vowels_numbers(mot)
