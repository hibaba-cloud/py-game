import pgzrun
WIDTH=225
HEIGHT=400

cake=Actor("cake")
board=Actor("happy bday")
def draw():
    screen.blit("background",(0,0))

    
    cake.x=113
    cake.y=230
    cake.draw()
    board.x=113
    board.y=30
    board.draw()
    screen.draw.text("hope ur 8th treats u better than ur 7th!",center=(115,100),fontsize=18,color="navy")








pgzrun.go()
    
