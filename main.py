trainer_name = input("what is yout name? ")

print(f"Welcome, {trainer_name}!")

print(f"Choose your Pokemon:")
print(f"1. Pikachu")
print(f"2. Charmander")
print(f"3. Squirtle")

pokemon_choice = int(input("Enter Pokemon name (1-3):"))

pokemon_name = ""

if pokemon_choice == 1:
    pokemon_name = "Pikachu"
    pokemon_hp = 420
    print(f"Pikachu is an Electric type!")
    print(f"Pikachu has {pokemon_hp} HP!")
elif pokemon_choice == 2:
    pokemon_name = "Charmander"
    pokemon_hp = 390
    print(f"Charmander is a Fire type!")
    print(f"Charmander has {pokemon_hp} HP!")
elif pokemon_choice == 3:
    pokemon_name = "Squirtle"
    pokemon_hp = 100
    print(f"Squirtle is a Water type!")
    print(f"Squirtle has {pokemon_hp} HP!")
else:
    print(f"Unknown Pokemon!")

print(f" {trainer_name}, chose {pokemon_name}!")

enemy_name = "Charmander"
enemy_hp = 200
enemy_damage = 200


print(f"{pokemon_name} has entered a battle with {enemy_name}!")
print(f"Your {pokemon_name} has {pokemon_hp} HP! and your enemy {enemy_name} has {enemy_hp} HP!")

while pokemon_hp > 0 and enemy_hp > 0:
    print(f"{enemy_name} attacks {pokemon_name} for {enemy_damage} damage!")
    pokemon_hp = pokemon_hp - enemy_damage
    if pokemon_hp <0:
        pokemon_hp = 0
    if pokemon_hp > 0:
        
        print(f"{pokemon_name} has {pokemon_hp} HP left!")
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
        print(f"{pokemon_name} used {attack_name} and did {pokemon_damage} to {enemy_name}")
        enemy_hp = enemy_hp - pokemon_damage
        if enemy_hp <0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} left!")
        if enemy_hp >0:
            continue
        else:
            print(f"Your {pokemon_name} won the battle! {enemy_name} has fainted!")
    else:
        print(f"Your pokemon has {pokemon_hp} and fainted, {enemy_name} won!")
        



