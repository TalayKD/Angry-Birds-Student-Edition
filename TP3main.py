from cmu_112_graphics import *
import math
from Bird import *
from Pig import *
from Block import *
from Levels import *

#this is the main file that contains all the splash screen modes and runs the animations + math behind the game dynamics

##########################################
# Home Page Mode
##########################################

def homePageMode_redrawAll(app, canvas):
    canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.homebackground), 
                        anchor = "nw")
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.playButton))
    canvas.create_image(app.width-20, app.height-20, 
                image=ImageTk.PhotoImage(app.instructionsButton), anchor = "se")

def homePageMode_mousePressed(app, event):
    #changes mode if player clicks on play or instructions button
    mouseX = event.x
    mouseY = event.y
    instructions = (1221, 660)
    instrButtonRadius = 31
    if (564 <= mouseX <= 713 and 364 <= mouseY <= 435):
        app.mode = 'gameSelectionMode'
    if (distance(mouseX, mouseY, instructions[0], instructions[1]) <= instrButtonRadius):
        app.mode = 'instructionsMode'


##########################################
# Instructions Page Mode
##########################################

def instructionsMode_redrawAll(app, canvas):
    canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.background), 
                        anchor = "nw")
    canvas.create_image(app.width-20, app.height-20, 
                image=ImageTk.PhotoImage(app.backToHomeButton), anchor = "se")
    canvas.create_image(app.width/2, 90, image=ImageTk.PhotoImage(app.howToPlayText))
    canvas.create_image(app.width * (1.3/4), 180, image=ImageTk.PhotoImage(app.instr1))
    canvas.create_image(app.width * (2.66/4), 180, image=ImageTk.PhotoImage(app.instr15))
    canvas.create_image(app.width/2, 220, image=ImageTk.PhotoImage(app.instr2))
    canvas.create_image(app.width * (1.3/4), 270, image=ImageTk.PhotoImage(app.redImage))
    canvas.create_image(app.width * (2/4), 270, image=ImageTk.PhotoImage(app.redDes))
    canvas.create_image(app.width * (1.15/4), 320, image=ImageTk.PhotoImage(app.bigRedImage))
    canvas.create_image(app.width * (2/4), 320, image=ImageTk.PhotoImage(app.bigRedDes))
    canvas.create_image(app.width * (2/4), 380, image=ImageTk.PhotoImage(app.instr3))
    canvas.create_image(app.width * (1.35/4), 430, image=ImageTk.PhotoImage(app.yellowImage))
    canvas.create_image(app.width * (2/4), 430, image=ImageTk.PhotoImage(app.yellowDes))
    canvas.create_image(app.width * (1.26/4), 490, image=ImageTk.PhotoImage(app.boomerangImage))
    canvas.create_image(app.width * (2/4), 490, image=ImageTk.PhotoImage(app.boomDes))
    canvas.create_image(app.width * (1.305/4), 550, image=ImageTk.PhotoImage(app.matildaImage))
    canvas.create_image(app.width * (2/4), 550, image=ImageTk.PhotoImage(app.matildaDes))
    
def instructionsMode_mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    home = (1221, 660)
    homeButtonRadius = 31
    #back to home page
    if (distance(mouseX, mouseY, home[0], home[1]) <= homeButtonRadius):
        app.mode = 'homePageMode'


##########################################
# Game Selection Mode
##########################################

def gameSelectionMode_redrawAll(app, canvas):
    canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.background), 
                        anchor = "nw")
    canvas.create_image(app.width/2, 90, image=ImageTk.PhotoImage(app.gameModeText))
    canvas.create_image(app.width * (1.5/5), app.height/2, image=ImageTk.PhotoImage(app.normalModeImage))
    canvas.create_image(app.width * (3.5/5), app.height/2, image=ImageTk.PhotoImage(app.zeroGravityModeImage))
    canvas.create_image(app.width * (1.5/5), app.height * (7/10) + 10, image=ImageTk.PhotoImage(app.normalModeText))
    canvas.create_image(app.width * (3.5/5), app.height * (7/10) + 10, image=ImageTk.PhotoImage(app.zeroModeText))
    canvas.create_image(app.width * (3.5/5), app.height * (8/10) - 5, image=ImageTk.PhotoImage(app.gravityModeText))
    canvas.create_image(app.width-20, app.height-20, 
                image=ImageTk.PhotoImage(app.backToHomeButton), anchor = "se")

def gameSelectionMode_mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    home = (1221, 660)
    homeButtonRadius = 31
    #normal mode
    if (224 <= mouseX <= 544 and 244 <= mouseY <= 476):
        app.mode = 'normalLevelSelectionMode'
    #no gravity mode
    if (736 <= mouseX <= 1056 and 244 <= mouseY <= 476):
        app.mode = 'noGravLevelSelectionMode'
    #back to home page
    if (distance(mouseX, mouseY, home[0], home[1]) <= homeButtonRadius):
        app.mode = 'homePageMode'


##########################################
# Normal Level Selection Mode
##########################################

