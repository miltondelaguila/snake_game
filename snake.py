from turtle import Turtle

HEIGHT = 600
WIDTH = 600
MOVE_DISTANCE = 20
START_POSITION = (0,0)

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(START_POSITION)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        position = (position[0] - 20, position[1])
        self.snake_parts.append(snake)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for i in range(len(self.snake_parts)):
            # time.sleep(1)
            # print(self.snake_parts[i].ycor())
            # print(self.snake_parts[i].xcor())


            if i == 0:
                previous_place = self.snake_parts[i].position()
                self.snake_parts[i].forward(MOVE_DISTANCE)
            else:
                previous_place_tail = self.snake_parts[i].position()
                self.snake_parts[i].goto(previous_place)
                previous_place = previous_place_tail

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)