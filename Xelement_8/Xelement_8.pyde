

import random
tetrisX = 1600
startButton = [860, 850, 250, 100]
textveld = [100, 100, 1550, 150]
playerbox = [1750, 100, 100, 100]
nextButton = [1550, 850, 250, 100]
rollButton = [860, 850, 250, 100]
firstRollP1 = [300, 200]
firstRollP2 = [1620, 200]
firstRollP3 = [300, 714]
firstRollP4 = [1620, 714]
buyTetrisP1 =  [tetrisX, 100, 75, 80]
buyTetrisP2 =  [tetrisX, 300, 75, 80]
buyTetrisP3 =  [tetrisX, 500, 75, 80]
buyTetrisP4 =  [tetrisX, 700, 75, 80]
elements = [800, 100, 300, 500, 700]
d1 = 0
d2 = 0
d3 = 0
d4 = 0


Button=[1500,840,840,830,850,850]
rps=[200,1550,450,700,1540,1630,1720,850]
playertext=[200,1550,100]
texts=["RPS Game","Go again","Next"]




#sachil
coin_image_x = 340
coin_image_y = 100
coin_image_y_diff = 200
coin_image_wh = 80
plus_min_y = 200
plus_min_x = 320
plus_min_diff = 60
#############################################################################################################################################

def keyTyped():
    pass    

def rgbcolor():
    if frameCount % 60 <= 20:
        fill(255,0,0)
    elif frameCount % 60 <= 40:
        fill(0,255,0)
    else:
        fill(0,0,255)

#################################################### DICE DICE DICE #####################################################################



def diceCycle(x, y):
    if frameCount % 60 <= 10:
        image(dice1, x, y)
    elif frameCount % 60 <= 20:
        image(dice2, x, y)
    elif frameCount % 60 <= 30:
        image(dice3, x, y)
    elif frameCount % 60 <= 40:
        image(dice4, x, y)
    elif frameCount % 60 <= 50:
        image(dice5, x, y)
    else:
        image(dice6, x, y)


def rollDice(x, y):
    d = random.randint(1,6)
    return d

def rollP1(d1):
    if d1 == 1:
        return image(dice1, firstRollP1[0], firstRollP1[1])
    elif d1 == 2:
        return image(dice2, firstRollP1[0], firstRollP1[1])
    elif d1 == 3:
        return image(dice3, firstRollP1[0], firstRollP1[1])
    elif d1 == 4:
        return image(dice4, firstRollP1[0], firstRollP1[1])
    elif d1 == 5:
        return image(dice5, firstRollP1[0], firstRollP1[1])
    elif d1 == 6:
        return image(dice6, firstRollP1[0], firstRollP1[1])

def rollP2(d2):
    if d2 == 1:
        return image(dice1, firstRollP2[0], firstRollP2[1])
    elif d2 == 2:
        return image(dice2, firstRollP2[0], firstRollP2[1])
    elif d2 == 3:
        return image(dice3, firstRollP2[0], firstRollP2[1])
    elif d2 == 4:
        return image(dice4, firstRollP2[0], firstRollP2[1])
    elif d2 == 5:
        return image(dice5, firstRollP2[0], firstRollP2[1])
    elif d2 == 6:
        return image(dice6, firstRollP2[0], firstRollP2[1])

def rollP3(d3):
    if d3 == 1:
        return image(dice1, firstRollP3[0], firstRollP3[1])
    elif d3 == 2:
        return image(dice2, firstRollP3[0], firstRollP3[1])
    elif d3 == 3:
        return image(dice3, firstRollP3[0], firstRollP3[1])
    elif d3 == 4:
        return image(dice4, firstRollP3[0], firstRollP3[1])
    elif d3 == 5:
        return image(dice5, firstRollP3[0], firstRollP3[1])
    elif d3 == 6:
        return image(dice6, firstRollP3[0], firstRollP3[1])
    
def rollP4(d4):
    if d4 == 1:
        return image(dice1, firstRollP4[0], firstRollP4[1])
    elif d4 == 2:
        return image(dice2, firstRollP4[0], firstRollP4[1])
    elif d4 == 3:
        return image(dice3, firstRollP4[0], firstRollP4[1])
    elif d4 == 4:
        return image(dice4, firstRollP4[0], firstRollP4[1])
    elif d4 == 5:
        return image(dice5, firstRollP4[0], firstRollP4[1])
    elif d4 == 6:
        return image(dice6, firstRollP4[0], firstRollP4[1])
    
