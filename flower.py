print "I love flowers!"
import turtle

window = turtle.Screen()
window.bgcolor('light blue')

def draw_triangle(triangle, length):
    j = 0
    while j < 3:
        triangle.forward(length)
        triangle.right(120)
        j = j + 1

def flower_layer(flower2, angle, length):
    i = 0
    repeat = int(360 /angle)
    while i < repeat:
        draw_triangle(flower2, length)
        flower2.right(angle)
        i = i + 1

def draw_flower(flower, angle, layers):
    #main functin that defines instance of Turtle class
    #and define shape of turtle
    flower = turtle.Turtle()
    flower.shape('turtle')
    flower.color('purple','pink')
    flower.speed(10)
    #repeat to layer flower
    k = 0
    length = 100
    while k < layers:
        flower_layer(flower, angle, length)
        k = k + 1
        length = length + 30
    #then move the turtle down to draw stem
    flower.right(90)
    flower.color("dark green")
    flower.forward(300)
    flower.right(155)
    flower.circle(150, 60)
    flower.left(120)
    flower.circle(150, 120)
    flower.left(120)
    flower.circle(150, 60)

draw_flower('babe', 15, 3)



window.exitonclick()
