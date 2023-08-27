import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('yellow')
drawing_board.title('chokbucakli2')

turtle_ins = turtle.Turtle()

num_sides = 7
num_degree = 360 / 7
side_ins = 70

for i in range(num_sides):
    turtle_ins.right(num_degree)
    turtle_ins.forward(side_ins)

turtle.done()