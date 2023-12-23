from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()

    if (snake.head.xcor() > 290):
        snake.head.goto(-290, snake.head.ycor())
    if (snake.head.xcor() < -290):
        snake.head.goto(290, snake.head.ycor())
    if (snake.head.ycor() > 290):
        snake.head.goto(snake.head.xcor(), -290)
    if (snake.head.ycor() < -290):
        snake.head.goto(snake.head.xcor(), 290)

    snake.detect_collision()    
    if snake.detect_collision() == True:
        game_is_on = False
        snake.goto(0, 0)
        score.write(f"Game Over!!!", False, align="center", font=("Arial", 12, "normal"))





screen.exitonclick()