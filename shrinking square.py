import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('black')
drawing_board.title('Shrinking square test')




turtle_ins = turtle.Turtle()
turtle_ins.color('red')
turtle_ins.pensize(1)
turtle_ins.shape("square")
turtle_ins.setposition(0, 0)
turtle_ins.setheading(0)
turtle_ins.shapesize(1)
turtle_ins.speed(1000)

turtle_sat = turtle.Turtle()
turtle_sat.speed(1000)

size = 30
for i in range(size * 4):
    turtle_ins.forward(i*4)
    turtle_ins.right(91)

turtle.done()