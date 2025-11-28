from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball


import time

screen = Screen()
scoreboard = ScoreBoard()
paddle_right = Paddle(380)
paddle_left = Paddle(-390)
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
screen.onkeypress(paddle_right.start_up, "Up")
screen.onkeyrelease(paddle_right.stop_up, "Up")
screen.onkeypress(paddle_right.start_down, "Down")
screen.onkeyrelease(paddle_right.stop_down, "Down")
screen.onkeypress(paddle_left.start_up, "w")
screen.onkeyrelease(paddle_left.stop_up, "w")
screen.onkeypress(paddle_left.start_down, "s")
screen.onkeyrelease(paddle_left.stop_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.check_wall_collision()
    ball.check_paddle_collision(paddle_left, paddle_right)
    ball.move()
    if ball.xcor() > 395:
        scoreboard.point_right()
        ball.goto(0,0)
    elif ball.xcor() < -395:
        scoreboard.point_left()
        ball.goto(0,0)

    # Check win condition
    if scoreboard.left_player_score == 10 or scoreboard.right_player_score == 10:
        scoreboard.game_over()
        game_is_on = False

    paddle_right.move()
    paddle_left.move()






screen.exitonclick()