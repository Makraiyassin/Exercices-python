from model.player import  Player,Warrior
from model.weapon import  Weapon
# from model.batiment import  Batiment,Immeuble,Magasin,Banque

knife = Weapon("knife",4)

player = Player("Héro",26,3)
player.set_weapon(knife)
warrior = Warrior("DarkWarrior",18,5)

#-------------------------------------------------------------------------------
i=1

while player.get_pv() > 0 and warrior.get_pv() > 0:

    print("tour", i)
    i+=1

    player.attack_player(warrior)
    print(player.get_pseudo(),"attaque",warrior.get_pseudo())

    print("Joueur {} / pv: {} / attack: {} + {}".format(player.get_pseudo(),player.get_pv(),player.get_attack(),player.weapon.get_damage_amount() if player.has_weapon() else 0))
    print("Joueur {} / pv: {} / attack: {} + {} / armor: {}".format(warrior.get_pseudo(),warrior.get_pv(),warrior.get_attack(),warrior.weapon.get_damage_amount() if warrior.has_weapon() else 0,warrior.get_armor_point()))
    #-------------------------------------------------------------------------------
    if player.get_pv() <= 0 or warrior.get_pv() <= 0:
        break

    print("tour", i)
    i+=1

    warrior.attack_player(player)
    print(warrior.get_pseudo(),"attaque",player.get_pseudo())

    print("Joueur {} / pv: {} / attack: {} + {}".format(player.get_pseudo(),player.get_pv(),player.get_attack(),player.weapon.get_damage_amount() if player.has_weapon() else 0))
    print("Joueur {} / pv: {} / attack: {} + {} / armor: {}".format(warrior.get_pseudo(),warrior.get_pv(),warrior.get_attack(),warrior.weapon.get_damage_amount() if warrior.has_weapon() else 0 , warrior.get_armor_point()))
    #-------------------------------------------------------------------------------
