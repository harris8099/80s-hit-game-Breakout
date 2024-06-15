# 80s hit game Breakout
from turtle import Screen
from player import Player
from blocks import Block
from ball import Ball
import time

# Todo: make ball move in random direction when game starts

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.title("Breakout")
screen.colormode(255)

player = Player()
blocks = Block()
ball = Ball()

screen.listen()
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
blocks.create_blocks()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.tracer(1)
    # screen.update()
    ball.move()
    # if len(blocks.all_blocks) == 0 and blocks.LEVEL == 3:
    #     screen.reset()
    if len(blocks.all_blocks) == 0 and 0 <= blocks.LEVEL <= 3:
        print("NEXT LEVEL")
        blocks.LEVEL += 1
        ball.reset_position()
        # blocks.all_blocks = []
        blocks.create_blocks()
    if ball.xcor() > 250 or ball.xcor() < -250:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.ycor() < -290:
        blocks.LEVEL = 1
        ball.reset_position()
        for i in blocks.all_blocks:
            i.color("white")
        # blocks.all_blocks = []
        blocks.create_blocks()

    if ball.distance(player) <= 35 and ball.switch:
        ball.bounce_y()
        ball.switch = False
    if ball.ycor() > -180:
        ball.switch = True
    for i in blocks.all_blocks:
        if ball.distance(i) < 20:
            i.color("white")
            blocks.all_blocks.remove(i)
            ball.bounce_y()

screen.exitonclick()
