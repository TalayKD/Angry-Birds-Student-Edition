from cmu_112_graphics import *
from Bird import *
from Pig import *
from Block import *

#this file stores all the data for initializing the different levels

##########################################
# Level Initialization
##########################################

##########################################
# Normal Mode
##########################################  

#initialize values for level 1
def initLevel1(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.red1 = Bird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "red1")
        app.red2 = Bird(180, 600, 0, 0, app.noGravity, "red2")
        app.red3 = Bird(130, 600, 0, 0, app.noGravity, "red3")
        app.birds = [app.red3, app.red2]
        app.playingBird = app.red1
        
        #initialize pig object
        app.pig1 = Pig(1050, 480, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 380, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(870, 580, 0, 0, app.noGravity, 'pig3')
        app.pigs = [app.pig1, app.pig2, app.pig3]
        
        #initialize block object
        app.block1 = Block(950, 470, 0, 0, app.noGravity, "woodblock1")
        app.block2 = Block(950, 580, 0, 0, app.noGravity, "woodblock2")
        app.block3 = Block(1050, 580, 0, 0, app.noGravity, "woodblock3")
        app.blocks =[app.block1, app.block2, app.block3]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 2
def initLevel2(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.red1 = Bird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "red1")
        app.red2 = Bird(180, 600, 0, 0, app.noGravity, "red2")
        app.red3 = Bird(130, 600, 0, 0, app.noGravity, "red3")
        app.birds = [app.red3, app.red2]
        app.playingBird = app.red1
        
        #initialize pig object
        app.pig1 = Pig(1050, 400, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(870, 580, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(1150, 580, 0, 0, app.noGravity, "pig4")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4]
        
        #initialize block object
        app.block1 = Block(950, 490, 0, 0, app.noGravity, "woodblock1")
        app.block2 = Block(950, 580, 0, 0, app.noGravity, "woodblock2")
        app.block3 = Block(1050, 580, 0, 0, app.noGravity, "woodblock3")
        app.block4 = Block(1050, 490, 0, 0, app.noGravity, "woodblock4")
        app.blocks =[app.block1, app.block2, app.block3, app.block4]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 3
def initLevel3(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.bigRed1 = BigRedBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "bigRed1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.red1 = Bird(130, 600, 0, 0, app.noGravity, "red1")
        app.birds = [app.red1, app.yellow1]
        app.playingBird = app.bigRed1
        
        #initialize pig object
        app.pig1 = Pig(1150, 490, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1050, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(950, 580, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(850, 400, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(750, 490, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1150, 580, 0, 0, app.noGravity, "glassblock1")
        app.block2 = GlassBlock(1050, 580, 0, 0, app.noGravity, "glassblock2")
        app.block3 = Block(1050, 490, 0, 0, app.noGravity, "woodblock1")
        app.block4 = GlassBlock(850, 580, 0, 0, app.noGravity, "glassblock3")
        app.block5 = GlassBlock(750, 580, 0, 0, app.noGravity, "glassblock4")
        app.block6 = Block(850, 490, 0, 0, app.noGravity, "woodblock2")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 4
def initLevel4(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.matilda1 = MatildaBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "matilda1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.red1 = Bird(130, 600, 0, 0, app.noGravity, "red1")
        app.bigRed1 = BigRedBird(70, 590, 0, 0, app.noGravity, "bigRed1")
        app.birds = [app.bigRed1, app.red1, app.yellow1]
        app.playingBird = app.matilda1
        
        #initialize pig object
        app.pig1 = Pig(1010, 430, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 580, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(890, 430, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(830, 580, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(760, 430, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1010, 510, 0, 0, app.noGravity, "glassblock1")
        app.block2 = SmallBlock(1010, 580, 0, 0, app.noGravity, "smallblock1")
        app.block3 = GlassBlock(890, 510, 0, 0, app.noGravity, "glassblock2")
        app.block4 = SmallBlock(890, 580, 0, 0, app.noGravity, "smallblock2")
        app.block5 = GlassBlock(760, 510, 0, 0, app.noGravity, "glassblock3")
        app.block6 = SmallBlock(760, 580, 0, 0, app.noGravity, "smallblock3")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 5
def initLevel5(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.boomerang1 = BoomerangBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "boomerang1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.bigred1 = BigRedBird(120, 590, 0, 0, app.noGravity, "bigred1")
        app.matilda1 = MatildaBird(50, 593, 0, 0, app.noGravity, "matilda1")
        app.birds = [app.matilda1, app.bigred1, app.yellow1]
        app.playingBird = app.boomerang1
        
        #initialize pig object
        app.pig1 = Pig(1150, 490, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1070, 580, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(990, 400, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(910, 580, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(830, 490, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1150, 580, 0, 0, app.noGravity, "glassblock1")
        app.block2 = StoneBlock(990, 580, 0, 0, app.noGravity, "stoneblock1")
        app.block3 = StoneBlock(990, 490, 0, 0, app.noGravity, "stoneblock2")
        app.block4 = Block(830, 580, 0, 0, app.noGravity, "woodblock1")
        app.block5 = StoneBlock(740, 580, 0, 0, app.noGravity, "stoneblock3")
        app.block6 = StoneBlock(740, 490, 0, 0, app.noGravity, "stoneblock4")
        app.block7 = StoneBlock(650, 580, 0, 0, app.noGravity, "stoneblock5")
        app.block8 = StoneBlock(650, 490, 0, 0, app.noGravity, "stoneblock6")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6, app.block7, app.block8]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 6
def initLevel6(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = False

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        app.matilda1 = MatildaBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "matilda1")
        
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.bigred1 = BigRedBird(120, 590, 0, 0, app.noGravity, "bigred1")
        app.boomerang1 = BoomerangBird(50, 593, 0, 0, app.noGravity, "boomerang1")
        app.birds = [app.boomerang1, app.bigred1, app.yellow1]
        app.playingBird = app.matilda1
        
        #initialize pig object
        app.pig1 = Pig(1150, 440, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1060, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(970, 490, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(880, 430, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(810, 580, 0, 0, app.noGravity, "pig5")
        app.pig6 = Pig(720, 430, 0, 0, app.noGravity, "pig6")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5, app.pig6]
        
        #initialize block object
        app.block1 = StoneBlock(1150, 580, 0, 0, app.noGravity, "stoneblock1")
        app.block2 = SmallBlock(1150, 510, 0, 0, app.noGravity, "smallblock1")
        app.block3 = StoneBlock(1060, 580, 0, 0, app.noGravity, "stoneblock2")
        app.block4 = StoneBlock(1060, 490, 0, 0, app.noGravity, "stoneblock3")
        app.block5 = StoneBlock(970, 580, 0, 0, app.noGravity, "stoneblock4")
        app.block6 = SmallBlock(880, 510, 0, 0, app.noGravity, "smallblock2")
        app.block7 = GlassBlock(880, 580, 0, 0, app.noGravity, "glassblock1")
        #pig in between here at 810
        app.block8 = SmallBlock(720, 510, 0, 0, app.noGravity, "smallblock3")
        app.block9 = GlassBlock(720, 580, 0, 0, app.noGravity, "glassblock2")
        app.block10 = StoneBlock(630, 580, 0, 0, app.noGravity, "stoneblock5")
        app.block11 = StoneBlock(630, 490, 0, 0, app.noGravity, "stoneblock6")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6, app.block7, app.block8, app.block9, app.block10, app.block11]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

##########################################
# No Gravity Mode
##########################################  

#initialize values for level 1
def initLevel1NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.red1 = Bird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "red1")
        app.red2 = Bird(180, 600, 0, 0, app.noGravity, "red2")
        app.red3 = Bird(130, 600, 0, 0, app.noGravity, "red3")
        app.birds = [app.red3, app.red2]
        app.playingBird = app.red1
        
        #initialize pig object
        app.pig1 = Pig(1050, 480, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 380, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(870, 580, 0, 0, app.noGravity, 'pig3')
        app.pigs = [app.pig1, app.pig2, app.pig3]
        
        #initialize block object
        app.block1 = Block(950, 470, 0, 0, app.noGravity, "woodblock1")
        app.block2 = Block(950, 580, 0, 0, app.noGravity, "woodblock2")
        app.block3 = Block(1050, 580, 0, 0, app.noGravity, "woodblock3")
        app.blocks =[app.block1, app.block2, app.block3]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 2
def initLevel2NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.red1 = Bird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "red1")
        app.red2 = Bird(180, 600, 0, 0, app.noGravity, "red2")
        app.red3 = Bird(130, 600, 0, 0, app.noGravity, "red3")
        app.birds = [app.red3, app.red2]
        app.playingBird = app.red1
        
        #initialize pig object
        app.pig1 = Pig(1050, 400, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(870, 580, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(1150, 580, 0, 0, app.noGravity, "pig4")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4]
        
        #initialize block object
        app.block1 = Block(950, 490, 0, 0, app.noGravity, "woodblock1")
        app.block2 = Block(950, 580, 0, 0, app.noGravity, "woodblock2")
        app.block3 = Block(1050, 580, 0, 0, app.noGravity, "woodblock3")
        app.block4 = Block(1050, 490, 0, 0, app.noGravity, "woodblock4")
        app.blocks =[app.block1, app.block2, app.block3, app.block4]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 3
def initLevel3NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.bigRed1 = BigRedBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "bigRed1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.red1 = Bird(130, 600, 0, 0, app.noGravity, "red1")
        app.birds = [app.red1, app.yellow1]
        app.playingBird = app.bigRed1
        
        #initialize pig object
        app.pig1 = Pig(1150, 490, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1050, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(950, 580, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(850, 400, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(750, 490, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1150, 580, 0, 0, app.noGravity, "glassblock1")
        app.block2 = GlassBlock(1050, 580, 0, 0, app.noGravity, "glassblock2")
        app.block3 = Block(1050, 490, 0, 0, app.noGravity, "woodblock1")
        app.block4 = GlassBlock(850, 580, 0, 0, app.noGravity, "glassblock3")
        app.block5 = GlassBlock(750, 580, 0, 0, app.noGravity, "glassblock4")
        app.block6 = Block(850, 490, 0, 0, app.noGravity, "woodblock2")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 4
def initLevel4NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.matilda1 = MatildaBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "matilda1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.red1 = Bird(130, 600, 0, 0, app.noGravity, "red1")
        app.bigRed1 = BigRedBird(70, 590, 0, 0, app.noGravity, "bigRed1")
        app.birds = [app.bigRed1, app.red1, app.yellow1]
        app.playingBird = app.matilda1
        
        #initialize pig object
        app.pig1 = Pig(1010, 430, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(950, 580, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(890, 430, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(830, 580, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(760, 430, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1010, 510, 0, 0, app.noGravity, "glassblock1")
        app.block2 = SmallBlock(1010, 580, 0, 0, app.noGravity, "smallblock1")
        app.block3 = GlassBlock(890, 510, 0, 0, app.noGravity, "glassblock2")
        app.block4 = SmallBlock(890, 580, 0, 0, app.noGravity, "smallblock2")
        app.block5 = GlassBlock(760, 510, 0, 0, app.noGravity, "glassblock3")
        app.block6 = SmallBlock(760, 580, 0, 0, app.noGravity, "smallblock3")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)

#initialize values for level 5
def initLevel5NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        #initialize red bird object with starting position at slingshot
        app.boomerang1 = BoomerangBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "boomerang1")
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.bigred1 = BigRedBird(120, 590, 0, 0, app.noGravity, "bigred1")
        app.matilda1 = MatildaBird(50, 593, 0, 0, app.noGravity, "matilda1")
        app.birds = [app.matilda1, app.bigred1, app.yellow1]
        app.playingBird = app.boomerang1
        
        #initialize pig object
        app.pig1 = Pig(1150, 490, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1070, 580, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(990, 400, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(910, 580, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(830, 490, 0, 0, app.noGravity, "pig5")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5]
        
        #initialize block object
        app.block1 = GlassBlock(1150, 580, 0, 0, app.noGravity, "glassblock1")
        app.block2 = StoneBlock(990, 580, 0, 0, app.noGravity, "stoneblock1")
        app.block3 = StoneBlock(990, 490, 0, 0, app.noGravity, "stoneblock2")
        app.block4 = Block(830, 580, 0, 0, app.noGravity, "woodblock1")
        app.block5 = StoneBlock(740, 580, 0, 0, app.noGravity, "stoneblock3")
        app.block6 = StoneBlock(740, 490, 0, 0, app.noGravity, "stoneblock4")
        app.block7 = StoneBlock(650, 580, 0, 0, app.noGravity, "stoneblock5")
        app.block8 = StoneBlock(650, 490, 0, 0, app.noGravity, "stoneblock6")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6, app.block7, app.block8]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)


#initialize values for level 6
def initLevel6NoGrav(app):
        app.gameOverWin = False
        app.gameOverLose = False
        app.score = 0
        app.noGravity = True

        #initialize egg as false, and it will only be used when Matilda Bird uses her power
        app.egg = Egg(0, 0, False, "Egg1")
        app.matilda1 = MatildaBird(app.slingstartcx, app.slingstartcy, 0, 0, app.noGravity, "matilda1")
        
        app.yellow1 = YellowBird(180, 600, 0, 0, app.noGravity, "yellow1")
        app.bigred1 = BigRedBird(120, 590, 0, 0, app.noGravity, "bigred1")
        app.boomerang1 = BoomerangBird(50, 593, 0, 0, app.noGravity, "boomerang1")
        app.birds = [app.boomerang1, app.bigred1, app.yellow1]
        app.playingBird = app.matilda1
        
        #initialize pig object
        app.pig1 = Pig(1150, 440, 0, 0, app.noGravity, "pig1")
        app.pig2 = Pig(1060, 400, 0, 0, app.noGravity, "pig2")
        app.pig3 = Pig(970, 490, 0, 0, app.noGravity, "pig3")
        app.pig4 = Pig(880, 430, 0, 0, app.noGravity, "pig4")
        app.pig5 = Pig(810, 580, 0, 0, app.noGravity, "pig5")
        app.pig6 = Pig(720, 430, 0, 0, app.noGravity, "pig6")
        app.pigs = [app.pig1, app.pig2, app.pig3, app.pig4, app.pig5, app.pig6]
        
        #initialize block object
        app.block1 = StoneBlock(1150, 580, 0, 0, app.noGravity, "stoneblock1")
        app.block2 = SmallBlock(1150, 510, 0, 0, app.noGravity, "smallblock1")
        app.block3 = StoneBlock(1060, 580, 0, 0, app.noGravity, "stoneblock2")
        app.block4 = StoneBlock(1060, 490, 0, 0, app.noGravity, "stoneblock3")
        app.block5 = StoneBlock(970, 580, 0, 0, app.noGravity, "stoneblock4")
        app.block6 = SmallBlock(880, 510, 0, 0, app.noGravity, "smallblock2")
        app.block7 = GlassBlock(880, 580, 0, 0, app.noGravity, "glassblock1")
        #pig in between here at 810
        app.block8 = SmallBlock(720, 510, 0, 0, app.noGravity, "smallblock3")
        app.block9 = GlassBlock(720, 580, 0, 0, app.noGravity, "glassblock2")
        app.block10 = StoneBlock(630, 580, 0, 0, app.noGravity, "stoneblock5")
        app.block11 = StoneBlock(630, 490, 0, 0, app.noGravity, "stoneblock6")
        app.blocks =[app.block1, app.block2, app.block3, app.block4, app.block5, app.block6, app.block7, app.block8, app.block9, app.block10, app.block11]

        #list of all the objects on the screen
        app.characters = [app.playingBird] + app.pigs + app.blocks
        app.initialScore = len(app.birds)