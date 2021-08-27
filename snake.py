
from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_begin = []
        x_ = 0
        for i in range(3):
            self.snake_begin.append(Turtle(shape="square"))
            self.snake_begin[i].penup()
            self.snake_begin[i].speed("fastest")
            self.snake_begin[i].color("white")
            self.snake_begin[i].setx(x_)
            x_ -= 20

    def move(self):
        for dot in range(len(self.snake_begin)-1, 0, -1):
            new_x =self.snake_begin[dot-1].xcor()
            new_y =self.snake_begin[dot-1].ycor()
            self.snake_begin[dot].goto(new_x, new_y)
        self.snake_begin[0].forward(MOVE_DIST)

    def up(self):
        if self.snake_begin[0].heading()!=DOWN:
            self.snake_begin[0].setheading(UP)

    def down(self):
        if self.snake_begin[0].heading() != UP:
            self.snake_begin[0].setheading(DOWN)

    def left(self):
        if self.snake_begin[0].heading() != RIGHT:
            self.snake_begin[0].setheading(LEFT)

    def right(self):
        if self.snake_begin[0].heading() != LEFT:
            self.snake_begin[0].setheading(RIGHT)


    def eat(self):
        #add 1 to tail after eating
        self.snake_begin.append(Turtle(shape="square"))
        self.snake_begin[-1].penup()
        self.snake_begin[-1].speed("fast")
        self.snake_begin[-1].color("white")
        self.snake_begin[-1].setx(self.snake_begin[-2].xcor() -20)
