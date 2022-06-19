import turtle

s=turtle.getscreen()
t1=turtle.Turtle()

# set the fillcolor
t1.fillcolor('red')
#start the filling color
t1.begin_fill()
t1.goto(100,0)
t1.goto(0,100)
t1.goto(-100,0)
t1.goto(0,0)
# ending the filling of the color
t1.end_fill()


