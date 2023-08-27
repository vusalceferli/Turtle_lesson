import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('black')
turtle_screen.title('Spiral Test')

turtle_ins = turtle.Turtle()
turtle_ins.color('red')
turtle_ins.speed(50)
turtle_ins.pensize(2)


#turtle_ins.circle(150)
#turtle_ins.circle(-150)


turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue']

for i in range(50):
    turtle_ins.color(turtle_colors [i % 5])
    turtle_ins.circle(7*i)
    turtle_ins.circle(-7 * i)
    turtle_ins.left(i)

turtle.mainloop()
#turtle.done()