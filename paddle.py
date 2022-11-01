from turtle import Turtle
MOVING_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("chartreuse")
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        self.setpos(position)

    def up(self):
        self.speed("fastest")
        self.forward(MOVING_DISTANCE)

    def down(self):
        self.speed("fastest")
        self.back(MOVING_DISTANCE)


