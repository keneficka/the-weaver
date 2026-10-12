import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("cyan")
t.speed(0)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
    t.circle(fibonacci(i), 90)
    t.left(90)

screen.mainloop()