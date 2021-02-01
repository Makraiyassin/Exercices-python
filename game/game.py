from model.player import  Player,Warrior
from model.weapon import  Weapon
# from model.batiment import  Batiment,Immeuble,Magasin,Banque

knife = Weapon("knife",4)

player = Player(input("choisissez le nom du protagoniste: "),int(input("entrez ses points de vie: ")),int(input("entrez ses poin d'attaque (qui seront ajouté de +4 car le héro est equipé d'une arme): ")))
player.set_weapon(knife)
warrior = Warrior(input("choisissez le nom de l'antagoniste (qui sera invulnérable pendant les trois premier tour grace à son armure): "),int(input("entrez ses points de vie: ")),int(input("entrez ses poin d'attaque: ")))

#-------------------------------------------------------------------------------
i=1

while player.get_pv() > 0 and warrior.get_pv() > 0:
    print("_______________________________________________________________________")

    print("tour", i)
    i+=1
    print("_______________________________________________________________________")
    player.attack_player(warrior)
    print(player.get_pseudo(),"attaque",warrior.get_pseudo())
    print("_______________________________________________________________________")
    print("Joueur {} / pv: {} / attack: {} + {}".format(player.get_pseudo(),player.get_pv(),player.get_attack(),player.weapon.get_damage_amount() if player.has_weapon() else 0))
    print("Joueur {} / pv: {} / attack: {} + {} / armor: {}".format(warrior.get_pseudo(),warrior.get_pv(),warrior.get_attack(),warrior.weapon.get_damage_amount() if warrior.has_weapon() else 0,warrior.get_armor_point()))
    #-------------------------------------------------------------------------------
    if player.get_pv() <= 0 or warrior.get_pv() <= 0:
        break
    print("_______________________________________________________________________")

    print("tour", i)
    i+=1
    print("_______________________________________________________________________")

    warrior.attack_player(player)
    print(warrior.get_pseudo(),"attaque",player.get_pseudo())
    print("_______________________________________________________________________")
    print("Joueur {} / pv: {} / attack: {} + {}".format(player.get_pseudo(),player.get_pv(),player.get_attack(),player.weapon.get_damage_amount() if player.has_weapon() else 0))
    print("Joueur {} / pv: {} / attack: {} + {} / armor: {}".format(warrior.get_pseudo(),warrior.get_pv(),warrior.get_attack(),warrior.weapon.get_damage_amount() if warrior.has_weapon() else 0 , warrior.get_armor_point()))
    #-------------------------------------------------------------------------------