def normalLevelSelectionMode_redrawAll(app, canvas):
    canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.background), 
                        anchor = "nw")
    #dimensions of level image
    halfLength = 128
    halfWidth = 72
    #showing map of each level during level selection mode
    halfWidthText = 30
    canvas.create_image(app.width/2, 90, image=ImageTk.PhotoImage(app.normalBigText))
    canvas.create_image(app.width * (1/5), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level1Map))
    canvas.create_image(app.width * (1/2), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level2Map))
    canvas.create_image(app.width * (4/5), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level3Map))
    canvas.create_image(app.width * (1/5), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level4Map))
    canvas.create_image(app.width * (1/2), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level5Map))
    canvas.create_image(app.width * (4/5), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level6Map))
    #level text display
    canvas.create_image(app.width * (1/5), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level1Text))
    canvas.create_image(app.width * (1/2), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level2Text))
    canvas.create_image(app.width * (4/5), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level3Text))
    canvas.create_image(app.width * (1/5), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level4Text))
    canvas.create_image(app.width * (1/2), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level5Text))
    canvas.create_image(app.width * (4/5), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level6Text))
    canvas.create_image(app.width-20, app.height-20, 
                image=ImageTk.PhotoImage(app.backToModeButton), anchor = "se")

def normalLevelSelectionMode_mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    halfLength = 128
    halfWidth = 72
    modeButton = (1221, 660)
    modeButtonRadius = 31
    if (app.width * (1/5) - halfLength <= mouseX <= app.width * (1/5) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 1
        startLevel(app)
        app.mode = 'gameMode'
    if (app.width * (1/2) - halfLength <= mouseX <= app.width * (1/2) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 2
        startLevel(app)
        app.mode = 'gameMode'
    if (app.width * (4/5) - halfLength <= mouseX <= app.width * (4/5) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 3
        startLevel(app)
        app.mode = 'gameMode'
    if (app.width * (1/5) - halfLength <= mouseX <= app.width * (1/5) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 4
        startLevel(app)
        app.mode = 'gameMode'
    if (app.width * (1/2) - halfLength <= mouseX <= app.width * (1/2) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 5
        startLevel(app)
        app.mode = 'gameMode'
    if (app.width * (4/5) - halfLength <= mouseX <= app.width * (4/5) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 6
        startLevel(app)
        app.mode = 'gameMode'
    if (distance(mouseX, mouseY, modeButton[0], modeButton[1]) <= modeButtonRadius):
        app.mode = 'gameSelectionMode'
    

##########################################
# No Gravity Level Selection Mode
##########################################

def noGravLevelSelectionMode_redrawAll(app, canvas):
    canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.spacebackground), 
                        anchor = "nw")
    #dimensions of level image
    halfLength = 128
    halfWidth = 72
    #showing map of each level during level selection mode
    halfWidthText = 30
    canvas.create_image(app.width/2, 90, image=ImageTk.PhotoImage(app.zeroGravityText))
    canvas.create_image(app.width * (1/5), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level1NoGravMap))
    canvas.create_image(app.width * (1/2), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level2NoGravMap))
    canvas.create_image(app.width * (4/5), app.height * (1.75/5), image=ImageTk.PhotoImage(app.level3NoGravMap))
    canvas.create_image(app.width * (1/5), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level4NoGravMap))
    canvas.create_image(app.width * (1/2), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level5NoGravMap))
    canvas.create_image(app.width * (4/5), app.height * (3.4/5), image=ImageTk.PhotoImage(app.level6NoGravMap))
    #level text display
    canvas.create_image(app.width * (1/5), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level1Text))
    canvas.create_image(app.width * (1/2), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level2Text))
    canvas.create_image(app.width * (4/5), app.height * (1.75/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level3Text))
    canvas.create_image(app.width * (1/5), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level4Text))
    canvas.create_image(app.width * (1/2), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level5Text))
    canvas.create_image(app.width * (4/5), app.height * (3.4/5) + halfWidth + halfWidthText, image=ImageTk.PhotoImage(app.level6Text))
    canvas.create_image(app.width-20, app.height-20, 
                image=ImageTk.PhotoImage(app.backToModeButton), anchor = "se")

