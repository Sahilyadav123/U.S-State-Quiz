import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")

state_list = data.state.to_list()

count_list=[]
# for i in range(0,100):
while len(count_list) <= 50:
    answer_state = screen.textinput(title="Guess the state ", prompt=f"Start guessing! Score={len(count_list)}/50")
    capitalized = answer_state.title()
    # print(answer_state)

    if answer_state is None:
        break

    # print(x_cor)
    if capitalized in state_list:
        # score = score + 1;
        count_list.append(capitalized)
        sim = turtle.Turtle()
        sim.hideturtle()
        sim.penup()
        state_data = data[data.state == capitalized]
        sim.goto(int(state_data['x']), int(state_data['y']))
        sim.write(capitalized)
        # sim.goto(0, 0)

screen.mainloop()
