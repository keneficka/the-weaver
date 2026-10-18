# Optimized Fibonacci Spiral Generator
import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fibonacci Spiral")

# Create turtle
pen = turtle.Turtle()
pen.color("cyan")
pen.speed(0)
pen.width(2)

# Fibonacci sequence generation
a, b = 0, 1
for _ in range(10):  # Minimal iterations
    pen.circle(b, 90)  # Draw quarter-circle with radius b
    a, b = b, a + b

# Finish up
pen.hideturtle()
turtle.done()