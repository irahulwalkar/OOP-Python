import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")
        
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")
    brad.speed('1')

    i = 100
    while(i >= 10):
        j = 1
        while(j <= 6):
            brad.forward(i)
            brad.right(60)
            j = j + 1
        i = i - 10
    
    window.exitonclick()

draw_square()
