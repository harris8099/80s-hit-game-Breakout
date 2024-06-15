from turtle import Turtle
import random


class Block:
    def __init__(self):
        self.LEVEL = 1
        self.all_blocks = []

    def random_color(self):
        r = random.randint(1, 255)
        g = random.randint(0, 250)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def create_blocks(self):
        self.all_blocks = []
        x = -225
        y = 270
        for i in range(0, 10*self.LEVEL):
            new_block = Turtle("square")
            new_block.shapesize(stretch_wid=1, stretch_len=2)
            new_block.penup()
            new_block.color("white")
            if i % 10 == 0:
                x = -225
                y -= 20
            x += 40
            # new_block.setposition(x, y)
            new_block.speed(10)
            new_block.goto(x, y)
            new_block.color(self.random_color())
            self.all_blocks.append(new_block)