def noGravLevelSelectionMode_mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    halfLength = 128
    halfWidth = 72
    modeButton = (1221, 660)
    modeButtonRadius = 31
    if (app.width * (1/5) - halfLength <= mouseX <= app.width * (1/5) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 1
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (app.width * (1/2) - halfLength <= mouseX <= app.width * (1/2) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 2
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (app.width * (4/5) - halfLength <= mouseX <= app.width * (4/5) + halfLength and
        app.height * (1.75/5) - halfWidth <= mouseY <= app.height * (1.75/5) + halfWidth):
        app.level = 3
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (app.width * (1/5) - halfLength <= mouseX <= app.width * (1/5) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 4
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (app.width * (1/2) - halfLength <= mouseX <= app.width * (1/2) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 5
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (app.width * (4/5) - halfLength <= mouseX <= app.width * (4/5) + halfLength and
        app.height * (3.4/5) - halfWidth <= mouseY <= app.height * (3.4/5) + halfWidth):
        app.level = 6
        startLevelNoGrav(app)
        app.mode = 'gameMode'
    if (distance(mouseX, mouseY, modeButton[0], modeButton[1]) <= modeButtonRadius):
        app.mode = 'gameSelectionMode'


##########################################
# Game Mode
##########################################

def gameMode_mouseReleased(app, event):
    if (app.playingBird.dragBird):
        app.playingBird.launchProjectile(event.x, event.y, app.slingstartcx, app.slingstartcy, app.slingK)
        app.playingBird.drawSling = False
        
def gameMode_mouseMoved(app, event):
    if ((app.playingBird.x-app.playingBird.radius <= event.x <= app.playingBird.x+app.playingBird.radius) and 
        (app.playingBird.y-app.playingBird.radius <= event.y <= app.playingBird.y+app.playingBird.radius)):
        app.playingBird.dragBird = True
    else:
        app.playingBird.dragBird = False

def gameMode_mouseDragged(app, event):
    if (app.playingBird.dragBird):
        app.playingBird.x = event.x
        app.playingBird.y = event.y

def gameMode_keyPressed(app, event):
    #allows birds with special abilities to use their powers when space is pressed
    if (event.key == 'Space'):
        if (isinstance(app.playingBird, MatildaBird)):
            if (app.playingBird.usedPower == False):
                app.egg = app.playingBird.usePower()
                app.characters.append(app.egg)
        else:
            app.playingBird.usePower()

def gameMode_mousePressed(app, event):
    pause = (47, 47)
    buttonRadius = 36
    if (distance(event.x, event.y, pause[0], pause[1]) <= buttonRadius):
        app.mode = 'pauseMode'

def gameMode_timerFired(app):
    deadChar = []
    for char in app.characters:
        char.move()
        if (char.alive == False):
            deadChar.append(char)
    for i in range(len(app.characters)):
        for j in range(len(app.characters)):
            if(app.characters[i].name != app.characters[j].name):
                collide(app.characters[i], app.characters[j])
    eliminateDeadChar(app, deadChar)
    changePlayingBird(app)
    checkGameOver(app)

def gameMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawBackSling(app, canvas)
    drawBackSlingShot(app, canvas)
    drawBird(app, canvas)
    drawFrontSling(app, canvas)
    drawFrontSlingShot(app, canvas)
    drawPig(app, canvas)
    drawEgg(app, canvas)
    drawBlock(app, canvas)
    drawPauseButton(app, canvas)


##########################################
# Pause Mode
##########################################

def pauseMode_mousePressed(app, event):
    continueButton = (47, 47)
    replay = (47, 137)
    menu = (47, 227)
    buttonRadius = 36
    if (distance(event.x, event.y, continueButton[0], continueButton[1]) <= buttonRadius):
        app.mode = 'gameMode'
    if (distance(event.x, event.y, replay[0], replay[1]) <= buttonRadius):
        if (app.noGravity):
            startLevelNoGrav(app)
            app.mode = 'gameMode'
        else:
            startLevel(app)
            app.mode = 'gameMode'
    if (distance(event.x, event.y, menu[0], menu[1]) <= buttonRadius):
        if (app.noGravity):
            app.mode = 'noGravLevelSelectionMode'
        else:
            app.mode = 'normalLevelSelectionMode'

def pauseMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawBackSling(app, canvas)
    drawBackSlingShot(app, canvas)
    drawBird(app, canvas)
    drawFrontSling(app, canvas)
    drawFrontSlingShot(app, canvas)
    drawPig(app, canvas)
    drawEgg(app, canvas)
    drawBlock(app, canvas)
    drawContinueButton(app, canvas)
    drawReplayButton(app, canvas)
    drawMenuButton(app, canvas)


##########################################
# Game Over Mode
##########################################

def gameOverMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawBackSling(app, canvas)
    drawBackSlingShot(app, canvas)
    drawBird(app, canvas)
    drawFrontSling(app, canvas)
    drawFrontSlingShot(app, canvas)
    drawPig(app, canvas)
    drawEgg(app, canvas)
    drawBlock(app, canvas)
    drawGameOver(app, canvas)
    drawPauseButton(app, canvas)

def gameOverMode_mousePressed(app, event):
    buttonRadius = 53
    category = (561, 539)
    replay = (721, 540)
    if (distance(event.x, event.y, category[0], category[1]) <= buttonRadius):
        if (app.noGravity):
            app.mode = 'noGravLevelSelectionMode'
        else:
            app.mode = 'normalLevelSelectionMode'
    elif (distance(event.x, event.y, replay[0], replay[1]) <= buttonRadius):
        if (app.noGravity):
            startLevelNoGrav(app)
        else:
            startLevel(app)
        app.mode = 'gameMode'


##########################################
# Main App
##########################################

def appStarted(app):
    #load images
    #background image taken from https://wallpaper-house.com/wallpaper-id-226435.php
    app.background = app.loadImage('background.jpeg')
    #space background image taken from https://www.angrybirdsnest.com/forums/topic/angry-birds-seasons-backgrounds/
    app.spacebackground = app.loadImage('spaceBackground.png')
    app.homebackground = app.loadImage('homebackground.jpeg')
    #button images taken from https://angrybirds.fandom.com/wiki/Special:Search?scope=internal&query=buttons&ns%5B0%5D=6
    app.playButton = app.loadImage('playButton.png')
    app.instructionsButton = app.loadImage('instructionsIcon.png')
    app.backToModeButton = app.loadImage('backToMode.png')
    app.backToHomeButton = app.loadImage('backToHome.png')
    #pause, continue, replay, and menu button taken from https://angrybirds.fandom.com/wiki/Angry_Birds_(game)/Gallery?file=BUTTONS_SHEET_1_1_%2528Classic%2529.png#Sprites
    app.pauseButton = app.loadImage('pause.png')
    app.replayButton = app.loadImage('replayButton.png')
    app.continueButton = app.loadImage('continueButton.png')
    app.menuButton = app.loadImage('menuButton.png')
    #Angry Birds themed fonts created by https://fontmeme.com/angry-birds-font/
    app.gameModeText = app.loadImage('gameModeText.png')
    app.normalModeText = app.loadImage('normalText.png')
    app.normalBigText = app.loadImage('normalBigText.png')
    app.zeroModeText = app.loadImage('zero.png')
    app.gravityModeText = app.loadImage('gravity.png')
    app.zeroGravityText = app.loadImage('zerograv.png')
    app.level1Text = app.loadImage('level1.png')
    app.level2Text = app.loadImage('level2.png')
    app.level3Text = app.loadImage('level3.png')
    app.level4Text = app.loadImage('level4.png')
    app.level5Text = app.loadImage('level5.png')
    app.level6Text = app.loadImage('level6.png')
    app.howToPlayText = app.loadImage('how2play.png')
    app.instr1 = app.loadImage('instr1.png')
    app.instr15 = app.loadImage('instr1.5.png')
    app.instr2 = app.loadImage('instr2.png')
    app.redDes = app.loadImage('redDes.png')
    app.instr3 = app.loadImage('instr3.png')
    app.yellowDes = app.loadImage('yellowDes.png')
    app.bigRedDes = app.loadImage('bigRedDes.png')
    app.boomDes = app.loadImage('boomDes.png')
    app.matildaDes = app.loadImage('matildaDes.png')
    #map images
    #border added using https://www3.lunapic.com/editor/
    app.level1Map = app.loadImage('level1Map.png')
    app.level2Map = app.loadImage('level2Map.png')
    app.level3Map = app.loadImage('level3Map.png')
    app.level4Map = app.loadImage('level4Map.png')
    app.level5Map = app.loadImage('level5Map.png')
    app.level6Map = app.loadImage('level6Map.png')
    app.level1NoGravMap = app.loadImage('level1NoGravMap.png')
    app.level2NoGravMap = app.loadImage('level2NoGravMap.png')
    app.level3NoGravMap = app.loadImage('level3NoGravMap.png')
    app.level4NoGravMap = app.loadImage('level4NoGravMap.png')
    app.level5NoGravMap = app.loadImage('level5NoGravMap.png')
    app.level6NoGravMap = app.loadImage('level6NoGravMap.png')
    #normal mode theme image taken from https://wallpapersafari.com/w/RmGx9O
    app.normalModeImage = app.loadImage('normal.png')
    #zero gravity mode theme image taken from https://angrybirds.fandom.com/wiki/Angry_Birds_Wiki?file=Angry+Birds+SpaceComic2.jpg
    app.zeroGravityModeImage = app.loadImage('nogravity.png')
    #screen showing level cleared / failed images from https://angrybirds.fandom.com/wiki/Level_Cleared
    #and https://angrybirds.fandom.com/wiki/Level_Failed
    #cropped some star images from https://www.youtube.com/watch?v=ga-eHR1GVyA
    #used preview cropping tool to combine and edit some images
    app.loseImage = app.loadImage('GameOverLose.png')
    app.won1StarImage = app.loadImage('Won1Star.png')
    app.won2StarsImage = app.loadImage('Won2Stars.png')
    app.won3StarsImage = app.loadImage('Won3Stars.png')
    app.gameOverIcon = app.loadImage('gameOverIcons.png')
    #slingshot image taken from https://www.pnglib.com/slingshot-clipart/
    app.slingshotImage = app.loadImage('slingshot.png')
    app.slingshotImage2 = app.loadImage('sling2.png')
    #bird images taken from https://angrybirds.fandom.com/wiki/Angry_Birds_(game)/Gallery#Images
    app.redImage = app.loadImage('red.png')
    app.yellowImage = app.loadImage('yellow.png')
    app.bigRedImage = app.loadImage('bigRed.png')
    app.boomerangImage = app.loadImage('BoomerangBird.png')
    app.matildaImage = app.loadImage('matilda.png')
    app.eggImage = app.loadImage('egg.png')
    #minion pig images taken from https://angrybirds.fandom.com/wiki/Special:Search?scope=internal&query=pig&ns%5B0%5D=6&filter=imageOnly
    app.pigImage = app.loadImage('pig.png')
    app.pigImageHurt1 = app.loadImage('pigdie1.png')
    app.pigImageHurt2 = app.loadImage('pigdie2.png')
    #wooden block images taken from https://angrybirds.fandom.com/wiki/Blocks?file=INGAME_BLOCKS_WOOD_1.png
    app.woodenBlockImage = app.loadImage('woodblock.png')
    app.woodenBlockImageHurt1 = app.loadImage('woodblockHurt1.png')
    app.woodenBlockImageHurt2 = app.loadImage('woodblockHurt2.png')
    app.woodenBlockSmallImage = app.loadImage('woodblocksmall.png')
    app.woodenBlockSmallImageHurt1 = app.loadImage('woodblockHurt1small.png')
    app.woodenBlockSmallImageHurt2 = app.loadImage('woodblockHurt2small.png')
    #glass block images taken from https://angrybirds.fandom.com/wiki/Blocks?file=Glass_Block_Sheet.png
    app.glassBlockImage = app.loadImage('glassblock.png')
    app.glassBlockImageHurt1 = app.loadImage('glassblockhurt1.png')
    app.glassBlockImageHurt2 = app.loadImage('glassblockhurt2.png')
    #stone block images taken from https://angrybirds.fandom.com/wiki/Blocks?file=INGAME_BLOCKS_STONE_1.png
    app.stoneBlockImage = app.loadImage('stoneblock.png')
    app.stoneBlockImageHurt1 = app.loadImage('stoneblockhurt1.png')
    app.stoneBlockImageHurt2 = app.loadImage('stoneblockhurt2.png')

    #initialize values
    
    #coordinates of the center of the slingshot image
    app.slingshotcx = 220
    app.slingshotcy = 560
    #coordinates of the release point of the slingshot
    app.slingstartcx = app.slingshotcx - 9
    app.slingstartcy = app.slingshotcy - 40
    app.slingdrawx1 = app.slingstartcx - 12
    app.slingdrawx2 = app.slingstartcx + 12
    app.slingdrawy = app.slingstartcy
    app.slingK = 0.5

    app.level = 1
    app.timerDelay = 1
    app.mode = 'homePageMode'

def checkGameOver(app):
    if (app.pigs == []):
        app.score = len(app.birds)
        app.gameOverWin = True
        app.mode = 'gameOverMode'

def eliminateDeadChar(app, deadChar):
    for x in range(len(deadChar)):
        app.characters.remove(deadChar[x])
        if(isinstance(deadChar[x], Pig)):
            app.pigs.remove(deadChar[x])
        elif(isinstance(deadChar[x], Block)):
            app.blocks.remove(deadChar[x])

def changePlayingBird(app):
    if ((app.playingBird.played and app.playingBird.dx == 0 and app.playingBird.dy == 0) or
        (app.playingBird.x > 1280 or app.playingBird.x < 0 or app.playingBird.y > 720 or app.playingBird.y < 0) or 
        (app.playingBird.collided and math.sqrt(app.playingBird.dx ** 2 + app.playingBird.dy ** 2) <= 3)):
        if(len(app.birds) > 0):
            app.characters.remove(app.playingBird)
            app.playingBird = app.birds.pop(0)
            app.playingBird.x = app.slingstartcx
            app.playingBird.y = app.slingstartcy
            app.characters.insert(0, app.playingBird)
        else:
            if(app.pigs == [] and app.playingBird.played):
                app.gameOverWin = True
                app.mode = 'gameOverMode'
            elif(app.playingBird.played):
                app.gameOverLose = True
                app.mode = 'gameOverMode'

#returns the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#initializes the value for that level and starts it
def startLevel(app):
    if (app.level == 1):
        initLevel1(app)
    elif (app.level == 2):
        initLevel2(app)
    elif (app.level == 3):
        initLevel3(app)
    elif (app.level == 4):
        initLevel4(app)
    elif (app.level == 5):
        initLevel5(app)
    elif (app.level == 6):
        initLevel6(app)
    
def startLevelNoGrav(app):
    if (app.level == 1):
        initLevel1NoGrav(app)
    elif (app.level == 2):
        initLevel2NoGrav(app)
    elif (app.level == 3):
        initLevel3NoGrav(app)
    elif (app.level == 4):
        initLevel4NoGrav(app)
    elif (app.level == 5):
        initLevel5NoGrav(app)
    elif (app.level == 6):
        initLevel6NoGrav(app)

#draws the pause button
def drawPauseButton(app, canvas):
    canvas.create_image(10, 10, image=ImageTk.PhotoImage(app.pauseButton), anchor = 'nw')

#draws the continue button
def drawContinueButton(app, canvas):
    canvas.create_image(10, 10, image=ImageTk.PhotoImage(app.continueButton), anchor = 'nw')

#draws the replay button
def drawReplayButton(app, canvas):
    canvas.create_image(10, 100, image=ImageTk.PhotoImage(app.replayButton), anchor = 'nw')

#draws the menu button
def drawMenuButton(app, canvas):
    canvas.create_image(10, 190, image=ImageTk.PhotoImage(app.menuButton), anchor = 'nw')

#draws the background image
def drawBackground(app, canvas):
    if (app.noGravity):
        canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.spacebackground), 
                        anchor = "nw")
    else:
        canvas.create_image(0, 0, image=ImageTk.PhotoImage(app.background), 
                        anchor = "nw")

#draws the Red Angry Bird
def drawBird(app, canvas):
    for bird in app.birds:
        if (isinstance(bird, YellowBird)):
            canvas.create_image(bird.x, bird.y, image=ImageTk.PhotoImage(app.yellowImage))
        elif (isinstance(bird, BigRedBird)):
            canvas.create_image(bird.x, bird.y, image=ImageTk.PhotoImage(app.bigRedImage))
        elif (isinstance(bird, BoomerangBird)):
            canvas.create_image(bird.x, bird.y, image=ImageTk.PhotoImage(app.boomerangImage))
        elif (isinstance(bird, MatildaBird)):
            canvas.create_image(bird.x, bird.y, image=ImageTk.PhotoImage(app.matildaImage))
        else:
            canvas.create_image(bird.x, bird.y, image=ImageTk.PhotoImage(app.redImage))
    if (isinstance(app.playingBird, YellowBird)):
        canvas.create_image(app.playingBird.x, app.playingBird.y, image=ImageTk.PhotoImage(app.yellowImage))
    elif (isinstance(app.playingBird, BigRedBird)):
        canvas.create_image(app.playingBird.x, app.playingBird.y, image=ImageTk.PhotoImage(app.bigRedImage))
    elif (isinstance(app.playingBird, BoomerangBird)):
        canvas.create_image(app.playingBird.x, app.playingBird.y, image=ImageTk.PhotoImage(app.boomerangImage))
    elif (isinstance(app.playingBird, MatildaBird)):
        canvas.create_image(app.playingBird.x, app.playingBird.y, image=ImageTk.PhotoImage(app.matildaImage))
    else:
        canvas.create_image(app.playingBird.x, app.playingBird.y, image=ImageTk.PhotoImage(app.redImage))

def drawPig(app, canvas):
    for pig in app.pigs:
        if (pig.health >= (pig.fullHealth*(9.8/10))):
            canvas.create_image(pig.x, pig.y, image=ImageTk.PhotoImage(app.pigImage))
        elif (pig.health >= (pig.fullHealth/2)):
            canvas.create_image(pig.x, pig.y, image=ImageTk.PhotoImage(app.pigImageHurt1))
        elif (pig.health >= 0):
            canvas.create_image(pig.x, pig.y, image=ImageTk.PhotoImage(app.pigImageHurt2))

def drawEgg(app, canvas):
    if (app.egg.alive):
            canvas.create_image(app.egg.x, app.egg.y, image=ImageTk.PhotoImage(app.eggImage))

#draws the block
def drawBlock(app, canvas):
    for block in app.blocks:
        if (isinstance(block, GlassBlock)):
            if (block.health >= (block.fullHealth*(9.8/10))):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.glassBlockImage))
            elif (block.health >= (block.fullHealth/2)):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.glassBlockImageHurt1))
            elif (block.health >= 0):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.glassBlockImageHurt2))
        elif (isinstance(block, StoneBlock)):
            if (block.health >= (block.fullHealth*(9.8/10))):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.stoneBlockImage))
            elif (block.health >= (block.fullHealth/2)):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.stoneBlockImageHurt1))
            elif (block.health >= 0):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.stoneBlockImageHurt2))
        elif (isinstance(block, SmallBlock)):
            if (block.health >= (block.fullHealth*(9.8/10))):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockSmallImage))
            elif (block.health >= (block.fullHealth/2)):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockSmallImageHurt1))
            elif (block.health >= 0):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockSmallImageHurt2))
        else:
            if (block.health >= (block.fullHealth*(9.8/10))):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockImage))
            elif (block.health >= (block.fullHealth/2)):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockImageHurt1))
            elif (block.health >= 0):
                canvas.create_image(block.x, block.y, image=ImageTk.PhotoImage(app.woodenBlockImageHurt2))

