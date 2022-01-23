import time
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong - Sinclair")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.max_score = int(screen.textinput("Pong - Sinclair",
                                            "Welcome to Pong!\n\nControls:\nLeft paddle (W/S)\nRight paddle (⬆/⬇)\n\n"
                                            "How many points you want to play?"))

paddle_l = Paddles((-350, 0))
paddle_r = Paddles((350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.mov_speed)

    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 325 or ball.distance(paddle_l) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        ball.mov_speed *= 0.9
    # if pedal misses ball
    if ball.xcor() > 380 or ball.xcor() < -380:
        if scoreboard.add_score(ball.xcor()) == "end":
            game_over = True
        ball.out()
        ball.mov_speed = 0.1

screen.exitonclick()
