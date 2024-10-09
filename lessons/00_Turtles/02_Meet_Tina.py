"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast
tina.color(“black”)
tina.circle(30,180)
tina.forward(70)
tina.circle(30,180)
tina.forward(70)
tina.penup()
tina.forward(70)
tina.pendown()
tina.left(90)
tina.forward(60)
tina.circle(75,180)
tina.penup()
tina.forward(60)
tina.pendown()
tina.forward(140)
tina.circle(27,180)
tina.forward(50)
tina.circle(-21,180)
tina.forward(50)
tina.circle(27,180)
tina.forward(200)
tina.right(90)
tina.circle(-40,90)
tina.forward(70)
tina.circle(-40,90)
tina.penup()
tina.forward(80)
tina.right(90)
tina.forward(150)
tina.right(180)
tina.pendown()
tina.pencolor("cyan")
tina.circle(-30,90)
tina.forward(60)


turtle.exitonclick()
               # Close the window when we click on it

# Now you can try writing your own programs. Open
# the next file 03_Turtle_Tricks.py

