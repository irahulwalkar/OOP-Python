import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    some_turtle.backward(100)
    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.backward(130)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #Crate turtle Angie - draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #Create turtle Jack - draws a triangle
    jack = turtle.Turtle()
    jack.shape("circle")
    jack.color("brown")
    draw_triangle(jack)
    
    window.exitonclick()


draw_art()
