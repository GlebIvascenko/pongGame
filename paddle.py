
from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + SPEED
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - SPEED
        self.goto(x=self.xcor(), y=new_y)
