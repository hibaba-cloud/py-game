import pgzrun 
import random
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("white")
    screen.blit("background",(0,0))
    for i in range (25):
      
      sattellite=Actor("satallite")
      sattellite.x=random.randint(0,400)
      sattellite.y=random.randint(0,400)
      sattellite.draw()
    












pgzrun.go()