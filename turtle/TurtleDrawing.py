#Import turtle
import turtle
#
import colours as colours

turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)
#
#
# #Draw square
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()

# for colours in ["red","orange","yellow","green","pink","purple"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(10)
# turtle.done()
for i in range(10):
 for colours in ["red","orange","yellow","green","pink","purple","blue"]:
    turtle.color(colours)
    turtle.circle( 150)
    turtle.right(10)
turtle.done()

