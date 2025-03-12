from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-0, 250)
        self.update_board()

    def update_board(self):
        self.write(f"Score : {self.score_number}", align="center", font=("Arial", 13, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.score_number += 1
        self.update_board()
