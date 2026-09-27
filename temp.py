pikachu = {
    "name": "Pikachu",
    "type": "Electric",
    "hp": 420,
    "damage": 20
}
charmander = {
    "name" : "Charmander",
    "type": "Fire",
    "hp": 390,
    "damage": 25
}

squirtle = {
    "name": "Squirtle",
    "type": "Water",
    "hp": 400,
    "damage": 20
}

pokemon =[pikachu, charmander, squirtle]

index = 0

while index < 3:
    current_pokemon = pokemon [index]

    print(f'{current_pokemon["name"]} is an {current_pokemon["type"]} type with {current_pokemon["hp"]} hp and {current_pokemon["damage"]} damage!')
    index = index + 1