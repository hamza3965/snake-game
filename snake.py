import random
from turtle import Turtle
from turtledemo.paint import changecolor

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

COLORS = ["blue", "green", "yellow", "purple", "cyan", "orange", "white"]

class Snake:

    def __init__(self):
        self.segments = []
        self.current_color = "white"
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color(self.current_color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def change_color(self):
        """Change the snake's color randomly"""
        self.current_color = random.choice(COLORS)
        for segment in self.segments:
            segment.color(self.current_color)

    def red_snake(self):
        self.current_color = "red"
        for segment in self.segments:
            segment.color(self.current_color)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