def firstRoll():
    global d1, d2, d3, d4, valid_roll
    textFont(font)
    if playercounter == 2:
        d1 = rollDice(firstRollP1[0], firstRollP1[1])
        rollP1(d1)
        d2 = rollDice(firstRollP2[0], firstRollP2[1])
        rollP2(d2)
        if d1 > d2:
            text("Player 1 starts!", 500, 100)
            valid_roll = False
        elif d2 > d1:
            text("Player 2 starts!", 500, 100)
            valid_roll = False
        else:
            pass
    elif playercounter == 3:
        background(img)
        textFont(smallfont)
        fill(255)
        text("Player 1: ", firstRollP1[0] - 100, firstRollP1[1] + 50)
        text("Player 2: ", firstRollP2[0] - 100, firstRollP2[1] + 50)
        text("Player 3: ", firstRollP3[0] - 100, firstRollP3[1] + 50)
        textFont(font)
        if d1 == d2 and d1 == d3:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
        elif d1 == 2 and d1 != d3:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            if d1 > d2:
                text("Player 1 starts!", 500, 100)
                valid_roll = False
            else:
                text("Player 2 starts!", 500, 100)
                valid_roll = False
        elif d1 == d3 and d1 != d2:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            if d1 > d3:
                text("Player 1 starts!", 500, 100)
                valid_roll = False
            else:
                text("Player 3 starts!", 500, 100)
                valid_roll = False
        elif d2 == d3:
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            if d2 > d3:
                text("Player 2 starts!", 500, 100)
                valid_roll = False
            else:
                text("Player 3 starts!", 500, 100)
                valid_roll = False
                
                
    elif playercounter == 4:
        background(img)
        textFont(smallfont)
        fill(255)
        text("Player 1: ", firstRollP1[0] - 100, firstRollP1[1] + 50)
        text("Player 2: ", firstRollP2[0] - 100, firstRollP2[1] + 50)
        text("Player 3: ", firstRollP3[0] - 100, firstRollP3[1] + 50)
        text("Player 4: ", firstRollP4[0] - 100, firstRollP4[1] + 50)
        textFont(font)
        if d1 == d2 and d1 == d3 and d1 == d4:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d2 and d1 == d3 and d1 != d4:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            if d1 > d2 and d1 > d3:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            else:
                text("player 3 starts!", 500, 100)
                valid_roll = False
        elif d1 == d3 and d1 == d4 and d1 != d2:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1  and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d2 and d1 == d4 and d1 != d3:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d2 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d2 == d3 and d2 == d4:
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d2 and d3 == d4:
            if d1 > d3:
                d1 = rollDice(firstRollP1[0], firstRollP1[1])
                rollP1(d1)
                d2 = rollDice(firstRollP2[0], firstRollP2[1])
                rollP2(d2)
                
            else:
                d3 = rollDice(firstRollP3[0], firstRollP3[1])
                rollP3(d3)
                d4 = rollDice(firstRollP4[0], firstRollP4[1])
                rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d3 and d2 == d4:
            if d1 > d2:
                d1 = rollDice(firstRollP1[0], firstRollP1[1])
                rollP1(d1)
                d3 = rollDice(firstRollP3[0], firstRollP3[1])
                rollP3(d3)
            else:
                d2 = rollDice(firstRollP2[0], firstRollP2[1])
                rollP2(d2)
                d4 = rollDice(firstRollP4[0], firstRollP4[1])
                rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d2 and d1 != d3 and d1 != d4:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d3 and d1 != d4:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d1 == d4:
            d1 = rollDice(firstRollP1[0], firstRollP1[1])
            rollP1(d1)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d2 == d3 and d2 != d4:
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d2 == d4:
            d2 = rollDice(firstRollP2[0], firstRollP2[1])
            rollP2(d2)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
        elif d3 == d4:
            d3 = rollDice(firstRollP3[0], firstRollP3[1])
            rollP3(d3)
            d4 = rollDice(firstRollP4[0], firstRollP4[1])
            rollP4(d4)
            if d1 > d2 and d1 > d3 and d1 > d4:
                text("player 1 starts!", 500, 100)
                valid_roll = False
            elif d2 > d1 and d2 > d3 and d2 > d4:
                text("player 2 starts!", 500, 100)
                valid_roll = False
            elif d3 > d1 and d3 > d2 and d3 > d4:
                text("player 3 starts!", 500, 100)
                valid_roll = False
            elif d4 > d1 and d4 > d2 and d4 > d3:
                text("player 4 starts!", 500, 100)
                valid_roll = False
            else:
                pass
################################################################################### SETUP SETUP SETUP ############################################



def setup():
    global valid_roll, d1, d2, d3, d4, mainmenu, playerscreen, firstrollscreen, gamescreen, rollcounter, img, smallfont, font, playercounter, playerbuttonstate1, playerbuttonstate2, playerbuttonstate3, playerbuttonstate4, dice1, dice2, dice3, dice4, dice5, dice6, bgcounter, tetrisBlue, tetrisRed, tetrisOrange, tetrisYellow, tetrisGreen, buyTetris, player1Tetris, player2Tetris, player3Tetris, player4Tetris, coin_player1, coin_player2, coin_player3, coin_player4, coin_player1_count, coin_player2_count, coin_player3_count, coin_player4_count, player1_plus_button, player1_min_button, player1_plus_button, player1_min_button, fire, fireG, water, waterG, earth, earthG, nature, natureG, player ,choose0,change0,choose1,change1,choose2,change2,choose3,change3,playerelement0,playerelement1,playerelement2,playerelement3,scissors,rock,paper,RPS,buttons,scissors1,rock1,paper1,player_2,player_1, buttoncounter, current_tetP1, current_tetP2, current_tetP3, current_tetP4, dkimg, P1, P2, P3, P4 
    img = loadImage("Xelementbg.jpg")
    dkimg = loadImage("darkBG.jpg")
    dice1 = loadImage("Dice1.png")
    dice2 = loadImage("Dice2.png")
    dice3 = loadImage("Dice3.png")
    dice4 = loadImage("Dice4.png")
    dice5 = loadImage("Dice5.png")
    dice6 = loadImage("Dice6.png")
    tetrisBlue = loadImage("TetrisBlue.png")
    tetrisOrange = loadImage("TetrisOrange.png")
    tetrisGreen = loadImage("TetrisGreen.png")
    tetrisYellow = loadImage("TetrisYellow.png")
    tetrisRed = loadImage("TetrisRed.png")
    buyTetris = loadImage("BuyTetris.png")
    playercounter = 0
    playerbuttonstate1 = False
    playerbuttonstate2 = False
    playerbuttonstate3 = False
    playerbuttonstate4 = False
    valid_roll = True
    mainmenu = True
    playerscreen = False
    firstrollscreen = False
    gamescreen = False
    rollcounter = 0
    bgcounter = 0
    size(1920, 1014)
    font = createFont("Algerian", 60)
    smallfont = createFont("Arial", 24)
    
    tetriscounter = 0
    player1Tetris = False
    player2Tetris = False
    player3Tetris = False
    player4Tetris = False
    
    current_tetP1 = 0
    current_tetP2 = 0
    current_tetP3 = 0
    current_tetP4 = 0
    
    #SACHIL ZIJN CODE
    coin_player1 = loadImage("coin_player1.png")
    coin_player2 = loadImage("coin_player2.png")
    coin_player3 = loadImage("coin_player3.png")
    coin_player4 = loadImage("coin_player4.png")
    player1_plus_button = loadImage("player1_plus_button.png")
    player1_min_button = loadImage("player1_min_button.png")
    
    coin_player4_count = 0
    coin_player3_count = 0
    coin_player2_count = 0
    coin_player1_count = 0
    
    # Esmaiel
    choose0=choose1=choose2=choose3=True
    change0=change1=change2=change3=False
    
    fire=loadImage("Fire.png")
    fireG=loadImage("FireG.png")
    water=loadImage("Water.png")
    waterG=loadImage("WaterG.png")
    earth=loadImage("Earth.png")
    earthG=loadImage("EarthG.png")
    nature=loadImage("Nature.png")
    natureG=loadImage("NatureG.png")
    
    
    rock=loadImage("Rock.png")
    paper=loadImage("Paper.png")
    scissors=loadImage("Scissors.png")
    rock1=loadImage("Rock1.png")
    paper1=loadImage("Paper1.png")
    scissors1=loadImage("Scissors1.png")
    RPS=False
    buttons=True
    player_1=False  
    player_2=False
    buttoncounter=0
    
    P1 = 'Player 1'
    P2 = 'Player 2'
    P3 = 'Player 3'
    P4 = 'Player 4'

