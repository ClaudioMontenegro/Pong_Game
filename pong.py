from turtle import Turtle
import random
from turtle import Screen

HEADING = [40, 130, 210, 310]
screen = Screen()
TOUCH = 20


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.create_pong()
        self.move_speed = 10

    def initial_move(self):
        self.forward(self.move_speed)

    def create_pong(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.move_speed = 10
        self.penup()
        self.goto(0, 0)
        self.setheading(random.choice(HEADING))

    def recalc(self):
        new_rout = self.heading() * -1
        self.setheading(new_rout)

    def paddle_touch(self):
        new_rout = self.heading() + 180
        self.setheading(new_rout)
        self.initial_move()

    def pong_touch(self, paddle1, paddle2):
        for paddle in range(0, len(paddle1.paddles)):
            if self.distance(paddle1.paddles[paddle]) < TOUCH or self.distance(paddle2.paddles[paddle]) < TOUCH:
                self.paddle_touch()
                if self.move_speed <= 100:
                    self.move_speed += (self.move_speed * 0.2)

