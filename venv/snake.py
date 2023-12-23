from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment= Turtle()
            new_segment.shape("square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        self.segments[0].forward(MOVE_DISTANCE)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num-1].xcor()
            y_pos = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        new_segment = Turtle()
        new_segment.color("black")
        new_segment.shape("square")
        new_segment.penup()
        self.segments.append(new_segment)
        return new_segment
    
    def detect_collision(self):
        for segment in self.segments:
            if segment == self.head:
                pass
            elif self.head.distance(segment) < 15:
                return True
            return False