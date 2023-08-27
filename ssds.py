import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("test square")

turtle_instance = turtle.Turtle()
for n in range(4):
    turtle_instance.forward(300)
    turtle_instance.right(90)

turtle_instance2 = turtle.Turtle()
turtle_instance2.right(55)
turtle_instance2.forward(100)

#turtle_instance3= turtle.Turtle()
for i in range(5):
    turtle_instance2.forward(200)
    turtle_instance2.left(144)

#turtle_instance3= turtle.Turtle()
turtle.done()