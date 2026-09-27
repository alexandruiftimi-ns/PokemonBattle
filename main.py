import random
trainer_name = input("what is yout name? ")

print(f"Welcome, {trainer_name}!")


pikachu = {
    "name" : "Pikachu",
    "type": "Electric",
    "hp": 420,
    "attacks": [
        {
            "name": "Thunderbolt",
            "damage": 20
        },
        {
            "name": "Electro Ball",
            "damage": 25
        },
        {
            "name": "Electric Shock",
            "damage": 35
        }
        
    ]
}
charmander = {
    "name" : "Charmander",
    "type": "Fire",
    "hp": 400,
    "attacks": [
        {
            "name": "Fire Breath",
            "damage": 20
        },
        {
            "name": "Burnt Ash",
            "damage": 25
        },
        {
            "name": "Duo Attack",
            "damage": 35
        }
        
    ]
}

squirtle = {
    "name" : "Squirtle",
    "type": "Water",
    "hp": 380,
    "attacks": [
        {
            "name": "Water Pump",
            "damage": 20
        },
        {
            "name": "Water Spit",
            "damage": 25
        },
        {
            "name": "Bite",
            "damage": 35
        }
        
    ]
}
pokemon = [pikachu, charmander, squirtle]

random_pokemon = random.randrange(len(pokemon))
enemy_pokemon = pokemon[random_pokemon]


while True:
    number = 1
    for current_pokemon in pokemon:
        print(f'{number}.{current_pokemon["name"]}')
        number = number +1
    pokemon_choice = int(input("Choose your Pokemon: "))
    if pokemon_choice <= 0 or pokemon_choice > len(pokemon):
        print("Not a valid Pokemon! Try again")
        continue
    else:
        chosen_pokemon = pokemon[pokemon_choice - 1]
        print(f" {trainer_name}, chose {chosen_pokemon["name"]}!")
        break


print(f"{chosen_pokemon["name"]} has entered a battle with {enemy_pokemon["name"]}!")
print(f"Your {chosen_pokemon["name"]} has {chosen_pokemon["hp"]} HP! and your enemy {enemy_pokemon["name"]} has {enemy_pokemon["hp"]} HP!")

while chosen_pokemon["hp"] > 0 and enemy_pokemon["hp"] > 0:
    random_attack = random.randrange(len(enemy_pokemon["attacks"]))
    enemy_attack = enemy_pokemon["attacks"][random_attack]
    print(f"{enemy_pokemon["name"]} uses {enemy_attack["name"]} on {chosen_pokemon["name"]} and deals {enemy_attack["damage"]} damage!")
    chosen_pokemon["hp"] = chosen_pokemon["hp"] - enemy_attack["damage"]
    if chosen_pokemon["hp"] <0:
        chosen_pokemon['hp'] = 0
    if chosen_pokemon["hp"] > 0:
        print(f"{chosen_pokemon["name"]} has {chosen_pokemon["hp"]} HP left!")


        while True:
            number = 1
            for attacks in chosen_pokemon["attacks"]:
                print(f'{number}.{attacks["name"]}')
                number = number +1
            attack_choice = int(input("Enter attack (1-3): "))
            if attack_choice <= 0 or attack_choice >len(chosen_pokemon["attacks"]):
                print("Not a valid attack! Choose a valid one.")
                continue
            else:
                chosen_attack = chosen_pokemon["attacks"][attack_choice - 1]
                print(f"{chosen_pokemon["name"]} used {chosen_attack["name"]} and did {chosen_attack["damage"]} to {enemy_pokemon["name"]}")
                enemy_pokemon["hp"] = enemy_pokemon["hp"] - chosen_attack["damage"]
            break

        if enemy_pokemon["hp"] <0:
            enemy_pokemon["hp"] = 0
        print(f"{enemy_pokemon["name"]} has {enemy_pokemon["hp"]} left!")
        if enemy_pokemon["hp"] >0:
            continue
        else:
            print(f"Your {chosen_pokemon["name"]} won the battle! {enemy_pokemon["name"]} has fainted!")
    else:
        print(f"Your pokemon has {chosen_pokemon["hp"]} and fainted, {enemy_pokemon["name"]} won!")
        



