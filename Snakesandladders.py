import tkinter as tk
from tkinter import messagebox
import random

ladders = {3: 24, 14: 42, 30: 86, 37: 57, 50: 96, 66: 74}
snakes = {95: 18, 77: 45, 60: 28, 34: 10, 20: 2}
TILE_SIZE = 60
BOARD_SIZE = TILE_SIZE * 10
class SnakesAndLaddersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snakes and Ladders")
        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()
        self.draw_board()
        self.player_positions = [1, 1]
        self.tokens = [
            self.canvas.create_oval(5, 545, 25, 565, fill="blue"), 
            self.canvas.create_oval(30, 545, 50, 565, fill="red")   
        ]
        self.current_player = 0
        self.players = ["Player 1", "Player 2"]
        self.label = tk.Label(root, text="Player 1's Turn", font=("Arial", 14))
        self.label.pack()
        self.dice_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.dice_button.pack(pady=10)
        self.dice_label = tk.Label(root, text="Dice: -", font=("Arial", 12))
        self.dice_label.pack()
    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                index = row * 10 + col if row % 2 == 0 else row * 10 + (9 - col)
                self.canvas.create_text(x1 + 30, y1 + 30, text=str(100 - index))
    def get_coordinates(self, position):
        pos = position - 1
        row = pos // 10
        col = pos % 10
        if row % 2 == 1:
            col = 9 - col
        x = col * TILE_SIZE + TILE_SIZE // 2
        y = (9 - row) * TILE_SIZE + TILE_SIZE // 2
        return x, y
    def roll_dice(self):
        dice = random.randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice}")
        player = self.current_player
        position = self.player_positions[player] + dice
        if position > 100:
            self.switch_turn()
            return
        if position in ladders:
            position = ladders[position]
        elif position in snakes:
            position = snakes[position]
        self.player_positions[player] = position
        x, y = self.get_coordinates(position)
        offset = -10 if player == 0 else 10
        self.canvas.coords(self.tokens[player], x - 10 + offset, y - 10, x + 10 + offset, y + 10)
        if position == 100:
            messagebox.showinfo("Game Over", f"{self.players[player]} wins!")
            self.dice_button.config(state="disabled")
            return
        self.switch_turn()
    def switch_turn(self):
        self.current_player = 1 - self.current_player
        self.label.config(text=f"{self.players[self.current_player]}'s Turn")
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakesAndLaddersGame(root)
    root.mainloop()
