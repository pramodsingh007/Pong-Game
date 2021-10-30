from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


from pong_score import Scoreboard




on = Screen()
on.bgcolor("black")
on.setup(800,600)
on.tracer(0)
p1 = Paddle((-350,0))
p2 = Paddle((350,0))
b = Ball()
on.title("The Pong Game by Pramod")







on.listen()
on.onkeypress(p1.up,"w")
on.onkeypress(p1.down,"s")
on.onkeypress(p2.up,"Up")
on.onkeypress(p2.down,"Down")


game_on = True
turn_count = 0
score = Scoreboard()
while game_on:
    score.refresh()
    score.check_score()
    

    
      

    if b.ycor() > 280 or b.ycor() < -280:  #ditecting collision with the uper and lower wall 
        b.bounce_y()
    if b.distance(p1) < 40 and b.xcor() > -340 :    # ditecting collision with both of the paddles in the game
        b.bounce_x()
    if b.distance(p2) < 40 and b.xcor() > -340:

        b.bounce_x()
    on.update()
    time.sleep(0.02)  
    b.move()
    
    if b.xcor() > 395 or b.xcor() < -395: # this line of code will track if paddle missed the ball
        turn_count+=1
        if b.xcor() > 395:
            score.p1score()
        if b.xcor() < -395:
            score.p2score()
        b.relocate()
        time.sleep(1)
    if turn_count > 10:
        game_on = False
        score.gameover()

























on.exitonclick()