######################################################################## DRAW DRAW DRAW DRAW ##########################################3

# Roy
def draw():
    global selectelement
    if mainmenu == True:
        mainMenu()
    elif playerscreen == True:
        playerScreen()
    elif firstrollscreen == True:
        firstRollScreen()
    elif gamescreen == True:
        gameScreen()
    elif RPS==True:
        RPSgame(buttoncounter)

    
    

        

##################################### TEST TEST #############################
def mouseClicked():
    global mainmenu, playerscreen, firstrollscreen, gamescreen, rollcounter , playercounter, clicked, playerbuttonstate1, playerbuttonstate2, playerbuttonstate3, playerbuttonstate4, bgcounter, buyTetrisP1, player1Tetris, player2Tetris , player3Tetris , player4Tetris, coin_player1_count, coin_player2_count, coin_player3_count, coin_player4_count,RPS, current_tet1, current_tet2, current_tet3, current_tet4, current_tetP1, current_tetP2, current_tetP3, current_tetP4 

    if gamescreen == True:    
        if playercounter == 4:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                current_tet1 = generateTetris(buyTetrisP1[0], buyTetrisP1[1])
                current_tetP1 = 1
        
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                current_tet2 = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                current_tetP2 = 1
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:
                current_tet3 = generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                current_tetP3 = 1
                    
            if buyTetrisP4[0] < mouseX < buyTetrisP4[0] + buyTetrisP4[2] and buyTetrisP4[1] < mouseY < buyTetrisP4[1] + buyTetrisP4[3]:
                current_tet4 = generateTetris(buyTetrisP4[0], buyTetrisP4[1])
                current_tetP4 = 1
        
        if playercounter == 3:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                current_tet1 = generateTetris(buyTetrisP1[0], buyTetrisP1[1])
                current_tetP1 = 1
        
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                current_tet2 = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                current_tetP2 = 1
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:
                current_tet3 = generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                current_tetP3 = 1
                
        if playercounter == 2:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                current_tet1 = generateTetris(buyTetrisP1[0], buyTetrisP1[1])
                current_tetP1 = 1
        
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                current_tet2 = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                current_tetP2 = 1
                
    
                
            
#KLAAR            
def mouseReleased():
    if gamescreen == True:    
        if playercounter == 4:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                fill(0)
                rect(buyTetrisP1[0]-6, buyTetrisP1[1]-6,buyTetrisP1[2]+10, buyTetrisP1[3]+4,20)
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                fill(0)
                rect(buyTetrisP2[0]-6, buyTetrisP2[1]-6,buyTetrisP2[2]+10, buyTetrisP2[3]+4,20)
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:    
                fill(0)
                rect(buyTetrisP3[0]-6, buyTetrisP3[1]-6,buyTetrisP3[2]+10, buyTetrisP3[3]+4,20)
            
            if buyTetrisP4[0] < mouseX < buyTetrisP4[0] + buyTetrisP4[2] and buyTetrisP4[1] < mouseY < buyTetrisP4[1] + buyTetrisP4[3]:   
                fill(0)
                rect(buyTetrisP4[0]-6, buyTetrisP4[1]-6,buyTetrisP4[2]+10, buyTetrisP4[3]+4,20)
                
                
        if playercounter == 3:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                fill(0)
                rect(buyTetrisP1[0]-6, buyTetrisP1[1]-6,buyTetrisP1[2]+10, buyTetrisP1[3]+4,20)
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                fill(0)
                rect(buyTetrisP2[0]-6, buyTetrisP2[1]-6,buyTetrisP2[2]+10, buyTetrisP2[3]+4,20)
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:    
                fill(0)
                rect(buyTetrisP3[0]-6, buyTetrisP3[1]-6,buyTetrisP3[2]+10, buyTetrisP3[3]+4,20)

                
        if playercounter == 2:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                fill(0)
                rect(buyTetrisP1[0]-6, buyTetrisP1[1]-6,buyTetrisP1[2]+10, buyTetrisP1[3]+4,20)
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                fill(0)
                rect(buyTetrisP2[0]-6, buyTetrisP2[1]-6,buyTetrisP2[2]+10, buyTetrisP2[3]+4,20)
         

            
    



###################################################################### MOUSE PRESSED MOUSE PRESSED ##################################################

def mousePressed():
    global mainmenu, playerscreen, valid_roll, firstrollscreen, gamescreen, rollcounter , playercounter, clicked, playerbuttonstate1, playerbuttonstate2, playerbuttonstate3, playerbuttonstate4, bgcounter, buyTetrisP1, player1Tetris, player2Tetris , player3Tetris , player4Tetris, coin_player1_count, coin_player2_count, coin_player3_count, coin_player4_count,RPS, current_tet1, current_tet2, current_tet3, current_tet4, current_tetP1, current_tetP2, current_tetP3, current_tetP4 
    # Roy
    if startButton[0] < mouseX < startButton[0] + startButton[2] and startButton[1] < mouseY < startButton[1] + startButton[3] and mainmenu == True:
        playerscreen = True
        mainmenu = False
        
        
        
    if nextButton[0] < mouseX < nextButton[0] + nextButton[2] and nextButton[1] < mouseY < nextButton[1] + nextButton[3] and playerscreen == True and playercounter >= 2:
        firstrollscreen = True
        playerscreen = False
        
        
    if rollButton[0] < mouseX < rollButton[0] + rollButton[2] and rollButton[1] < mouseY < rollButton[1] + rollButton[3] and firstrollscreen == True and valid_roll == True:
        rollcounter += 1
        firstRoll()
        
        
    if rollButton[0] + 300 < mouseX < rollButton[0] + rollButton[2] + 300 and rollButton[1] < mouseY < rollButton[1] + rollButton[3] and firstrollscreen == True:
        bgcounter = 0
        gamescreen = True
        firstrollscreen = False
        
        

         
        
        
# Roy 
    if playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] < mouseY < playerbox[1] + playerbox[3]and (playercounter == 0 or playercounter == 1):
        print("test")
        if playercounter == 0:
            playercounter += 1
            playerbuttonstate1 = True
        else:
            playercounter -= 1
            playerbuttonstate1 = False
            
            
            
    if playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 200 < mouseY < playerbox[1] + playerbox[3] + 200 and (playercounter == 1 or playercounter == 2):
        if playercounter == 1:
            playercounter += 1
            playerbuttonstate2 = True
        else:
            playercounter -= 1
            playerbuttonstate2 = False
            
            
            
    if playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 400 < mouseY < playerbox[1] + playerbox[3] + 400 and (playercounter == 2 or playercounter == 3):
        if playercounter == 2:
            playercounter += 1
            playerbuttonstate3 = True
        else:
            playercounter -= 1
            playerbuttonstate3 = False
            
            
            
    if playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 600 < mouseY < playerbox[1] + playerbox[3] + 600 and (playercounter == 3 or playercounter == 4):
        if playercounter == 3:
            playercounter += 1
            playerbuttonstate4 = True
        else:
            playercounter -= 1
            playerbuttonstate4 = False
            
            
            
            
            
            
