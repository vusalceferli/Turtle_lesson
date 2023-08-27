import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')
screen.title("catch the turtle")
FONT = ('Arial', 22, 'normal')
gride_size = 13
score = 0
game_over = False

#turtle list

turtle_list =[]

#score turtle

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color('dark red')
    score_turtle.penup()
    top_height = screen.window_height()/2
    y=top_height *0.87
    score_turtle.setpos(0,y)
    score_turtle.write(arg='Score 0', move=False,align='center', font=FONT)

setup_score_turtle()

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False,align='center', font=FONT)
        #print(x,y)

    t.onclick(handle_click)
    t.color('white')
    t.penup()
    t.shape('turtle')
    t.shapesize(1,1)
    t.goto(x*gride_size,y*gride_size)
    turtle_list.append(t)

x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [20, 10, 0, -10, -20]

def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color('dark blue')
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.87
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game over!", move=False, align='center', font=FONT)


def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()