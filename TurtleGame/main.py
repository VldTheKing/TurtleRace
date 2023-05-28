from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Make your choice", "Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
all_turtles = []

y_axis = -100
for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    turtle_color = random.choice(colors)
    new_turtle.color(turtle_color)
    colors.pop(colors.index(turtle_color))
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis += 50

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print("You guessed the right color! You win!")
            else:
                print(f"You didn't guess the right color. The {winning_color} turtle won the race!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()