# Kerem    

    if gamescreen == True:    
        if playercounter == 4:        
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                # print('Tetris stukje van player 1')
                # player1Tetris == True
                # generateTetris(buyTetrisP1[0],buyTetrisP1[1])
                fill(0,255,0)
                rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                # print('Tetris stukje van player 2')
                # player2Tetris == True
                # generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                # current_tet = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                fill(0,255,0)
                rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
                
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:
                # print('Tetris stukje van player 3')
                # player3Tetris == True
                # generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                # current_tet = generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                fill(0,255,0)
                rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
                
                
            if buyTetrisP4[0] < mouseX < buyTetrisP4[0] + buyTetrisP4[2] and buyTetrisP4[1] < mouseY < buyTetrisP4[1] + buyTetrisP4[3]:
                # print('Tetris stukje van player 4')
                # player4Tetris == True
                # generateTetris(buyTetrisP4[0], buyTetrisP4[1])
                # current_tet = generateTetris(buyTetrisP4[0], buyTetrisP4[1])
                fill(0,255,0)
                rect(buyTetrisP4[0]-5, buyTetrisP4[1]-5,buyTetrisP4[2]+9, buyTetrisP4[3]+3,20)
                
# Sachil    

            if isMouseWithinSpace(plus_min_x, plus_min_y, 50, 36):
                #bgcounter = 0
                coin_player1_count = coin_player1_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y, 50, 36):
                #bgcounter = 0 
                coin_player1_count = coin_player1_count - 1
                if coin_player1_count < 0:
                    coin_player1_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0
                coin_player2_count = coin_player2_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0 
                coin_player2_count = coin_player2_count - 1
                if coin_player2_count < 0:
                    coin_player2_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ (coin_image_y_diff* 2), 50, 36):
                #bgcounter = 0
                coin_player3_count = coin_player3_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ (coin_image_y_diff * 2), 50, 36):
                #bgcounter = 0 
                coin_player3_count = coin_player3_count - 1
                if coin_player3_count < 0:
                    coin_player3_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ (coin_image_y_diff* 3), 50, 36):
                #bgcounter = 0
                coin_player4_count = coin_player4_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ (coin_image_y_diff* 3), 50, 36):
                #bgcounter = 0 
                coin_player4_count = coin_player4_count - 1
                if coin_player4_count < 0:
                    coin_player4_count = 0

# Kerem

        elif playercounter == 3:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                # print('Tetris stukje van player 1')
                # player1Tetris == True
                # generateTetris(buyTetrisP1[0],buyTetrisP1[1])
                fill(0,255,0)
                rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                # print('Tetris stukje van player 2')
                # player2Tetris == True
                # generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                # current_tet = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                fill(0,255,0)
                rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
                
                
            if buyTetrisP3[0] < mouseX < buyTetrisP3[0] + buyTetrisP3[2] and buyTetrisP3[1] < mouseY < buyTetrisP3[1] + buyTetrisP3[3]:
                # print('Tetris stukje van player 3')
                # player3Tetris == True
                # generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                # current_tet = generateTetris(buyTetrisP3[0], buyTetrisP3[1])
                fill(0,255,0)
                rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
            
# Sachil

            if isMouseWithinSpace(plus_min_x, plus_min_y, 50, 36):
                #bgcounter = 0
                coin_player1_count = coin_player1_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y, 50, 36):
                #bgcounter = 0 
                coin_player1_count = coin_player1_count - 1
                if coin_player1_count < 0:
                    coin_player1_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0
                coin_player2_count = coin_player2_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0 
                coin_player2_count = coin_player2_count - 1
                if coin_player2_count < 0:
                    coin_player2_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ (coin_image_y_diff* 2), 50, 36):
                #bgcounter = 0
                coin_player3_count = coin_player3_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ (coin_image_y_diff * 2), 50, 36):
                #bgcounter = 0 
                coin_player3_count = coin_player3_count - 1
                if coin_player3_count < 0:
                    coin_player3_count = 0
    
# Kerem

        elif playercounter == 2:
            if buyTetrisP1[0] < mouseX < buyTetrisP1[0] + buyTetrisP1[2] and buyTetrisP1[1] < mouseY < buyTetrisP1[1] + buyTetrisP1[3]:
                # print('Tetris stukje van player 1')
                # player1Tetris == True
                # generateTetris(buyTetrisP1[0],buyTetrisP1[1])
                fill(0,255,0)
                rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            
                
            if buyTetrisP2[0] < mouseX < buyTetrisP2[0] + buyTetrisP2[2] and buyTetrisP2[1] < mouseY < buyTetrisP2[1] + buyTetrisP2[3]:
                # print('Tetris stukje van player 2')
                # player2Tetris == True
                # generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                # current_tet = generateTetris(buyTetrisP2[0], buyTetrisP2[1])
                fill(0,255,0)
                rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
                
    
            
