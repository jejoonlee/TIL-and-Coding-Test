from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def add_snake(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.body.append(snake_body)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def extend(self):
        position = (self.body[-1].xcor(), self.body[-1].ycor())
        self.add_snake(position)

    # 제일 뒤에서 부터, 앞에까지 박스들이 모인다
    # 이렇게 하면, 앞에 머리 부분에서 특정한 곳으로 움직이면, 뒤에서 쫓아오게 된다
    def move(self):
        for snake_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[snake_num - 1].xcor()
            new_y = self.body[snake_num - 1].ycor()
            self.body[snake_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # 다시 방향을 돌아갈 수 없도록 if문으로 만든다
    # 예) 위를 보고 있으면 DOWN 방향을 못 가게 만든다
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
