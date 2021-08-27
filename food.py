from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.x = random.randint(-290,290)
        self.y = random.randint(-290,290)
        self.goto(self.x,self.y)

    def refresh(self):
        self.x = random.randint(-270,270)
        self.y = random.randint(-270,270)
        self.setx(self.x)
        self.sety(self.y)