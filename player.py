from turtle import Turtle
HORIZONTAL_POSITION = -270
MOVE_LENGTH = 50
SCREENSIZE = (500, 600)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 4, 1)
        self.penup()
        self.go_to_start()

    def move_left(self):
        if self.xcor() > -225:
            new_x = self.xcor() - MOVE_LENGTH
            self.goto(new_x, HORIZONTAL_POSITION)

    def move_right(self):
        if self.xcor() < 225:
            new_x = self.xcor() + MOVE_LENGTH
            self.goto(new_x, HORIZONTAL_POSITION)

    def go_to_start(self):
        self.goto(x=0, y=HORIZONTAL_POSITION)