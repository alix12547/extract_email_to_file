import turtle

achraf = turtle.Turtle()
turtle.bgcolor("black")
achraf.color("#4285F4", "#4285F4")
achraf.pensize(5)
achraf.speed(2)

# Positioning for each letter
achraf.penup()
achraf.setpos(-200, 0)  # Adjust the starting x-coordinate as per your preference
achraf.pendown()

# Drawing the letters vertically
achraf.left(90)
achraf.forward(150)
achraf.right(150)
achraf.forward(150)
achraf.backward(75)
achraf.right(105)
achraf.forward(60)
achraf.left(75)

achraf.penup()
achraf.setpos(-50, 0)  # Adjust the x-coordinate for the next letter
achraf.pendown()

achraf.left(105)
achraf.forward(150)
achraf.right(105)
achraf.circle(-75, 225)

achraf.penup()
achraf.setpos(100, 0)  # Adjust the x-coordinate for the next letter
achraf.pendown()

achraf.left(90)
achraf.forward(150)
achraf.backward(75)
achraf.right(90)
achraf.forward(75)
achraf.left(90)
achraf.forward(75)
achraf.backward(150)

achraf.penup()
achraf.setpos(250, 0)  # Adjust the x-coordinate for the next letter
achraf.pendown()

achraf.left(90)
achraf.forward(150)
achraf.right(90)
achraf.circle(-75, 180)
achraf.right(90)
achraf.forward(150)

achraf.hideturtle()
turtle.done()
