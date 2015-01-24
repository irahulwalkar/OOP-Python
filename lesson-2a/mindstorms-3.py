import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    
    for i in range(1,73):
        draw_square(brad)
        brad.right(5)

    brad.right(90)
    brad.forward(300)

    window.exitonclick()


draw_art()
