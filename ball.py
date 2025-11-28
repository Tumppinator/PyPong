from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0) # Animation speed
        # Initial change in X (dx) and Y (dy) per frame
        self.dx = 0.8
        self.dy = 0.8
        self.move_speed = 2

    def move(self):
        new_x = self.xcor() + self.dx * self.move_speed
        new_y = self.ycor() + self.dy * self.move_speed
        self.goto(new_x, new_y)

    def check_wall_collision(self):
        if self.ycor() > 290:
            self.sety(290) # Reset position to avoid sticking
            self.dy *= -1  # Reverse vertical direction
        elif self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

    def check_out_of_bounds(self):
        if self.xcor() > 395:
            return "right"
        elif self.xcor() < -395:
            return "left"
        return None


    def check_paddle_collision(self, paddle_a, paddle_b):
        # Collision with Paddle B (Right Paddle)
        if (self.xcor() > paddle_b.xcor() - 20 and self.xcor() < paddle_b.xcor()) and \
           (self.ycor() < paddle_b.ycor() + 50 and self.ycor() > paddle_b.ycor() - 50):

            # Force direction to be negative (Left)
            self.dx = -abs(self.dx)
            # Increase speed slightly on hit for difficulty
            self.move_speed *= 1.05
            # Collision with Paddle A (Left Paddle)
        elif (self.xcor() < paddle_a.xcor() + 20 and self.xcor() > paddle_a.xcor()) and \
                (self.ycor() < paddle_a.ycor() + 50 and self.ycor() > paddle_a.ycor() - 50):
            # Force direction to be positive (Right)
            self.dx = abs(self.dx)
            self.move_speed *= 1.05


    def reset_position(self):
        # Resets the ball to the center and reverses direction after a score
        self.goto(0, 0)
        self.dx *= -1
