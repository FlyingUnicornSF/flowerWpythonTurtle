print "I love flowers!"
import turtle

window = turtle.Screen()
window.bgcolor('light blue')

def draw_triangle(length):
    j = 0
    while j < 3:
        turtle.forward(length)
        turtle.right(120)
        j = j + 1

def flower_layer(angle, length):
    i = 0
    repeat = int(360 /angle)
    while i < repeat:
        draw_triangle(length)
        turtle.right(angle)
        i = i + 1

def draw_flower(angle, layers):
    #main functin that defines instance of Turtle class
    #and define shape of turtle
    turtle.shape('turtle')
    turtle.color('purple','pink')
    turtle.speed(10)
    #repeat to layer flower
    k = 0
    length = 100
    while k < layers:
        flower_layer(angle, length)
        k = k + 1
        length = length + 30
    #then move the turtle down to draw stem
    turtle.right(90)
    turtle.color("dark green")
    turtle.forward(300)
    turtle.right(155)
    turtle.circle(150, 60)
    turtle.left(120)
    turtle.circle(150, 120)
    turtle.left(120)
    turtle.circle(150, 60)

draw_flower(15, 3)



window.exitonclick()
