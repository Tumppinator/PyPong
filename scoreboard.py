from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 22, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-20, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(20, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def point_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def point_right(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=("arial", 32, "normal"))