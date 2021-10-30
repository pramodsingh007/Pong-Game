from time import sleep
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xa = 10
        self.yb= 10
        self.move()
    def move(self):
        x = self.xcor() + self.xa
        y = self.ycor() + self.yb
        self.goto(x,y)

    def bounce_y(self):
        self.yb*=-1

    def bounce_x(self):
        self.xa *=-1
   
    def relocate(self):
        self.goto(0,0)
        self.bounce_x()
         