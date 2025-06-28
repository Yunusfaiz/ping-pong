from turtle import *
import random

# screen setup
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')

# Score variables
score_a = 0
score_b = 0


# paddle movement
def paddleR_up():
    paddle_right.forward(20)

def paddleR_down():
    paddle_right.back(20)


def paddleL_up():
    paddle_left.forward(20)

def paddleL_down():
    paddle_left.back(20)


# paddle setup
paddle_right = Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(1, 4)
paddle_right.color('white')
paddle_right.penup()
paddle_right.setheading(90)
paddle_right.goto(370, 0)

paddle_left = Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(1, 4)
paddle_left.color('white')
paddle_left.penup()
paddle_left.setheading(90)
paddle_left.goto(-370, 0)

# Ball creation
ball = Turtle()
ball.speed(0)
ball.color('blue')
ball.shape('circle')
ball.goto(0,0)
ball.penup()
ball.dx = 2
ball.dy = 2

# Scoreboard for A and B
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0  0", align="center", font=("Courier", 24, "normal"))

# Listen for keys
screen.listen()
screen.onkey(paddleR_up, 'Up')
screen.onkey(paddleR_down, 'Down')
screen.onkey(paddleL_up, 'w')
screen.onkey(paddleL_down, 's')

# Border Dimensions
border_top = 350
border_bottom = -350
border_left = -390
border_right = 390

# Update scoreboard
def update_score():
    pen.clear()
    pen.write(f"{score_a}  {score_b}", align="center", font=("Courier", 24, "normal"))


while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball border collision
    if ball.ycor() > border_top:
        ball.sety(border_top)
        ball.dy *= -1

    if ball.ycor() < border_bottom:
        ball.sety(border_bottom)
        ball.dy *= -1

    if ball.xcor() > border_right:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < border_left:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Ball and paddle collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

screen.mainloop()
