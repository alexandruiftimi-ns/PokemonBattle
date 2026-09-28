import random


trainer_name = input("What is your name? ")
print(f"\nWelcome, {trainer_name}!")


# -------------------- POKÉMON DATA --------------------

pikachu = {
    "name": "Pikachu",
    "type": "Electric",
    "hp": 420,
    "attacks": [
        {"name": "Thunderbolt", "damage": 20},
        {"name": "Electro Ball", "damage": 25},
        {"name": "Electric Shock", "damage": 35},
    ],
    "weakness": "Fire",
}

charmander = {
    "name": "Charmander",
    "type": "Fire",
    "hp": 400,
    "attacks": [
        {"name": "Fire Breath", "damage": 20},
        {"name": "Burnt Ash", "damage": 25},
        {"name": "Duo Attack", "damage": 35},
    ],
    "weakness": "Water",
}

squirtle = {
    "name": "Squirtle",
    "type": "Water",
    "hp": 380,
    "attacks": [
        {"name": "Water Pump", "damage": 20},
        {"name": "Water Spit", "damage": 25},
        {"name": "Bite", "damage": 35},
    ],
    "weakness": "Electric",
}

pokemon = [pikachu, charmander, squirtle]

# --------------------CLAMP HP ----------------------------
def clamp_hp(pokemon):
    if pokemon["hp"] < 0:
        pokemon['hp'] = 0

# -------------------- ENEMY SELECTION --------------------

random_pokemon = random.randrange(len(pokemon))
enemy_pokemon = pokemon[random_pokemon]


# -------------------- PLAYER SELECTION --------------------

while True:
    number = 1

    for current_pokemon in pokemon:
        print(f'{number}. {current_pokemon["name"]}')
        number = number + 1

    pokemon_choice = int(input("\nChoose your Pokémon: "))

    if pokemon_choice <= 0 or pokemon_choice > len(pokemon):
        print("Not a valid Pokémon! Try again.\n")
        continue

    chosen_pokemon = pokemon[pokemon_choice - 1]

    print(f"\n{trainer_name} chose {chosen_pokemon['name']}!")
    break


# -------------------- BATTLE START --------------------

print(
    f"\n{chosen_pokemon['name']} has entered a battle "
    f"with {enemy_pokemon['name']}!"
)

print(
    f"Your {chosen_pokemon['name']} has {chosen_pokemon['hp']} HP, "
    f"and the enemy {enemy_pokemon['name']} has {enemy_pokemon['hp']} HP!"
)


# -------------------- BATTLE LOOP --------------------

while chosen_pokemon["hp"] > 0 and enemy_pokemon["hp"] > 0:

    # Enemy turn
    random_attack = random.randrange(len(enemy_pokemon["attacks"]))
    enemy_attack = enemy_pokemon["attacks"][random_attack]
    enemy_actual_damage = enemy_attack["damage"]
    enemy_is_super_effective = False


    if chosen_pokemon["weakness"] == enemy_pokemon["type"]:
        enemy_actual_damage = enemy_actual_damage * 2
        enemy_is_super_effective = True

    chosen_pokemon["hp"] = chosen_pokemon["hp"] - enemy_actual_damage

    print(
        f"\n{enemy_pokemon['name']} uses {enemy_attack['name']} "
        f"on {chosen_pokemon['name']} and deals "
        f"{enemy_actual_damage} damage!"
    )


    if enemy_is_super_effective:
        print(f"Enemy's {enemy_attack["name"]} is Super Effective!")

    clamp_hp(chosen_pokemon)

    if chosen_pokemon["hp"] > 0:
        print(
            f"{chosen_pokemon['name']} has "
            f"{chosen_pokemon['hp']} HP left!"
        )

        # Player turn
        while True:
            number = 1

            for attack in chosen_pokemon["attacks"]:
                print(f'{number}. {attack["name"]}')
                number = number + 1

            attack_choice = int(input("\nChoose an attack: "))

            if (
                attack_choice <= 0
                or attack_choice > len(chosen_pokemon["attacks"])
            ):
                print("Not a valid attack! Choose a valid one.")
                continue

            chosen_attack = chosen_pokemon["attacks"][attack_choice - 1]

            actual_damage = chosen_attack["damage"]
            is_super_effective = False

            if chosen_pokemon["type"] == enemy_pokemon["weakness"]:
                actual_damage = actual_damage * 2
                is_super_effective = True

            enemy_pokemon["hp"] = enemy_pokemon["hp"] - actual_damage

            print(
                f"\n{chosen_pokemon['name']} used "
                f"{chosen_attack['name']} and did "
                f"{actual_damage} damage to "
                f"{enemy_pokemon['name']}!"
            )

            if is_super_effective:
                print(f"Your {chosen_pokemon["name"]} 's {chosen_attack["name"]} is Super Effective!")

            break

        clamp_hp(enemy_pokemon)

        print(
            f"{enemy_pokemon['name']} has "
            f"{enemy_pokemon['hp']} HP left!"
        )

        if enemy_pokemon["hp"] > 0:
            continue

        print(
            f"\nYour {chosen_pokemon['name']} won the battle! "
            f"{enemy_pokemon['name']} has fainted!"
        )

    else:
        print(
            f"\nYour {chosen_pokemon['name']} has fainted! "
            f"{enemy_pokemon['name']} won the battle!"
        )