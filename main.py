import time
from turtle import Screen
from score_board import Score
from screen_game import PongScreen
from paddle import Paddle
from pong import Pong


screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


pong_screen = PongScreen()
paddle1 = Paddle(-580)
paddle2 = Paddle(580)
pong = Pong()
score_one = Score(-100)
score_two = Score(100)
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    pong.initial_move()
    if pong.ycor() > 260 or pong.ycor() < -260:
        screen.update()
        time.sleep(0.1)
        pong.recalc()
        pong.initial_move()

    if pong.xcor() > 590:
        screen.update()
        time.sleep(0.1)
        score_one.score_count()
        pong.create_pong()

    elif pong.xcor() < -590:
        screen.update()
        time.sleep(0.1)
        score_two.score_count()
        pong.create_pong()

    pong.pong_touch(paddle1, paddle2)

screen.exitonclick()
