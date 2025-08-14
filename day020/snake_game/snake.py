from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    starting_position = [(0,0),(-20,0),(-40,0)]
    segments = []
    position = 0

    def __init__(self):
        for position in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.starting_position[position])
            self.segments.append(new_segment)
        self.head = self.segments[0]


    def addSegment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(self.segments[len(self.segments) - 1].position())
        new_segment.color("white")
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1 ,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)


    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)
