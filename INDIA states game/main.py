import turtle
import pandas

states_data = pandas.read_csv("india_states.csv")
states_list = states_data.state.to_list()
screen = turtle.Screen()
screen.title("Indian States Game")
image = "india_states_blank.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 31:
    user_ans = screen.textinput(title=f"{len(guessed_states)}/31 States found",
                                prompt="What's the name of the state?").title()
    match = states_data[states_data["state"] == user_ans]

    if user_ans == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        print(missing_states)
        # new_data = pandas.DataFrame(missing_state)
        # new_data.to_csv("states_to_learn.csv")
        break
    if not match.empty:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(match.x.item(), match.y.item())
        t.write(match.state.item(), align="center")
        guessed_states.append(user_ans)
if len(guessed_states) == 31:
    print("Wonderful! You've guessed all the states.")