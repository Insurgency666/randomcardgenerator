import tkinter as tk
import random

def draw(event=None):
    cards = ["🂡", "🂢", "🂣", "🂤", "🂥", "🂾"]
    card_label.config(text=random.choice(cards))

root = tk.Tk()
root.title("Random Card Generator")
root.geometry("400x350")
root.configure(bg="#353839")

card_label = tk.Label(root, text="🃏", font=("Arial", 60))
card_label.pack(pady=30)

deal_btn = tk.Button(root, text="Deal!")
deal_btn.bind("<Button-1>", draw)

command=draw
deal_btn.pack()

root.mainloop()
