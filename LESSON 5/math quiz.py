import pgzrun
import random

WIDTH = 400
HEIGHT = 400

math = Actor("math")
math.center = (200, 70)

button = Actor("button")
button.center = (200, 300)

visible = True
questionvisible = False

firstnumber = random.randint(1, 12)
secondnumber = random.randint(1, 12)

question = str(firstnumber) + " x " + str(secondnumber) + " = "
rounds=0
answer = ""
message = ""
timer=10


def draw():
    global firstnumber,secondnumber,timer,questionvisible

    question = str(firstnumber) + " x " + str(secondnumber) + " = "
    screen.fill("navy")

    # Draw the math image
    math.draw()
    screen.draw.text("Rounds:"+str(rounds),center=(300,200),color="white")

    # Show button before it is clicked
    if visible:
        button.draw()

    # Show question after button is clicked
    if questionvisible:
        screen.draw.text(
            question,
            (100, 250),
            fontsize=30,
            color="white"
        )

        # Answer box
        screen.draw.rect(
            Rect((100, 290), (200, 45)),
            "white"
        )

        screen.draw.text(
            answer,
            (110, 300),
            fontsize=25,
            color="black"
        )
        screen.draw.text(
            "Press ENTER to submit",
            (80, 350),
            fontsize=18,
            color="white"
        )

    # Show result
    if message:
        screen.draw.text(
            message,
            (150, 175),
            fontsize=30,
            color="black"
        )

    # Timer text
    if questionvisible==True:
        
    
        screen.draw.text(
        "Time = "+str(timer),
        (120, 200),
        fontsize=25,
        color="white"
        )
    if timer==0:

        questionvisible=False


def on_mouse_down(pos):
    global visible, questionvisible,timer

    if visible and button.collidepoint(pos):
        visible = False
        questionvisible = True
        timer=10

def on_key_down(key):
    global answer, message,rounds,firstnumber,secondnumber

    if questionvisible:

        # Submit answer when Enter is pressed
        if key == keys.RETURN:
            if answer != "":
                if int(answer) == firstnumber * secondnumber:
                    message = "Correct!"
                    rounds=rounds+1
                else:
                    message = "Incorrect!"
                    rounds=rounds+1
                firstnumber=random.randint (1,12)
                secondnumber=random.randint (1,12)
                answer=""

        # Delete last character
        elif key == keys.BACKSPACE:
            answer = answer[:-1]

        # Add number to answer
        elif key.name in ["K_0", "K_1", "K_2", "K_3", "K_4",
                          "K_5", "K_6", "K_7", "K_8", "K_9"]:

            number = key.name[-1]
            answer += number
def decrease_timer():
    global timer
    if timer>0:
        timer=timer-1
clock.schedule_interval(decrease_timer,1.0)


pgzrun.go()

 