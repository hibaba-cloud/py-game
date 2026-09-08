import pgzrun
WIDTH=500
HEIGHT=350
TITLE="beautiful nature"


coco=Actor("fluttershy")
coco.pos=(WIDTH/2,HEIGHT/2)

def draw():
    screen.blit("nature",(0,0))
    coco.draw()

def update():
    if keyboard.up:
        coco.y-=10
    if keyboard.down:
        coco.y+=10
    if keyboard.right:
        coco.x+=10
    if keyboard.left:
        coco.x-=10


pgzrun.go()