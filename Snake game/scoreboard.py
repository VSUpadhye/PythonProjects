from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x= 0, y= 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()