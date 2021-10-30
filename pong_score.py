
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.p1_score = 0
        self.p2_score = 0
        self.check_score()
        
    def check_score(self):
        self.write(arg= f"{self.p1_score}   {self.p2_score}",align="center",font=("Courier",30,"normal"))
    
    def refresh(self):
        self.clear()

    def p1score(self):
        self.p1_score+=1

    def p2score(self):
        self.p2_score+=1

    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over",align ="center",font=("Courier",80,"bold"))