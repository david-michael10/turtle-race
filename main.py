from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your bet", prompt="Choose a color (red/orange/yellow/green/blue/purple): ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-100, -70, -40, -10, 20, 50]
turtles = []
winning_turtle = ""

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.goto(x=-230, y= positions[i])

if user_guess:
    is_on = True

while is_on:
    for i in turtles:

        if i.xcor() >= 230:
            is_on = False
            winning_turtle = i.pencolor()

        rand_distance = random.randint(1,10)
        i.forward(rand_distance)

if user_guess == winning_turtle:
    print(f"You win! The winner is '{winning_turtle}'")
else:
    print(f"You lose! The winner is '{winning_turtle}'")

screen.exitonclick()