# Sachil
            if isMouseWithinSpace(plus_min_x, plus_min_y, 50, 36):
                #bgcounter = 0
                coin_player1_count = coin_player1_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y, 50, 36):
                #bgcounter = 0 
                coin_player1_count = coin_player1_count - 1
                if coin_player1_count < 0:
                    coin_player1_count = 0
                    
            if isMouseWithinSpace(plus_min_x, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0
                coin_player2_count = coin_player2_count + 1
        
            if isMouseWithinSpace(plus_min_x + plus_min_diff, plus_min_y+ coin_image_y_diff, 50, 36):
                #bgcounter = 0 
                coin_player2_count = coin_player2_count - 1
                if coin_player2_count < 0:
                    coin_player2_count = 0
                
    
                
    
                
                
        
    

                           

            
###################################################################################### SCREEN SCREEN SCREEN ##############################################
# SACHIL
def isMouseWithinSpace(x, y, breedte, hoogte): 
    global mainmenu, playerscreen, firstrollscreen, gamescreen, rollcounter , playercounter, clicked, playerbuttonstate1, playerbuttonstate2, playerbuttonstate3, playerbuttonstate4, bgcounter, coin_player1_count
    if x < mouseX <x + breedte and y < mouseY < y + hoogte:
        return True
    else:
        return False
# Roy
def mainMenu():
    background(img)
    fill(255)
    textSize(100)
    text("Xelement", startButton[0] + 120, 150)
    if startButton[0] < mouseX < startButton[0] + startButton[2] and startButton[1] < mouseY < startButton[1] + startButton[3] and mousePressed:
        fill(40)
    elif startButton[0] < mouseX < startButton[0] + startButton[2] and startButton[1] < mouseY < startButton[1] + startButton[3]:
        fill(200)
    else:
        fill(100)
    
    rect(startButton[0], startButton[1], startButton[2], startButton[3], 10)
    
    fill(255)
    textFont(font)
    text("Start", startButton[0] + 130, startButton[1] + 70)
    textAlign(CENTER)
    
##################################################################################################################################################################    
# Roy
def playerScreen():
    background(img)
    textFont(smallfont)
    fill(150)
    rect(textveld[0], playerbox[1], textveld[2], playerbox[3],10)
    
    
    
    if playerbuttonstate1 == True:
        fill(0,255,0)
    elif playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] < mouseY < playerbox[1] + playerbox[3]:
        fill(155,255,155,227)
    else:
        fill(150)
        
        
        
    rect(playerbox[0], playerbox[1], playerbox[3], playerbox[2], 10)
    fill(255)
    fill(150)
    rect(textveld[0], playerbox[1] + 200, textveld[2], playerbox[3],10)
    
    
    
    if playerbuttonstate2 == True:
        fill(0,255,0)
    elif playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 200 < mouseY < playerbox[1] + playerbox[3] + 200:
        fill(155,255,155,227)
    else:
        fill(150)
        
        
        
    rect(playerbox[0], playerbox[1] + 200, playerbox[3], playerbox[2], 10)
    fill(255)
    fill(150)
    rect(textveld[0], playerbox[1] + 200, textveld[2], playerbox[3],10)
    
    
    
    
    if playerbuttonstate3 == True:
        fill(0,255,0)
    elif playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 400 < mouseY < playerbox[1] + playerbox[3] + 400:
        fill(155,255,155,227)
    else:
        fill(150)
        
        
        
    rect(playerbox[0], playerbox[1] + 400, playerbox[3], playerbox[2], 10)
    fill(255)
    fill(150)
    rect(textveld[0], playerbox[1] + 400, textveld[2], playerbox[3],10)
    
    
    
    
    if playerbuttonstate4 == True:
        fill(0,255,0)
    elif playerbox[0] < mouseX < playerbox[0] + playerbox[2] and playerbox[1] + 600 < mouseY < playerbox[1] + playerbox[3] + 600:
        fill(155,255,155,227)
    else:
        fill(150)
        
        
        
    rect(playerbox[0], playerbox[1] + 600, playerbox[3], playerbox[2], 10)
    fill(255)
    fill(150)
    rect(textveld[0], playerbox[1] + 600, textveld[2], playerbox[3],10)
    
    
    
    fill(255)
    textSize(38)
    text("Number of players: " + str(playercounter), textveld[0] + 180, playerbox[1] + 800)
    if playercounter > 1:
      if nextButton[0] < mouseX < nextButton[0] + nextButton[2] and nextButton[1] < mouseY < nextButton[1] + nextButton[3] and mousePressed:
          fill(40)
      elif nextButton[0] < mouseX < nextButton[0] + nextButton[2] and nextButton[1] < mouseY < nextButton[1] + nextButton[3]:
          fill(200)
      else:
          fill(80)
    else:
      fill(20)
      
      
      
      
    rect(nextButton[0], nextButton[1], nextButton[2], nextButton[3], 10)
    fill(255)
    textFont(font)
    text("Player 1", textveld[0] + 150, playerbox[1] + 75)
    text("Player 2", textveld[0] + 150, playerbox[1] + 275)
    text("Player 3", textveld[0] + 150, playerbox[1] + 475)
    text("Player 4", textveld[0] + 150, playerbox[1] + 675)
    text("Next", nextButton[0] + 130, nextButton[1] + 70)
    textAlign(CENTER)

######################################################################################FRSFRSFRSFRS#################################3


def firstRollScreen():
    global bgcounter
    if bgcounter == 0:
        background(img)
        bgcounter += 1


    textFont(smallfont)
    if rollcounter == 0:
        if playercounter == 2:
            fill(255)
            text("Player 1: ", firstRollP1[0] - 100, firstRollP1[1] + 50)
            text("Player 2: ", firstRollP2[0] - 100, firstRollP2[1] + 50)
            diceCycle(firstRollP1[0], firstRollP1[1])
            diceCycle(firstRollP2[0], firstRollP2[1])
        elif playercounter == 3:
            fill(255)
            text("Player 1: ", firstRollP1[0] - 100, firstRollP1[1] + 50)
            text("Player 2: ", firstRollP2[0] - 100, firstRollP2[1] + 50)
            text("Player 3: ", firstRollP3[0] - 100, firstRollP3[1] + 50)
            diceCycle(firstRollP1[0], firstRollP1[1])
            diceCycle(firstRollP2[0], firstRollP2[1])
            diceCycle(firstRollP3[0], firstRollP3[1])
        elif playercounter == 4:
            fill(255)
            text("Player 1: ", firstRollP1[0] - 100, firstRollP1[1] + 50)
            text("Player 2: ", firstRollP2[0] - 100, firstRollP2[1] + 50)
            text("Player 3: ", firstRollP3[0] - 100, firstRollP3[1] + 50)
            text("Player 4: ", firstRollP4[0] - 100, firstRollP4[1] + 50)
            diceCycle(firstRollP1[0], firstRollP1[1])
            diceCycle(firstRollP2[0], firstRollP2[1])
            diceCycle(firstRollP3[0], firstRollP3[1])
            diceCycle(firstRollP4[0], firstRollP4[1])
            
            
            
            
    else:
        if rollButton[0] + 300 < mouseX < rollButton[0] + rollButton[2] + 300 and rollButton[1] < mouseY < rollButton[1] + rollButton[3] and mousePressed:
            fill(40)
        elif rollButton[0] + 300 < mouseX < rollButton[0] + rollButton[2] + 300 and rollButton[1] < mouseY < rollButton[1] + rollButton[3]:
            fill(200)
        else:
            fill(80)
        rect(rollButton[0] + 300, rollButton[1], rollButton[2], rollButton[3], 10)
    
        fill(255)
        textFont(font)
        text("Next", rollButton[0] + 430, rollButton[1] + 70)
        textAlign(CENTER)


    if rollButton[0] < mouseX < rollButton[0] + rollButton[2] and rollButton[1] < mouseY < rollButton[1] + rollButton[3] and mousePressed and valid_roll == True:
        fill(40)
    elif rollButton[0] < mouseX < rollButton[0] + rollButton[2] and rollButton[1] < mouseY < rollButton[1] + rollButton[3] and valid_roll == True:
        fill(200)
    elif valid_roll == False:
        fill(20)
    else:
        fill(80)
    rect(rollButton[0], rollButton[1], rollButton[2], rollButton[3], 10)
    
    fill(255)
    textFont(font)
    text("Roll!", rollButton[0] + 130, rollButton[1] + 70)
    textAlign(CENTER)
    
    
