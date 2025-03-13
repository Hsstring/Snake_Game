import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

score = Scoreboard()

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with the top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    # Detect collision with r_paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_horizontal()

    # Detect when the right paddle misses
    elif ball.xcor() > 370:
        ball.reset_position()
        time.sleep(0.1)
        score.l_point()
    # Detect when the left paddle misses
    elif ball.xcor() < -370:
        ball.reset_position()
        time.sleep(0.1)
        score.r_point()
screen.exitonclick()
