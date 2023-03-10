from turtle import Turtle
FONT = ("Courier", 22, "normal")



class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.score = 1
        # self.increase_level()

    def text_level(self):
        self.write(f"LEVEL {self.score}",align='left',font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",align='center',font=FONT)
        
        
    def increase_level(self):
        self.score += 1
        self.clear()
        self.text_level()

    