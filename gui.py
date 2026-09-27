import tkinter as tk

root = tk.Tk()

root.title("Pokemon Battle 1:1")
root.resizable(False, False)
root.minsize(900,600)
label = tk.Label(root, text="POKEMON BATTLE")
label.pack()

root.mainloop()