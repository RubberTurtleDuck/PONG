from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("chartreuse")
        self.penup()
        self.x_dir = 5
        self.y_dir = 5
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.speed("fastest")
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_dir *= -1

    def paddle_bounce(self):
        self.x_dir *= -1
        self.move_speed *= 0.75

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.05
