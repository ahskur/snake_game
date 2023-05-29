from turtle import *

# Tuples to set starting position of the 3 initial segments of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    # Attributes from the Snake
    def __init__(self):
        # Create an empty segment list, so we can always append new segments to it and keep track of the amount
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Methods the snake has
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        # To move the snake all at the same time - We set the first block to move and then the other blocks just
        # go to the old position of the block in front of them. So block 3 goes to position of block 2 and block 2 then
        # goes to where block 1 was - Always following the steps of block 1
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # With -1 we get always the last segment
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        # Clear list of segments
        self.segments.clear()
        # and then create a new fresh snake
        self.create_snake()
        self.head = self.segments[0]


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

