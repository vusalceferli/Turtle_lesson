import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor ("pink")
drawing_board.title("cokbucakli")

turtle_ins = turtle.Turtle()

for i in range(10):
    turtle_ins.left(360/10)
    turtle_ins.forward(50)

turtle.done