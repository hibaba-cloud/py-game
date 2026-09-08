import pgzrun
WIDTH = 600
HEIGHT = 400
TITLE="OCEAN SCENERY"
otteroo=Actor("otter")
otteroo.pos=(WIDTH/2,HEIGHT/2)






def draw():
    screen.blit("oceanscenery",(0,0))
    otteroo.draw()

def update():
     if keyboard.up:
        otteroo.y-=10
     if keyboard.down:
        otteroo.y+=10
     if keyboard.right:
        otteroo.x+=10
     if keyboard.left:
        otteroo.x-=10   


pgzrun.go()