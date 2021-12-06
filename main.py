from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def again():
    Screen().clear()
    game()

def game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game By YS")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(again, "space")
    screen.onkey(snake.exit, "Escape")

    game_continue = True
    while game_continue:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.new_score()
            snake.snake_length()

        # Detect collision with wall.
        if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
            game_continue = False
            scoreboard.game_over()
            scoreboard.highest_score()

        # if head collides with any segment in the tail --> game over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_continue = False
                scoreboard.game_over()
                scoreboard.highest_score()


    screen.exitonclick()

game()