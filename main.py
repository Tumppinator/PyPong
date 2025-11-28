from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
scoreboard = ScoreBoard()
r_paddle = Paddle(380)
l_paddle = Paddle(-390)
ball = Ball()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# Create middle line
middle_line = Turtle()
middle_line.color("white")
middle_line.penup()
middle_line.goto(0,295)
middle_line.setheading(270)
for i in range(16):
    middle_line.pendown()
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)

screen.listen()
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")
screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.check_wall_collision()
    ball.check_paddle_collision(l_paddle, r_paddle)
    ball.move()
    outcome = ball.check_out_of_bounds()
    if outcome == "right":
        scoreboard.point_right()
        ball.reset_position()
    elif outcome == "left":
        scoreboard.point_left()
        ball.reset_position()

    # Check win condition
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False

    r_paddle.move()
    l_paddle.move()


screen.exitonclick()