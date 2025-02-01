from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import pygame

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Draw Upper Wall
border = Turtle()
border.color("white")
border.penup()
border.goto(-300, 292)
border.pendown()
border.pensize(3)
border.forward(600)
border.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

pygame.mixer.init()
# Load sound effects
food_sound = pygame.mixer.Sound("./sound_effects/food_eat.wav")
game_over_sound = pygame.mixer.Sound("./sound_effects/game_over.wav")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        food_sound.play()

        if scoreboard.score % 2 == 0:
            snake.change_color()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.color("red")
        scoreboard.game_over()
        game_over_sound.play()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            snake.red_snake()
            scoreboard.game_over()
            screen.update()
            game_over_sound.play()



screen.exitonclick()
