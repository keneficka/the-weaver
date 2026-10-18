import turtle

def draw_pattern():
    turtle.speed(0)
    for i in range(120):
        turtle.forward(i)
        turtle.left(60)
    turtle.done()

if __name__ == "__main__":
    draw_pattern()