from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    time.sleep(0.09)
    screen.update()

    snake.move()

    # when the snake eat a fruit
    if snake.snake_begin[0].distance(food) < 13:
        food.refresh()
        snake.eat()
        score.increace()

    # when the snake hits wall
    if snake.snake_begin[0].xcor() > 290 or snake.snake_begin[0].xcor() < -290 or snake.snake_begin[0].ycor() > 290 or \
            snake.snake_begin[0].ycor() < -290:
        game_on = False
        score.game_over()

    #when the snake hits himself (head [0] hits the body [1 to len()]
    for i in range(1,len(snake.snake_begin)-1):
        if snake.snake_begin[0] == snake.snake_begin[i]:
            pass
        elif snake.snake_begin[0].distance(snake.snake_begin[i]) < 13:
            game_on = False
            score.game_over()

screen.exitonclick()
