from turtle import Turtle
FINISH_LINE = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto_start()

    def move_up(self):
        self.forward(10)

    def is_at_finsh_line(self):
        if self.ycor() >= 280:
            return True
        return False

    def goto_start(self):
        self.goto(0, -280)