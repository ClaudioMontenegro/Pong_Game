from turtle import Turtle, Screen
import time

Y_AXIS = list(range(-40, 80, 20))
X = -580
UP = 90
DOWN = 270
MOVE = 50
screen = Screen()


class Paddle:
    def __init__(self, x_axis):
        self.paddles = []
        self.make_paddle()
        self.set_paddle(x_axis)
        self.head = self.paddles[0]

    def make_paddle(self):
        for posy in range(len(Y_AXIS)):
            self.paddle = Turtle("square")
            self.paddle.color("white")
            self.paddle.shapesize(1)
            self.paddle.penup()
            self.paddles.append(self.paddle)

    def move(self):
        for pad in range(len(self.paddles)):
            self.paddles[pad].forward(MOVE)

    def heading(self, set):
        for pad in range(len(self.paddles)):
            self.paddles[pad].setheading(set)

    def up(self):
        self.heading(UP)
        self.move()

    def down(self):
        self.heading(DOWN)
        self.move()

    def set_paddle(self, x_axis):
        for posy in range(len(Y_AXIS)):
            self.paddles[posy].goto(x_axis, Y_AXIS[posy])

    def move_alone(self):
        if self.paddles[0].ycor() > -230:
            screen.update()
            time.sleep(0.2)
            self.down()
        else:
            while self.paddles[-1].ycor() < 230:
                screen.update()
                time.sleep(0.2)
                self.up()
