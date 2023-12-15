from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("yellow")
        self.penup()
        self.goto(xcor, ycor)
        
    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)

