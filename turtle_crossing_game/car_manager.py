import turtle
import random

COLORS = ["orange", "red", "yellow", "blue", "brown", "cyan"]
CAR_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(turtle.Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_MOVE_DISTANCE

    def create_car(self):
        i = random.randint(1,5)
        if i == 2:
            car = turtle.Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            self.all_cars.append(car)

    def move_all_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



