import tkinter as tk
import pandas as pd
import random

# Load data and set up the words to learn
data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")  # Convert each row to a dictionary in a list
current_word = {}

def next_card():
    global current_word
    current_word = random.choice(to_learn)
    canvas_1.itemconfig(card_title, text="French", fill="black")
    canvas_1.itemconfig(card_words, text=current_word["French"], fill="black")
    canvas_1.itemconfig(canvas_image, image=bg_image_front)

def flip_flash_card():
    canvas_1.itemconfig(card_title, text="English", fill="white")
    canvas_1.itemconfig(card_words, text=current_word["English"], fill="white")
    canvas_1.itemconfig(canvas_image, image=bg_image_back)

BACKGROUND_COLOR = "#B1DDC6"

# Setup window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas_1 = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_image_front = tk.PhotoImage(file="images/card_front.png")
bg_image_back = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas_1.create_image(400, 263, image=bg_image_front)
card_title = canvas_1.create_text(400, 150, text="Title", font=("Arial", 35, "bold"))
card_words = canvas_1.create_text(400, 290, text="Description", font=("Arial", 55, "bold"))
canvas_1.grid(row=0, column=0, columnspan=2)

# Buttons setup
right_button_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_button_img, bg=BACKGROUND_COLOR, command=next_card, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_button_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_button_img, bg=BACKGROUND_COLOR, command=flip_flash_card, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.after(3000, flip_flash_card)

next_card()

window.mainloop()
