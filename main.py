from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
game_over = False

right_paddle = Paddle((480, 0))
left_paddle = Paddle((-480, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 460 or ball.distance(left_paddle) < 50 and ball.xcor() < -460:
        ball.paddle_bounce()

    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
