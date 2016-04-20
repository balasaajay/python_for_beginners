import turtle

def draw_figure():
    window=turtle.Screen()
    window.bgcolor("pink")
    draw_flower = turtle.Turtle()
    draw_flower.shape("turtle")
    draw_flower.color("blue")
    draw_flower.speed(10)
    for j in range(1,37):
        draw_a_square(draw_flower)
        draw_flower.right(10)
    draw_flower.right(90)
    draw_flower.forward(250)
    window.exitonclick()

def draw_a_square(draw_square):
    for i in range(1,5):
        draw_square.forward(100)
        draw_square.right(90)

draw_figure()