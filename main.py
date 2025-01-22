from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title('Snake Game')


screen.tracer(0)

snake = Snake()
print(snake.snake_parts)

food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

#
wall_not_touched = True
while wall_not_touched:
    screen.update()
    time.sleep(0.1)
    # previousLocation = (0,0);
    if abs(snake.head.ycor()) >= HEIGHT/2  or abs(snake.head.xcor()) >= WIDTH/2:
        wall_not_touched = False
        scoreboard.game_over()

    snake.move()

    if snake.head.distance(food)<15:

        food.refresh()
        scoreboard.changing_score()
        snake.extend()
screen.exitonclick()