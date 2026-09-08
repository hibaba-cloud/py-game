import pgzrun,random
WIDTH=500
HEIGHT=420
TITLE= "WINTERLAND"
snowman=Actor("snowman")
snowman.pos=100,100
present=Actor("present")
present.pos=180,190
def draw():
    screen.blit("winterland",(0,0))
    snowman.draw()
    present.draw()


def update():
    if keyboard.left:
        snowman.x=snowman.x-2
    if keyboard.right:
        snowman.x=snowman.x+2
    if keyboard.up:
        snowman.y=snowman.y-2
    if keyboard.down:
        snowman.y=snowman.y+2
    if snowman.colliderect(present):
        present.x=random.randint(0,WIDTH)
        present.y=random.randint(0,HEIGHT)










pgzrun.go()