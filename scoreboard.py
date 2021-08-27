from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.score = 0
        self.write(f"Score: {self.score}",align="center",font=("Arial" ,18 , "bold"))


    def increace(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER ! :( ", align="center", font=("Arial", 24, "normal"))