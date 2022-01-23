from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.max_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Verdana", 20, "bold"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Verdana", 20, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Verdana", 20, "bold"))

    def add_score(self, pos):
        if pos == 390:
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Verdana", 20, "bold"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Verdana", 20, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Verdana", 20, "bold"))
        if self.l_score == self.max_score or self.r_score == self.max_score:
            self.goto(0, 0)
            self.write("GAME OVER!", align="center", font=("Verdana", 20, "bold"))
            return "end"
