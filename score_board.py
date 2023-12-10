from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'bold')


class Score(Turtle):
    def __init__(self, xposition):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(xposition, 220)
        self.score = 0
        self.general_score()

    def general_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.general_score()