############################################################################################################################################################

 
        
# Kerem    
def buyPieceButton(x, y):
    image(buyTetris, x, y)
    
def currentTetris1(x, y):
    image(current_tet1,x,y)          
    
def currentTetris2(x, y):
    image(current_tet2,x,y)    
    
def currentTetris3(x, y):
    image(current_tet3,x,y)    
    
def currentTetris4(x, y):
    image(current_tet4,x,y)    
    
  
    
# Kerem
def generateTetris(x, y):
    d = random.randint(1,6)
    if d == 1:
        return tetrisBlue
    elif d == 2:
        return tetrisOrange
    elif d == 3:
        return tetrisYellow
    elif d == 4:
        return tetrisRed
    elif d == 5:
        return tetrisGreen
    elif d == 6:
        return tetrisRed
        
# Kerem    
def randomTetris():
    buyTetris(randomTetris[0], randomTetris[1])    
             

# Roy
def gameScreen():
    global bgcounter, player1Tetris,RPS,gamescreen, current_tetP1, current_tetP2, current_tetP3, current_tetP4, dkimg
    smallfont = createFont("Arial", 55)
    textFont(smallfont)
    if bgcounter == 0:
        background(dkimg)
        bgcounter += 1

#Kerem
    if playercounter == 2:
        fill(255)
        text(P1,150,170)
        text(P2,150,370)
        if current_tetP1 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])        
        else:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            currentTetris1(buyTetrisP1[0], buyTetrisP1[1])            
            
        if current_tetP2 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        else:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            currentTetris2(buyTetrisP2[0], buyTetrisP2[1])
            
        # fill(255)
        # # # text("Generate new piece: ", buyTetrisP1[0] - 150, buyTetrisP1[1] + 50)
        # # # text("Generate new piece: ", buyTetrisP2[0] - 150, buyTetrisP2[1] + 50)
        # # buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])
        # # buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        
    elif playercounter == 3:
        fill(255)
        text(P1,150,170)
        text(P2,150,370)
        text(P3,150,570)
    
        if current_tetP1 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])        
        else:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            currentTetris1(buyTetrisP1[0], buyTetrisP1[1])            
            
        if current_tetP2 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        else:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            currentTetris2(buyTetrisP2[0], buyTetrisP2[1])
            
        if current_tetP3 == 0:
            # fill(0)
            # rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
            buyPieceButton(buyTetrisP3[0], buyTetrisP3[1])
        else:
            # fill(0)
            # rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
            currentTetris3(buyTetrisP3[0], buyTetrisP3[1])
        # fill(255)
        # text("Generate new piece: ", buyTetrisP1[0] - 150, buyTetrisP1[1] + 50)
        # text("Generate new piece: ", buyTetrisP2[0] - 150, buyTetrisP2[1] + 50)
        # text("Generate new piece: ", buyTetrisP3[0] - 150, buyTetrisP3[1] + 50)
        # buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])
        # buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        # buyPieceButton(buyTetrisP3[0], buyTetrisP3[1])
        
    elif playercounter == 4:
        fill(255)
        text(P1,150,170)
        text(P2,150,370)
        text(P3,150,570)
        text(P4,150,770)
    
        if current_tetP1 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])        
        else:
            # fill(255,255,0)
            # rect(buyTetrisP1[0]-5, buyTetrisP1[1]-5,buyTetrisP1[2]+9, buyTetrisP1[3]+3,20)
            currentTetris1(buyTetrisP1[0], buyTetrisP1[1])            
            
        if current_tetP2 == 0:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        else:
            # fill(255,255,0)
            # rect(buyTetrisP2[0]-5, buyTetrisP2[1]-5,buyTetrisP2[2]+9, buyTetrisP2[3]+3,20)
            currentTetris2(buyTetrisP2[0], buyTetrisP2[1])
            
        if current_tetP3 == 0:
            # fill(0)
            # rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
            buyPieceButton(buyTetrisP3[0], buyTetrisP3[1])
        else:
            # fill(0)
            # rect(buyTetrisP3[0]-5, buyTetrisP3[1]-5,buyTetrisP3[2]+9, buyTetrisP3[3]+3,20)
            currentTetris3(buyTetrisP3[0], buyTetrisP3[1])
            
        if current_tetP4 == 0:
            # fill(0)
            # rect(buyTetrisP4[0]-5, buyTetrisP4[1]-5,buyTetrisP4[2]+9, buyTetrisP4[3]+3,20)
            buyPieceButton(buyTetrisP4[0], buyTetrisP4[1])
        else:
            # fill(0)
            # rect(buyTetrisP4[0]-5, buyTetrisP4[1]-5,buyTetrisP4[2]+9, buyTetrisP4[3]+3,20)
            currentTetris4(buyTetrisP4[0], buyTetrisP4[1])
            
            
        # fill(255)
        # currentTetris(buyTetrisP1[0], buyTetrisP1[1])
        # currentTetris(buyTetrisP2[0], buyTetrisP2[1])
        # currentTetris(buyTetrisP3[0], buyTetrisP3[1])
        # currentTetris(buyTetrisP4[0], buyTetrisP4[1])
        # text("Generate new piece: ", buyTetrisP1[0] - 150, buyTetrisP1[1] + 50)
        # text("Generate new piece: ", buyTetrisP2[0] - 150, buyTetrisP2[1] + 50)
        # text("Generate new piece: ", buyTetrisP3[0] - 150, buyTetrisP3[1] + 50)
        # text("Generate new piece: ", buyTetrisP4[0] - 150, buyTetrisP4[1] + 50)
        # buyPieceButton(buyTetrisP1[0], buyTetrisP1[1])
        # buyPieceButton(buyTetrisP2[0], buyTetrisP2[1])
        # buyPieceButton(buyTetrisP3[0], buyTetrisP3[1])
        # buyPieceButton(buyTetrisP4[0], buyTetrisP4[1])

