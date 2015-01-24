import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")

    brad.forward(50)
    brad.right(60)
    brad.forward(50)
    brad.right(60)
    brad.forward(50)
    brad.right(30)
    

    window.exitonclick()

draw_triangle()
    
