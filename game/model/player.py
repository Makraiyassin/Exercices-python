class  Player:
    def __init__(self,pseudo,pv,attack):
        self.pseudo=pseudo
        self.pv=pv
        self.attack=attack
        self.weapon= None
        print("Bienvenue au joueur {} / pv: {} / attack: {}".format(pseudo,pv,attack))

    def get_pseudo(self):
        return self.pseudo

    def get_pv(self):
        return self.pv

    def get_attack(self):
        return self.attack

    def damage(self,damage):
        self.pv-= damage

    def attack_player(self, target_player):
        degat = self.attack
        
        if self.has_weapon():
            degat += self.weapon.get_damage_amount()

        target_player.damage(degat)


    # méthode pour changer l'arme du joueur
    def set_weapon(self, weapon):
        self.weapon = weapon

    # méthode pour verifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None

class Warrior(Player):
    def __init__(self,pseudo,pv,attack):
        super().__init__(pseudo,pv,attack)
        self.armor = 3
        print("Bienvenue au guerrier {} / pv: {} / attack: {} / armor:{}".format(pseudo,pv,attack,self.armor))

    def damage(self,damage):
        if self.armor > 0:
            self.armor-= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("les points d'armur ont été recharger")

    def get_armor_point(self):
        return self.armor

