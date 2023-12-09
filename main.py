import pandas
from turtle import Turtle,Screen

turtle=Turtle()
screen=Screen()

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.title("U.S. States Game")
screen.setup(height=491,width=725)
states_data=pandas.read_csv("50_states.csv")

guessed_states=[]
states_name=states_data.state
states_list=states_name.to_list()

while len(guessed_states)<50:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State name? ")
    state_title=answer_state.title()

    if state_title in states_list:
        pointer=Turtle()
        pointer.penup()
        pointer.hideturtle()
        guessed_states.append(state_title)
        states_coor=states_data[states_name==state_title]
        pointer.goto(float(states_coor.x),float(states_coor.y))
        pointer.write(state_title)

    if state_title=="Exit":
        missing_states=[states for states in states_list if states not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
