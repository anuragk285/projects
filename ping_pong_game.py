from turtle import Turtle, Screen
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__("square")
        self.penup()
        self.fillcolor("white")
        self.goto(xcor, ycor)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.fillcolor("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    # resetting ball if ball gone out
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.update_scores()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update_scores()


screen.exitonclick()