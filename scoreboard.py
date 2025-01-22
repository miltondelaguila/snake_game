from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 270

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.changing_score()

    def changing_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="center", font=('Courier', 18, 'bold'))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=('Courier', 18, 'bold'))

