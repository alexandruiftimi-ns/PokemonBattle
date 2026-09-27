trainer_name = input("what is yout name? ")

print(f"Welcome, {trainer_name}!")


pikachu = {
    "name" : "Pikachu",
    "type": "Eletrict",
    "hp": 420,
    "attacks": ['Thunder Bolt', 'Electro Ball', 'Electic Shock']
}
charmander = {
    "name" : "Charmander",
    "type": "Fire",
    "hp": 390,
    "damage": 25
}
squirtle = {
    "name" : "Squirtle",
    "type": "Water",
    "hp": 400,
    "damage": 20
}

pokemon = [pikachu, charmander, squirtle]


number = 1
for current_pokemon in pokemon:
    print(f'{number}.{current_pokemon["name"]}')
    number = number +1

pokemon_choice = int(input("Choose your Pokemon:"))

chosen_pokemon = pokemon[pokemon_choice - 1]

print(f" {trainer_name}, chose {chosen_pokemon["name"]}!")

enemy_name = "Charmander"
enemy_hp = 200
enemy_damage = 200


print(f"{chosen_pokemon["name"]} has entered a battle with {enemy_name}!")
print(f"Your {chosen_pokemon["name"]} has {chosen_pokemon["hp"]} HP! and your enemy {enemy_name} has {enemy_hp} HP!")

while chosen_pokemon["hp"] > 0 and enemy_hp > 0:
    print(f"{enemy_name} attacks {chosen_pokemon["name"]} for {enemy_damage} damage!")
    chosen_pokemon["hp"] = chosen_pokemon["hp"] - enemy_damage
    if chosen_pokemon["hp"] <0:
        chosen_pokemon['hp'] = 0
    if chosen_pokemon["hp"] > 0:
        
        print(f"{chosen_pokemon["name"]} has {chosen_pokemon["hp"]} HP left!")
        while True:
            print("Choose your attack:")
            print("1. Quick Attack")
            print("2. Thunderbolt")
            print("3. Electro Ball")

            attack_choice = int(input("Enter attack (1-3): "))

            if attack_choice == 1:
                pokemon_damage = 20
                attack_name = "Quick Attack"
            elif attack_choice == 2:
                pokemon_damage = 35
                attack_name = "Thunderbolt"
            elif attack_choice == 3:
                pokemon_damage = 30
                attack_name = "Electro Ball"
            else:
                print("Unknown attack!")
                continue

            break
        print(f"{chosen_pokemon["name"]} used {attack_name} and did {chosen_pokemon["damage"]} to {enemy_name}")
        enemy_hp = enemy_hp - pokemon_damage
        if enemy_hp <0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} left!")
        if enemy_hp >0:
            continue
        else:
            print(f"Your {chosen_pokemon["name"]} won the battle! {enemy_name} has fainted!")
    else:
        print(f"Your pokemon has {chosen_pokemon["hp"]} and fainted, {enemy_name} won!")
        



