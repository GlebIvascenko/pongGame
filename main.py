from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

player_r = Paddle((350, 0))
player_l = Paddle((-350, 0))
ball = Ball()
score = Score()

line = Turtle()
line.penup()
line.color("white")
line.goto(0, 300)
line.pendown()
line.goto(0, -300)



screen.listen()
screen.onkey(player_r.move_up, "Up")
screen.onkey(player_r.move_down, "Down")
screen.onkey(player_l.move_up, "w")
screen.onkey(player_l.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(player_r) < 50 and ball.xcor() > 320 or ball.distance(player_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when paddle goes out of bounds
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()