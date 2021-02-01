class Batiment:
    def __init__(self, adresse, etages):
        self.etages = etages
        self.adresse = adresse
    
    def get_etages(self):
        return self.etages

    def get_adress(self):
        return self.adresse


class Immeuble(Batiment):
    def __init__(self,adresse,etages,fenetres):
        Batiment.__init__(self,adresse,etages)
        self.fenetres = fenetres
    
    def get_fenetres(self):
        return self.fenetres


class Magasin(Batiment):
    def __init__(self,adresse,etages,rayons):
        Batiment.__init__(self,adresse,etages)
        self.rayons = rayons
    def get_rayons(self):
        return self.rayons


class Banque(Batiment):
    def __init__(self,adresse,etages,name,coffres):
        Batiment.__init__(self,adresse,etages)
        self.name = name
        self.coffres = coffres
    def get_name(self):
        return self.name

    def get_coffres(self):
        return self.coffres

#4 immeubles

# immeuble1 = Immeuble(input("entrer l'adresse de l'immeuble1: "),input("Combien d'étage possède l'immeuble1: "),input("combien de fenetre possède l'immeuble1: "))
immeuble2 = Immeuble("28 rue de la Grevande", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble4 = Immeuble("120 rue pleiades", 8, 4)



# print("l'immeuble situé à {} possède {} étages et {} fenêtres".format(immeuble1.get_adress(),immeuble1.get_etages(),immeuble1.get_fenetres()))
print("l'immeuble' situé à {} possède {} étages et {} fenêtres".format(immeuble4.get_adress(),immeuble4.get_etages(),immeuble4.get_fenetres()))

#2 supermarché
magasin1 = Magasin("28 rue de la Grevande", 5, 6)
magasin2 = Magasin("120 rue pleiades", 8, 4)
print("le magasin situé à {} possède {} étages et {} rayons".format(magasin2.get_adress(),magasin2.get_etages(),magasin2.get_rayons()))

#1 banque
banque1 = Banque("120 rue pleiades", 4,"Fortis",3)
print("la banque {} situé à {} possède {} étages et {} coffres".format(banque1.get_name(),banque1.get_adress(),banque1.get_etages(),banque1.get_coffres()))
