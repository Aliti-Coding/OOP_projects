from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POSITION = (+280, 0)



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_lst = []
        self.level = 14
        self.hideturtle()
        
    def create_car(self):

        random_create = random.randint(1,self.level)
        if random_create == 2:
                
            self.cars = Turtle()
            self.cars.shape("square")
            self.cars.color(random.choice(COLORS))
            self.cars.penup()
            self.cars.shapesize(1,2)
            random_y = random.randrange(-250, 280)
            self.cars.goto(280,random_y)
            self.cars_lst.append(self.cars)
            
    def move(self):
        
        for car in self.cars_lst:
            car.backward(STARTING_MOVE_DISTANCE)
        
    def increase_difficulty(self):
        self.level -= 6

