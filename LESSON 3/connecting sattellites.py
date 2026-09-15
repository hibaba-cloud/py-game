import pgzrun 
import random
WIDTH=400
HEIGHT=400
lines=[]
sattellites=[]
def create_sattelites():
   for i in range (25):
         
         sattellite=Actor("satallite")
         sattellite.x=random.randint(0,400)
         sattellite.y=random.randint(0,400)
         sattellites.append(sattellite)
  
create_sattelites()   
def draw():
    screen.fill("white")
    screen.blit("background",(0,0))
    for i in sattellites:
        i.draw()
    if len(lines)>2:
      for i in range(0,len(lines)-1,2):
        screen.draw.line(lines[i],lines[i+1],"red")  
    

def on_mouse_down (pos):
   for i in sattellites:
      if i.collidepoint(pos):
         lines.append(i.pos)
   print(lines)
   
   
    












pgzrun.go()