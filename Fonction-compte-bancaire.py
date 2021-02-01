import statistics
from random import shuffle
import random

#Exercice fonction:

def credit():
    argent = int(input("Combien d'argent as-tu dans ton compte bancaire? "))
    produit = int(input("Vous avez achetez un produit coûtant: "))
    reste = argent - produit

    print("suite à votre achat d'un produit de ",produit,"€, il vous reste: "+ str(reste),"€ sur votre compte.")

credit()
