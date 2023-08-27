import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('black')
drawing_board.title('interactive game')

turtle_ins = turtle.Turtle()
turtle_ins.color('red')

def turtle_forward():
    turtle_ins.forward(50)

def turtle_forward_2():
    turtle_ins.back(50)

def turtle_right():
    turtle_ins.setheading(turtle_ins.heading()-20)
    #turtle_ins.left(45)

def turtle_left():
    turtle_ins.setheading(turtle_ins.heading() - 20)
    #turtle_ins.right(60)

def turtle_clear():
    turtle_ins.clear()

def turtle_returnHome():
    turtle_ins.home()
    turtle_ins.clear()

def turtle_pen_up():
    turtle_ins.penup()

def turtle_pen_down():
    turtle_ins.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key='w')
drawing_board.onkey(fun=turtle_forward_2, key='s')
drawing_board.onkey(fun=turtle_right, key='a')
drawing_board.onkey(fun=turtle_left, key='d')
drawing_board.onkey(fun=turtle_clear, key='space')
drawing_board.onkey(fun=turtle_returnHome, key='g')
drawing_board.onkey(fun=turtle_pen_up, key='q')
drawing_board.onkey(fun=turtle_pen_down, key='e')


turtle.mainloop()