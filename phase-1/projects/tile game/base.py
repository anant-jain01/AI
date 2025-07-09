import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("8 TILE GAME")

# Define and shuffle tiles
flat = [1, 2, 3, 4, 5, 6, 7, 8, None]
random.shuffle(flat)
tiles = [flat[i*3:(i+1)*3] for i in range(3)]

# Prepare button grid
buttons = [[None for _ in range(3)] for _ in range(3)]

def draw_board():
    for i in range(3):
        for j in range(3):
            value = tiles[i][j]
            text = str(value) if value is not None else ""
            btn = tk.Button(root, text=text, width=6, height=3, font=("Arial", 24))
            btn.grid(row=i, column=j)
            buttons[i][j] = btn

draw_board()

root.mainloop()
