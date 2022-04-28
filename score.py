from turtle import Turtle

from constant import WIDTH_SCREEN, DISTANCE_PER_STEP

POSITION_SCORE = WIDTH_SCREEN / 2 - DISTANCE_PER_STEP


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, POSITION_SCORE)
        self.refresh()

    def refresh(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 14, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_end(self):
        self.home()
        self.write("GAME OVER!", align="center", font=('Arial', 20, 'normal'))
