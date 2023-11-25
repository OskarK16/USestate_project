import turtle
import pandas

data = pandas.read_csv('50_states.csv')
countries = data["state"].to_list()
print(countries)

#Turtle settings
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

score = 0
is_game_on = True
while is_game_on:
    turtle.update()
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name?").title()
    if answer_state in countries:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}")
        countries.remove(answer_state)
        score += 1
        if score == 50:
            print("YOU ARE THE CHAMPION! You guessed all states. Congrats!")
            break

    elif answer_state == "Exit":
        print(f"You've score {score} points. If you want to learn more, go to states_to_learn file. Good luck!")
        break

if len(countries) > 0:
    states_missing = pandas.DataFrame(countries)
    states_missing.to_csv("states_to_learn.csv")
