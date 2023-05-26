from turtle import Turtle


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 350)
        self.write(
            f"Player 1: {self.score_l} | Player 2: {self.score_r}",
            align="center",
            font=("Arial", 24, "normal"),
        )
        self.write_score()

    def write_score(self):
        self.write(
            f"Player 1: {self.score_l} | Player 2: {self.score_r}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def increase_l_score(self):
        self.score_l += 1
        self.clear()
        self.write_score()

    def increase_r_score(self):
        self.score_r += 1
        self.clear()
        self.write_score()
