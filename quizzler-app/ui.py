from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        ##Background Canvas -- My solution to padding problem, before i realized i can use pady in grid setup
        # self.canvas = Canvas(width=300, height=500, bg=THEME_COLOR,highlightthickness=0,borderwidth=0)
        # self.canvas.grid(row=0, column=0, columnspan=2, rowspan=3)
        ##Score Label
        self.score_label = Label(text=f'Score: {0}',fg='white', bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0,)
        ## White Question Box
        self.question_box = Canvas(width=300, height=250, bg='white',highlightthickness=0,borderwidth=0)
        self.question_box.grid(row=1, column=0, columnspan=2,pady=20,)
        ##Question Text
        self.question_text = self.question_box.create_text(150, 125, text="Questions go here.", width=275, font=("Arial", 20, "italic"),fill=THEME_COLOR)
        ##True Button
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=1)
        ##False Button
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        #loop

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg='white')
        try:
            question_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=question_text)
        except IndexError:
            self.question_box.itemconfig(self.question_text, text=f"Quiz Complete:\n\nYou Scored {self.quiz.score}/10!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        self.feedback(self.quiz.check_answer('true'))
        self.get_next_question()
    def false_pressed(self):
        self.feedback(self.quiz.check_answer('false'))
        self.get_next_question()
    def feedback(self, is_right):
        self.score_label.config(text=f'Score: {self.quiz.score}',fg='white', bg=THEME_COLOR, font=("Arial", 10, "bold"))
        if is_right:
            self.question_box.config(bg='green')
            self.question_box.update()
            self.window.after(1000,)
        if not is_right:
            self.question_box.config(bg='red')
            self.question_box.update()
            self.window.after(1000, )