#draws the sling (behind the bird)
def drawBackSling(app, canvas):
    if (app.playingBird.drawSling):
        if (isinstance(app.playingBird, BoomerangBird)):
            canvas.create_line(app.slingdrawx2, app.slingdrawy, app.playingBird.x-app.playingBird.radius, app.playingBird.y+app.playingBird.radius-12,
                        width = 4, fill = 'saddlebrown')
        elif (isinstance(app.playingBird, MatildaBird)):
            canvas.create_line(app.slingdrawx2, app.slingdrawy, app.playingBird.x-app.playingBird.radius+11, app.playingBird.y+app.playingBird.radius-14,
                        width = 4, fill = 'saddlebrown')
        else:
            canvas.create_line(app.slingdrawx2, app.slingdrawy, app.playingBird.x-app.playingBird.radius+7, app.playingBird.y+app.playingBird.radius-14,
                        width = 4, fill = 'saddlebrown')

#draws the slingshot (behind view)
def drawBackSlingShot(app, canvas):
    canvas.create_image(app.slingshotcx, app.slingshotcy, image=ImageTk.PhotoImage(app.slingshotImage))

#draws the sling (in front of the bird)
def drawFrontSling(app, canvas):
    if (app.playingBird.drawSling):
        if (isinstance(app.playingBird, BoomerangBird)):
            canvas.create_line(app.slingdrawx1, app.slingdrawy, app.playingBird.x-app.playingBird.radius, app.playingBird.y+app.playingBird.radius-12,
                        width = 4, fill = 'saddlebrown')
        elif (isinstance(app.playingBird, MatildaBird)):
            canvas.create_line(app.slingdrawx1, app.slingdrawy, app.playingBird.x-app.playingBird.radius+11, app.playingBird.y+app.playingBird.radius-14,
                        width = 4, fill = 'saddlebrown')
        else:
            canvas.create_line(app.slingdrawx1, app.slingdrawy, app.playingBird.x-app.playingBird.radius+7, app.playingBird.y+app.playingBird.radius-14,
                        width = 4, fill = 'saddlebrown')

