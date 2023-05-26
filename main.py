from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time

LEFT_POSITIONS = (-580, 0)


RIGHT_POSITIONS = (580, 0)

Y_UPPER_LIMIT = 340
Y_LOWER_LIMIT = -340

scr = Screen()
scr.setup(width=1200, height=800)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)
scr.listen()

paddle_l = Paddle(LEFT_POSITIONS)
paddle_r = Paddle(RIGHT_POSITIONS)
ball = Ball()
score_board = Score_board()

scr.onkey(paddle_l.up, "w")
scr.onkey(paddle_l.down, "s")
scr.onkey(paddle_r.up, "Up")
scr.onkey(paddle_r.down, "Down")

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(ball.move_speed)

    if ball.ycor() > Y_UPPER_LIMIT or ball.ycor() < Y_LOWER_LIMIT:
        ball.bounce()

    if (ball.distance(paddle_l) < 50 and ball.xcor() == -570) or (
        ball.distance(paddle_r) < 50 and ball.xcor() == 570
    ):
        ball.reverse()

    if ball.xcor() == -590 and ball.distance(paddle_l) > 30:
        ball.restart()
        score_board.increase_r_score()

    if ball.xcor() == 590 and ball.distance(paddle_r) > 30:
        ball.restart()
        score_board.increase_l_score()

    ball.move()

scr.exitonclick()
