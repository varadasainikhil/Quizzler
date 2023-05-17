from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"
font = ("Arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=450)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_text = Label(text=f"Score : {self.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        self.question = "Hello,This is the 1st question"
        self.question_box = Canvas(height=250, width=300, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.question_box.create_text(150, 125, text=self.question, font=font, width=180)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)
        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, border=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)

        else:
            self.question_box.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        is_right = (self.quiz.check_answer("True"))
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = (self.quiz.check_answer("False"))
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_box.config(bg="green")
            self.score += 1
            self.score_text.config(text=f"Score : {self.score}")
        else:
            self.question_box.config(bg="red")
        self.window.after(1000, self.get_next_question)

