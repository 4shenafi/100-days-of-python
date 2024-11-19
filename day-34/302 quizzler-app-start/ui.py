import tkinter as tk
from data import question

THEME_COLOR = "#375362"

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        # Initialize score and question index
        self.score = 0
        self.i = 0

        # Score Label
        self.score_label = tk.Label(text=f"Score: {self.score}", font=("Helvetica", 16, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=10)

        # Canvas for Question
        self.canvas = tk.Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Welcome to Quizzler!",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Buttons
        self.right_image = tk.PhotoImage(file="images/true.png")
        self.false_image = tk.PhotoImage(file="images/false.png")
        self.right_button = tk.Button(image=self.right_image, command=self.check_true)
        self.right_button.grid(row=2, column=0, pady=20)
        self.false_button = tk.Button(image=self.false_image, command=self.check_false)
        self.false_button.grid(row=2, column=1, pady=20)

        # Load First Question
        self.load_question()

    def load_question(self):
        try:
            q_text, _ = question(self.i)  # Get question and correct answer
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            self.end_game()

    def check_true(self):
        self.check_answer("True")

    def check_false(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        _, correct_answer = question(self.i)  # Get correct answer
        if user_answer == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.i += 1
        self.load_question()

    def end_game(self):
        self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
        self.right_button.config(state="disabled")
        self.false_button.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