#sachil                
    if playercounter == 2:
        image(coin_player1, coin_image_x, coin_image_y, coin_image_wh, coin_image_wh)
        fill(0)
        rect(430, 100, 100, 80)
        fill(255,255,0)
        text(str(coin_player1_count), 480, 160)
        #text(str(coin_player1_count), 350, 470)
        image(player1_plus_button, plus_min_x, plus_min_y, 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y, 50, 36)
        
        fill(0)
        rect(450, 300, 100, 70)
        image(coin_player2, coin_image_x, coin_image_y + coin_image_y_diff, coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player2_count), 480,360)
        #text(str(coin_player2_count), 350, 670)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff), 50, 36)
    
        selectElement(0)
        selectElement(1)

    
    if playercounter == 3:
        image(coin_player1, coin_image_x, coin_image_y, coin_image_wh, coin_image_wh)
        fill(0)
        rect(430, 100, 100, 80)
        fill(255,255,0)
        text(str(coin_player1_count), 480, 160)
        #text(str(coin_player1_count), 350, 470)
        image(player1_plus_button, plus_min_x, plus_min_y, 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y, 50, 36)
        
        fill(0)
        rect(450, 300, 100, 70)
        image(coin_player2, coin_image_x, coin_image_y + coin_image_y_diff, coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player2_count), 480,360)
        #text(str(coin_player2_count), 350, 670)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff), 50, 36)
        
        fill(0)
        rect(450, 500, 100, 70)
        image(coin_player3, coin_image_x, coin_image_y + (coin_image_y_diff * 2), coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player3_count), 480, 560)
        #text(str(coin_player3_count), 350, 870)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff * 2), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff * 2), 50, 36)
        
        selectElement(0)
        selectElement(1)
        selectElement(2)
        
    if playercounter == 4:
        image(coin_player1, coin_image_x, coin_image_y, coin_image_wh, coin_image_wh)
        fill(0)
        rect(430, 100, 100, 80)
        fill(255,255,0)
        text(str(coin_player1_count), 480, 160)
        #text(str(coin_player1_count), 350, 470)
        image(player1_plus_button, plus_min_x, plus_min_y, 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y, 50, 36)
        
        fill(0)
        rect(450, 300, 100, 70)
        image(coin_player2, coin_image_x, coin_image_y + coin_image_y_diff, coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player2_count), 480,360)
        #text(str(coin_player2_count), 350, 670)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff), 50, 36)
        
        fill(0)
        rect(450, 500, 100, 70)
        image(coin_player3, coin_image_x, coin_image_y + (coin_image_y_diff * 2), coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player3_count), 480, 560)
        #text(str(coin_player3_count), 350, 870)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff * 2), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff * 2), 50, 36)
        
        fill(0)
        rect(450, 700, 100, 70)
        image(coin_player4, coin_image_x, coin_image_y + (coin_image_y_diff * 3), coin_image_wh, coin_image_wh)
        fill(255,255,0)
        text(str(coin_player4_count), 480, 760)
        #text(str(coin_player4_count), 350, 270)
        image(player1_plus_button, plus_min_x, plus_min_y + (coin_image_y_diff * 3), 50, 36)
        image(player1_min_button, plus_min_x + plus_min_diff, plus_min_y + (coin_image_y_diff * 3), 50, 36)
        
        selectElement(0)
        selectElement(1)
        selectElement(2)
        selectElement(3)
        

    
    #Esmaiel
    if rps[4]-20<mouseX<rps[4]-20 +300 and rps[7]+90 -100<mouseY<rps[7]+90 and mousePressed:
        fill(40)
        RPS=True
        gamescreen=False
    elif rps[4]-20<mouseX<rps[4]-20 +300 and rps[7]+90 -100<mouseY<rps[7]+90:
        fill(200)
    else:
        fill(80)
    
    rect(rps[4]-20,rps[7]+90,300,-100,10)
    image(rock1,rps[4],rps[7],80,80)
    image(scissors1,rps[5],rps[7],80,80)
    image(paper1,rps[6],rps[7],80,80)  
    

     
    
# Esmaiel
def selectElement(num):
    global choose0,change0,choose1,change1,choose2,change2,choose3,change3,playerelement0,playerelement1,playerelement2,playerelement3

    if (choose0==True and change0==False and num==0) or (choose1==True and change1==False and num==1) or (choose2==True and change2==False and num==2) or (choose3==True and change3==False and num==3):
        Elements(0,num)
        if mouseX > elements[0] and mouseX < elements[0]+80 and mouseY>elements[1+num] and mouseY<elements[1+num]+80 :
            image(nature,elements[0],elements[1+num],80,80) 
            if mousePressed==True:
                image(nature,elements[0],elements[1+num],80,80) 
                variables(num)
                playerElement(num,1)
        elif mouseX > elements[0] + 100 and mouseX < elements[0]+180 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(earth,elements[0] + 100,elements[1+num],80,80) 
            if mousePressed==True:
                image(earth,elements[0] + 100,elements[1+num],80,80) 
                variables(num)
                playerElement(num,2)
        elif mouseX > elements[0]+ 200 and mouseX < elements[0]+280 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(fire,elements[0]+ 200,elements[1+num],80,80)
            if mousePressed==True:
                image(fire,elements[0]+ 200,elements[1+num],80,80) 
                variables(num)
                playerElement(num,3)
        elif mouseX > elements[0]+ 300 and mouseX < elements[0]+380 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(water,elements[0]+ 300,elements[1+num],80,80)
            if mousePressed==True:
                image(water,elements[0]+300,elements[1+num],80,80) 
                variables(num)
                playerElement(num,4)
    if (choose0==False and change0==True and num==0) or (choose1==False and change1==True and num==1) or (choose2==False and change2==True and num==2) or (choose3==False and change3==True and num==3):
        if mouseX > elements[0] and mouseX < elements[0]+80 and mouseY>elements[1+num] and mouseY<elements[1+num]+80 :
            image(nature,elements[0],elements[1+num],80,80) 
            if mousePressed==True:
                Elements(1,num)
                playerElement(num,1)
            
        elif mouseX > elements[0]+100 and mouseX < elements[0]+180 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(earth,elements[0]+100,elements[1+num],80,80) 
            if mousePressed==True:
                Elements(2,num)
                playerElement(num,2)
            
        elif mouseX > elements[0]+200 and mouseX < elements[0]+280 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(fire,elements[0]+200,elements[1+num],80,80)
            if mousePressed==True:
                Elements(3,num)
                playerElement(num,3)
            
        elif mouseX > elements[0]+300 and mouseX < elements[0]+380 and mouseY>elements[1+num] and mouseY<elements[1+num]+80:
            image(water,elements[0]+300,elements[1+num],80,80)
            if mousePressed==True:
                Elements(4,num)
                playerElement(num,4)
                
        else:
            if num==0:
                Elements(playerelement0,num)
            elif num==1:
                Elements(playerelement1,num)
            elif num==2:
                Elements(playerelement2,num)
            elif num==3:
                Elements(playerelement3,num)
                
    
