import turtle
import math
import random

gamePr = turtle.Screen()
gamePr.bgcolor('black')
gamePr.title('Catch the turtle')

player=turtle.Turtle()
player.shape('turtle')

print(player.position())
player.penup()
player.goto(100,100)

player.color("red")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(-100, -100)

catcher=turtle.Turtle()
catcher.color("blue")
catcher.shape("triangle")
catcher.penup()
catcher.speed(5)
catcher.setposition(-50, 50)


speed = 2

score = 0
print ("\n" * 40)
print("Your score is:\n0")


def turtle_forward():
    catcher.forward(30)

def turtle_forward_2():
    catcher.back(30)

def turtle_right():
    catcher.right(25)

def turtle_left():
    catcher.left(25)

def turtle_pen_up():
    catcher.penup()


gamePr.listen()
gamePr.onkey(fun=turtle_forward, key='w')
gamePr.onkey(fun=turtle_forward_2, key='s')
gamePr.onkey(fun=turtle_right, key='a')
gamePr.onkey(fun=turtle_left, key='d')
gamePr.onkey(fun=turtle_pen_up, key='q')


while True:
    catcher.forward(speed)

    if catcher.xcor() > 300 or catcher.xcor() < -300:
        print("GAME OVER")
        quit()

    if catcher.ycor() > 300 or catcher.ycor() < -300:
        print("Game OVER")
        quit()

    d= math.sqrt(math.pow(catcher.xcor()-player.xcor(),2) + math.pow(catcher.ycor()-player.ycor(),2))

    if d < 20:
        player.setposition(random.randint(-300,300), random.randint(-300, 300))
        score = score + 1
        print ("\n" * 40)
        print("Your score is")
        print (score)

turtle.mainloop()