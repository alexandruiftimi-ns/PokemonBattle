import tkinter as tk

root = tk.Tk()
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
chosen_pokemon = pikachu
enemy_pokemon = charmander

root.title("Pokemon Battle 1:1")
root.resizable(False, False)
root.minsize(900,600)
title = tk.Label(root, text="POKEMON BATTLE")
title.grid(row=0, column=0, columnspan=2)

player_name = tk.Label(root, text="Player")
player_name.grid(row=1, column=0)

enemy_name= tk.Label(root, text="Enemy")
enemy_name.grid(row=1, column=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

player_pokemon_name = tk.Label(root, text=chosen_pokemon["name"])
player_pokemon_name.grid(row=2, column=0)
player_pokemon_hp = tk.Label(root, text=f"HP: {chosen_pokemon['hp']}")
player_pokemon_hp.grid(row=3, column=0)


enemy_pokemon_name = tk.Label(root, text=enemy_pokemon["name"])
enemy_pokemon_name.grid(row=2, column=1)
enemy_pokemon_hp = tk.Label(root, text =f"HP: {enemy_pokemon["hp"]}")
enemy_pokemon_hp.grid(row= 3, column=1)

root.mainloop()