# Esmaiel
def Elements(num1,num2):
    if num1==0:
        image(natureG,elements[0],elements[1+num2],80,80)
        image(earthG,elements[0] + 100,elements[1+num2],80,80)
        image(fireG,elements[0] + 200,elements[1+num2],80,80)
        image(waterG,elements[0] + 300,elements[1+num2],80,80)
    elif num1==1:
        image(nature,elements[0],elements[1+num2],80,80)
        image(earthG,elements[0] + 100,elements[1+num2],80,80)
        image(fireG,elements[0] + 200,elements[1+num2],80,80)
        image(waterG,elements[0] + 300,elements[1+num2],80,80)
    elif num1==2:
        image(natureG,elements[0],elements[1+num2],80,80)
        image(earth,elements[0] + 100,elements[1+num2],80,80)
        image(fireG,elements[0] + 200,elements[1+num2],80,80)
        image(waterG,elements[0] + 300,elements[1+num2],80,80)
    elif num1==3:
        image(natureG,elements[0],elements[1+num2],80,80)
        image(earthG,elements[0] + 100,elements[1+num2],80,80)
        image(fire,elements[0] + 200,elements[1+num2],80,80)
        image(waterG,elements[0] + 300,elements[1+num2],80,80)
    elif num1==4:
        image(natureG,elements[0],elements[1+num2],80,80)
        image(earthG,elements[0] + 100,elements[1+num2],80,80)
        image(fireG,elements[0] + 200,elements[1+num2],80,80)
        image(water,elements[0] + 300,elements[1+num2],80,80)
        
def variables(num):
    global choose0,change0,choose1,change1,choose2,change2,choose3,change3
    if num==0:
        choose0=False
        change0=True
    elif num==1:
        choose1=False
        change1=True
    elif num==2:
        choose2=False
        change2=True
    elif num==3:
        choose3=False
        change3=True

        
def playerElement(num1,num2):
    global playerelement0,playerelement1,playerelement2,playerelement3
    if num1==0:
        playerelement0=num2
    elif num1==1:
        playerelement1=num2
    elif num1==2:
        playerelement2=num2
    elif num1==3:
        playerelement3=num2
        
        
        
def RPSgame(num):
    global img,font,RPS,buttons,scissors,rock,paper,player_2,player_1,player1,player2, buttoncounter,gamescreen

    if buttons==True:
        if Button[0+num] < mouseX < Button[0+num] + 320 and Button[3+num] < mouseY < Button[3+num] + 100 and mousePressed:
            if num==0 or num==1:
                fill(40)
                buttons=False
                player_1=True
                player_2=False

            elif num==2:
                background(dkimg)
                RPS=False
                buttoncounter=0
                gamescreen=True
                return
        elif Button[0+num] < mouseX < Button[0+num] + 320 and Button[3+num] < mouseY < Button[3+num] +100:
            fill(200)
        else:
            fill(80)
        rect(Button[0+num], Button[3+num], 320, 100, 10) 
        fill(255)
        textFont(font)
        text(texts[num],Button[0+num]+160,Button[3+num]+70)
        textAlign(CENTER)
    if player_1==True and player_2==False:
        player1=Rps(1)
    if player_2==True and player_1==False:
        player2=Rps(2)
        
    if player_2==False and player_1==False and buttons==False:
        if player1 == player2:
            background(dkimg)
            result()
            text("Draw!",1000,150)
            buttoncounter=1    

        elif player1 == 'Rock' and player2 == 'Paper' or player1 == 'Paper' and player2 == 'Scissors' or player1 == 'Scissors' and player2 == 'Rock':
            background(dkimg)
            result()
            text("Player 2 won!",1000,150)
            buttoncounter=2

        elif player1 == 'Rock' and player2 == 'Scissors' or player1 == 'Paper' and player2 == 'Rock' or player1 == 'Scissors' and player2 == 'Paper':
            background(dkimg)
            result()
            text("Player 1 won!",1000,150)
            buttoncounter=2

        buttons=True
        player_1=False
        player_2=False

        RPSgame(buttoncounter)
    
def Rps(num):
    global player_2,player_1
    background(dkimg)
    text('Player '+str(num),playertext[-1+num],playertext[2])
    image(rock,rps[-1+num],rps[0])
    image(paper,rps[-1+num],rps[2])
    image(scissors,rps[-1+num],rps[3])
    if mouseX > rps[-1+num] and mouseX < rps[-1+num]+200 and mouseY>rps[0] and mouseY<rps[0]+160 :
        image(rock1,rps[-1+num],rps[0]) 
        if mousePressed==True:
            next(num)
            return 'Rock' 
    elif mouseX > rps[-1+num] and mouseX < rps[-1+num]+200 and mouseY>rps[2] and mouseY<rps[2]+160 :
        image(paper1,rps[-1+num],rps[2]) 
        if mousePressed==True:
            next(num)
            return 'Paper' 
    elif mouseX > rps[-1+num] and mouseX < rps[-1+num]+200 and mouseY>rps[3] and mouseY<rps[3]+160 :
        image(scissors1,rps[-1+num],rps[3]) 
        if mousePressed==True:
            next(num)
            return 'Scissors'

def next(num):
    global player_2,player_1
    if num==1:
        player_1=False
        player_2=True    
    if num==2:
        player_1=False
        player_2=False

def result():
    if player1=='Rock':
        image(rock1,rps[0],rps[0]) 
    elif player1=='Paper':
        image(paper1,rps[0],rps[2]) 
    elif player1=='Scissors':
        image(scissors1,rps[0],rps[3])
    if player2=='Rock':
        image(rock1,rps[1],rps[0]) 
    elif player2=='Paper':
        image(paper1,rps[1],rps[2]) 
    elif player2=='Scissors':
        image(scissors1,rps[1],rps[3])
