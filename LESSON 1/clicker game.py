import pgzrun,random
WIDTH=550
HEIGHT=400
TITLE="steal the money"
kitty=Actor("rich kitty")
x=random.randint(0,WIDTH)
y=random.randint(0,HEIGHT)
kitty.pos=(x,y)


def draw():
    screen.fill(color="white")
    kitty.draw()
    screen.draw.text(str(score),center=(300,50),fontsize=20,color="black")


score=0
#on_mouse_down will check if you click and records pos(position) of mouse
def on_mouse_down(pos):
    global score
    # if kitty is being clicked
    if kitty.collidepoint(pos):
        score+=1
        x=random.randint(0,WIDTH)
        y=random.randint(0,HEIGHT)
        kitty.pos=(x,y)
    else:
        score-=1





pgzrun.go()