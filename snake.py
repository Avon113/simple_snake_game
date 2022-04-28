from turtle import Turtle

from constant import POSITION_START, DISTANCE_PER_STEP, DIRECTION, WIDTH_SCREEN

HALF_SCREEN = WIDTH_SCREEN / 2 - DISTANCE_PER_STEP


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.head.shape('classic')

    def create_snake(self):
        for seg in POSITION_START:
            self.add(seg)

    def add(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("slowest")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add(self.segment[-1].position())

    def move(self):
        for seg_index in range(len(self.segment) - 1, 0, -1):
            new_xcor = self.segment[seg_index - 1].xcor()
            new_ycor = self.segment[seg_index - 1].ycor()
            self.segment[seg_index].goto(new_xcor, new_ycor)

        self.segment[0].forward(DISTANCE_PER_STEP)

        if self.head.xcor() > HALF_SCREEN:
            self.head.setx(-HALF_SCREEN)
        elif self.head.xcor() < -HALF_SCREEN:
            self.head.setx(HALF_SCREEN)
        elif self.head.ycor() > HALF_SCREEN:
            self.head.sety(-HALF_SCREEN)
        elif self.head.ycor() < -HALF_SCREEN:
            self.head.sety(HALF_SCREEN)

    def up(self):
        if self.head.heading() == DIRECTION['UP']:
            self.move()
        elif self.head.heading() != DIRECTION['DOWN']:
            self.head.seth(DIRECTION['UP'])

    def down(self):
        if self.head.heading() == DIRECTION['DOWN']:
            self.move()
        elif self.head.heading() != DIRECTION['UP']:
            self.head.seth(DIRECTION['DOWN'])

    def left(self):
        if self.head.heading() == DIRECTION['LEFT']:
            self.move()
        elif self.head.heading() != DIRECTION['RIGHT']:
            self.head.seth(DIRECTION['LEFT'])

    def right(self):
        if self.head.heading() == DIRECTION['RIGHT']:
            self.move()
        elif self.head.heading() != DIRECTION['LEFT']:
            self.head.seth(DIRECTION['RIGHT'])
