import time
from turtle import Screen

from constant import WIDTH_SCREEN
from food import Food
from score import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=WIDTH_SCREEN, height=WIDTH_SCREEN)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_continue = True
while is_game_continue:
    screen.update()
    position_segment_snake = [seg.pos() for seg in snake.segment[1:]]
    if snake.head.pos() in position_segment_snake:
        is_game_continue = False
        score_board.game_end()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head) <= 10:
        food.refresh()
        snake.extend()
        score_board.increase()

screen.exitonclick()
