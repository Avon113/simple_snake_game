import random
from turtle import Turtle

from constant import WIDTH_SCREEN, SIZE


class Food(Turtle):

    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        total_section = int(WIDTH_SCREEN / (2 * SIZE) - 1)
        rand_x = random.randint(total_section * -1, total_section) * SIZE
        rand_y = random.randint(total_section * -1, total_section) * SIZE
        print((rand_x, rand_y))
        self.goto(rand_x, rand_y)
