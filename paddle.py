from turtle import Turtle


UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def up(self):
        if self.ycor() < 390:
            current_y = self.ycor()
            current_x = self.xcor()
            self.goto(current_x, current_y + 20)

    def down(self):
        if self.ycor() > -380:
            current_y = self.ycor()
            current_x = self.xcor()
            self.goto(current_x, current_y - 20)
