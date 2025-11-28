from turtle import Turtle

PADDLE_SPEED = 2.8


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x_position, 0)
        self.direction_is_up = True
        self.direction = -1
        self.paddle_dy = 0
        self.boundary_limit = 250


    def start_up(self):
        self.paddle_dy = PADDLE_SPEED

    def start_down(self):
        self.paddle_dy = -PADDLE_SPEED

    def stop_up(self):
        if self.paddle_dy > 0:
            self.paddle_dy = 0

    def stop_down(self):
        if self.paddle_dy < 0:
            self.paddle_dy = 0

    def move(self):
        if self.paddle_dy != 0:
            new_y = self.ycor() + self.paddle_dy

            if new_y < self.boundary_limit and new_y > -self.boundary_limit:
                self.sety(new_y)


