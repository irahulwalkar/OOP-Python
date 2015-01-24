import turtle

    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    
    brad.right(90)
    brad.backward(200)
    brad.right(135)
    brad.backward(75)
    brad.right(90)
    brad.backward(75)
    brad.right(90)
    brad.forward(125)

    angie = turtle.Turtle()
    angie.shape("circle")
    angie.speed(10)

    angie.right(80)
    angie.forward(200)
    angie.left(150)
    angie.forward(200)
    angie.left(40)
    angie.backward(200)
    angie.left(150)
    angie.backward(200)
    

    window.exitonclick()


draw_art()
