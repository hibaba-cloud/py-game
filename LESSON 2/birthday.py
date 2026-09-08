import pgzrun,random
WIDTH=450
HEIGHT=420
score=0
TITLE= "happy bday to mee"
hijabi=Actor("hijabi")
hijabi.pos=100,100
cake=Actor("cake")
cake.pos=180,190
def draw():
    screen.blit("bday bg",(0,0))
    hijabi.draw()
    cake.draw()
    screen.draw.text(str(score),(50,50),color="black")


def update():
    global score
    if keyboard.left:
        hijabi.x=hijabi.x-2
    if keyboard.right:
        hijabi.x=hijabi.x+2
    if keyboard.up:
        hijabi.y=hijabi.y-2
    if keyboard.down:
        hijabi.y=hijabi.y+2
    if hijabi.colliderect(cake):
        cake.x=random.randint(0,WIDTH)
        cake.y=random.randint(0,HEIGHT)
        score=score+1











pgzrun.go()