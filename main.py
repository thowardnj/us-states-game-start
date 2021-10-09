import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = []
        for i in all_states:
            if i not in guessed_states:
                missed_states.append(i)
        missed = pd.DataFrame(missed_states)
        missed.to_csv('missed_states.csv')
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# states_to_learn.csv


screen.exitonclick()