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
print(pokemon[0])
print(pokemon[1])
print(pokemon[2])
print(pokemon[0]["name"])

print(f'{pikachu["name"]} is an {pikachu["type"]} type with {pikachu["hp"]} hp and {pikachu["damage"]} damage!')
print(f'{charmander["name"]} is an {charmander["type"]} type with {charmander["hp"]} hp and {charmander["damage"]} damage!')
print(f'{squirtle["name"]} is an {squirtle["type"]} type with {squirtle["hp"]} hp and {squirtle["damage"]} damage!')