#draws the slingshot (front view)
def drawFrontSlingShot(app, canvas):
    canvas.create_image(app.slingshotcx-13, app.slingshotcy, image=ImageTk.PhotoImage(app.slingshotImage2))

#draws endgame image
def drawGameOver(app, canvas):
    if (app.gameOverLose):
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.loseImage))
    else:
        #3 stars
        if (app.score >= int(app.initialScore/2)):
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.won3StarsImage))
        elif (app.score >= int(app.initialScore/4)):
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.won2StarsImage))
        else:
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.won1StarImage))
    canvas.create_image(app.width/2, app.height * (3/4), image=ImageTk.PhotoImage(app.gameOverIcon))

#checks whether two objects collide
#if they do:
#   change the x and y component of each objects' velocity due to the law of conservation of momentum
#   subtract their health
#   change alive variable to False if their health is below 0
def collide(self, other):
    otherTop, otherBot, otherLeft, otherRight = other.getBounds()
    top, bot, left, right = self.getBounds()
    #checks for collisions from right
    #second condition inside first parenthesis prevents objects from overlapping
    #if statement conditions for left, right, up, and down collisions inspired by https://github.com/ianzh68/AngryBirds/blob/master/tp3/classes.py
    if (((otherLeft <= right <= otherLeft + other.radius) or (otherLeft <= self.x < otherLeft + other.radius))
        and (otherTop <= self.y <= otherBot)):
        #subtract health of characters from collision
        if (abs(other.dx) > 12 or abs(other.dy) > 12):
            self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
        if (abs(self.dx) > 12 or abs(self.dy) > 12):
            other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
        #recalculate velocity in x-direction, but velocity in y-direction is kept the same
        newSelfdx = self.getvxf(other)
        newOtherdx = other.getvxf(self)
        self.dx = newSelfdx
        other.dx = newOtherdx
        #this overlap variable is only for colliding objects from below so they stack
        self.overlap = False
        #make sure the object does not overlap
        self.x = otherLeft - self.radius - 1
        #makes object dead if health is below 0
        if (self.health <= 0):
            self.alive = False
        if (other.health <= 0):
            other.alive = False
        #makes bird disappear after hitting and slowing down
        if (isinstance(self, Bird)):
            self.collided = True
        if (isinstance(other, Bird)):
            other.collided = True
    #checks for collisions from left
    if (((otherRight - other.radius <= left <= otherRight) or (otherRight - other.radius < self.x <= otherRight)) 
        and (otherTop <= self.y <= otherBot)):
        #subtract health of characters from collision
        if (abs(other.dx) > 12 or abs(other.dy) > 12):
            self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
        if (abs(self.dx) > 12 or abs(self.dy) > 12):
            other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
        newSelfdx = self.getvxf(other)
        newOtherdx = other.getvxf(self)
        self.dx = newSelfdx
        other.dx = newOtherdx
        self.overlap = False
        self.x = otherRight + self.radius + 1
        #makes object dead if health is below 0
        if (self.health <= 0):
            self.alive = False
        if (other.health <= 0):
            other.alive = False
        #makes bird disappear after hitting and slowing down
        if (isinstance(self, Bird)):
            self.collided = True
        if (isinstance(other, Bird)):
            other.collided = True
    #checks for collisions from top
    if((otherLeft <= self.x <= otherRight) and 
        ((otherBot - other.radius <= top <= otherBot) or (otherBot - other.radius < self.y <= otherBot))):
        #subtract health of characters from collision
        if (abs(other.dx) > 12 or abs(other.dy) > 12):
            self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
        if (abs(self.dx) > 12 or abs(self.dy) > 12):
            other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
        newSelfdy = self.getvyf(other)
        newOtherdy = other.getvyf(self)
        self.dy = newSelfdy
        other.dy = newOtherdy
        self.overlap = False
        self.y = otherBot + self.radius + 1
        #makes object dead if health is below 0
        if (self.health <= 0):
            self.alive = False
        if (other.health <= 0):
            other.alive = False
        #makes bird disappear after hitting and slowing down
        if (isinstance(self, Bird)):
            self.collided = True
        if (isinstance(other, Bird)):
            other.collided = True
    #checks for collisions from bottom
    if((otherLeft <= self.x <= otherRight) and 
        ((otherTop <= bot <= otherTop + other.radius) or (otherTop <= self.y < otherTop + other.radius))):
        #subtract health of characters from collision
        if (abs(other.dx) > 12 or abs(other.dy) > 12):
            self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
        if (abs(self.dx) > 12 or abs(self.dy) > 12):
            other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
        #might have to make dy zero here to make objects stack
        self.dy = int(self.dy)
        other.dy = int(other.dy)
        newSelfdy = self.getvyf(other)
        newOtherdy = other.getvyf(self)
        self.dy = newSelfdy
        other.dy = newOtherdy
        self.overlap = True
        self.y = otherTop - self.radius - 1
        #prevents objects from bouncing on each other
        if (abs(self.dy) <= 5):
            self.dy = 0
        #makes object dead if health is below 0
        if (self.health <= 0):
            self.alive = False
        if (other.health <= 0):
            other.alive = False
        #makes bird disappear after hitting and slowing down
        if (isinstance(self, Bird)):
            self.collided = True
        if (isinstance(other, Bird)):
            other.collided = True
    #checks for collisions from bot-right
    #if statement conditions for diagonal collisions inspired by https://github.com/ianzh68/AngryBirds/blob/master/tp3/classes.py
    if(self.x <= otherLeft and self.y <= otherTop):
        dis = self.distance(self.x, self.y, otherLeft, otherTop)
        #coordinates for bottom right of self
        if (dis <= self.radius):
            #subtract health of characters from collision
            if (abs(other.dx) > 12 or abs(other.dy) > 12):
                self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
            if (abs(self.dx) > 12 or abs(self.dy) > 12):
                other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
            newSelfdx = self.getvxf(other)
            newOtherdx = other.getvxf(self)
            newSelfdy = self.getvyf(other)
            newOtherdy = other.getvyf(self)
            self.dx = newSelfdx
            other.dx = newOtherdx
            self.dy = newSelfdy
            other.dy = newOtherdy
            self.overlap = False
            self.x = otherLeft - self.radius - 1
            self.y = otherTop - self.radius - 1
            #prevents objects from bouncing on each other
            if (abs(self.dy) <= 5):
                self.dy = 0
            #makes object dead if health is below 0
            if (self.health <= 0):
                self.alive = False
            if (other.health <= 0):
                other.alive = False
            #makes bird disappear after hitting and slowing down
            if (isinstance(self, Bird)):
                self.collided = True
            if (isinstance(other, Bird)):
                other.collided = True
    #checks collisions from bot-left
    if(self.x >= otherRight and self.y <= otherTop):
        dis = self.distance(self.x, self.y, otherRight, otherTop)
        #coordinates for bottom left of self
        if (dis <= self.radius):
            #subtract health of characters from collision
            if (abs(other.dx) > 12 or abs(other.dy) > 12):
                self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
            if (abs(self.dx) > 12 or abs(self.dy) > 12):
                other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
            newSelfdx = self.getvxf(other)
            newOtherdx = other.getvxf(self)
            newSelfdy = self.getvyf(other)
            newOtherdy = other.getvyf(self)
            self.dx = newSelfdx
            other.dx = newOtherdx
            self.dy = newSelfdy
            other.dy = newOtherdy
            self.overlap = False
            self.x = otherRight + self.radius + 1
            self.y = otherTop - self.radius - 1
            #prevents objects from bouncing on each other
            if (abs(self.dy) <= 5):
                self.dy = 0
            #makes object dead if health is below 0
            if (self.health <= 0):
                self.alive = False
            if (other.health <= 0):
                other.alive = False
            #makes bird disappear after hitting and slowing down
            if (isinstance(self, Bird)):
                self.collided = True
            if (isinstance(other, Bird)):
                other.collided = True
    #checks collisions from top-left
    if(self.x >= otherRight and self.y >= otherBot):
        dis = self.distance(self.x, self.y, otherLeft, otherTop)
        #coordinates for top left of self
        if (dis <= self.radius):
            #subtract health of characters from collision
            if (abs(other.dx) > 12 or abs(other.dy) > 12):
                self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
            if (abs(self.dx) > 12 or abs(self.dy) > 12):
                other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
            newSelfdx = self.getvxf(other)
            newOtherdx = other.getvxf(self)
            newSelfdy = self.getvyf(other)
            newOtherdy = other.getvyf(self)
            self.dx = newSelfdx
            other.dx = newOtherdx
            self.dy = newSelfdy
            other.dy = newOtherdy
            self.overlap = False
            self.x = otherRight + self.radius + 1
            self.y = otherBot + self.radius + 1
            #makes object dead if health is below 0
            if (self.health <= 0):
                self.alive = False
            if (other.health <= 0):
                other.alive = False
            #makes bird disappear after hitting and slowing down
            if (isinstance(self, Bird)):
                self.collided = True
            if (isinstance(other, Bird)):
                other.collided = True
    #checks collisions from top-right
    if(self.x <= otherLeft and self.y >= otherBot):
        dis = self.distance(self.x, self.y, otherLeft, otherBot)
        #coordinates for top right of self
        if (dis <= self.radius):
            #subtract health of characters from collision
            if (abs(other.dx) > 12 or abs(other.dy) > 12):
                self.health -= math.sqrt(other.getpx()**2 + other.getpy()**2)
            if (abs(self.dx) > 12 or abs(self.dy) > 12):
                other.health -= math.sqrt(self.getpx()**2 + self.getpy()**2)
            newSelfdx = self.getvxf(other)
            newOtherdx = other.getvxf(self)
            newSelfdy = self.getvyf(other)
            newOtherdy = other.getvyf(self)
            self.dx = newSelfdx
            other.dx = newOtherdx
            self.dy = newSelfdy
            other.dy = newOtherdy
            self.overlap = False
            self.x = otherLeft - self.radius - 1
            self.y = otherBot + self.radius + 1
            #makes object dead if health is below 0
            if (self.health <= 0):
                self.alive = False
            if (other.health <= 0):
                other.alive = False
            #makes bird disappear after hitting and slowing down
            if (isinstance(self, Bird)):
                self.collided = True
            if (isinstance(other, Bird)):
                other.collided = True
    else:
        self.overlap = False

runApp(width = 1280, height = 720)