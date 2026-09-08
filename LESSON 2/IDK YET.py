import pgzrun,random

WIDTH=640
HEIGHT=480
rarity=Actor("rarity")
rarity.pos=(WIDTH/2,300)

garfeild=Actor("garfeild")
garfeild.pos=(80,50)

octopus=Actor("octopus")
octopus.pos=(560,50)
score=0


def draw():
    screen.blit("beach",(0,0))
    rarity.draw()
    garfeild.draw()
    octopus.draw()
    screen.draw.text("score: "+str(score),(450,10),fontsize=30,color="dark green")
   

def update():
    global score
    if keyboard.left:
        rarity.x-=5
    if keyboard.right:
        rarity.x+=5 
    #move garfeild down
    garfeild.y+=5
    #move octopus down
    octopus.y+=5 
    if garfeild.y>HEIGHT:
        garfeild.y=0
        garfeild.x=random.randint(0,WIDTH)
    if octopus.y>HEIGHT:
        octopus.y=0
        octopus.x=random.randint(0,WIDTH)
    if rarity.colliderect(garfeild):
        score+=1
        garfeild.y=0
        garfeild.x=random.randint(0,WIDTH)
    if rarity.colliderect(octopus):
        score-=1
        octopus.y=0
        octopus.x=random.randint(0,WIDTH)
        


        
    





pgzrun.go()