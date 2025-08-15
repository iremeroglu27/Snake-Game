from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from turtledemo.penrose import start

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("LightCyan1")
screen.title("My Snake Game")
screen.tracer(0)

# creates snake
snake = Snake()
screen.listen()
food = Food()
score = ScoreBoard()


# moves snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) # adds a delay in seconds

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    snake.move()

    # detect collision with food
    # create a scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collisions with wall
    if (snake.head.xcor()>290 or snake.head.xcor()< -290 or
        snake.head.ycor()>290 or snake.head.ycor()< -290):
        score.reset()
        snake.reset()

    # detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
           
screen.exitonclick()

