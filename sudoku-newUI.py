from cmu_graphics import *
import os
import random
import copy
import math
import itertools
import PIL
from PIL import Image
import pyscreenshot

##############################################################
# starter code necessary to read files                       #
# from https://www.cs.cmu.edu/~112-3/notes/term-project.html #
##############################################################

def readFile(path):
  with open(path, "rt") as f:
    return f.read()

#makes a list of all the easy boards (modified website code)
easyBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("easy") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    easyBoards.append(fileContents)

#makes a list of all the medium boards (modified website code)
mediumBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("medium") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    mediumBoards.append((fileContents))

#makes a list of all the hard boards (modified website code)
hardBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("hard") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    hardBoards.append(fileContents)

#makes a list of all the expert boards (modified website code)
expertBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("expert") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    expertBoards.append(fileContents)

#makes a list of all the evil boards (modified website code)
evilBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("evil") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    evilBoards.append(fileContents)

#makes a list of all the custom boards (modified website code)
customBoards = []
for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/'):
  if filename.startswith("custom") and filename.endswith('.txt'):
    pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
    fileContents = readFile(pathToFile)
    customBoards.append(fileContents)

##############################################################
# starter code to write files                                #
# from https://www.cs.cmu.edu/~112-3/notes/term-project.html #
##############################################################

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

########################
# start of home screen #
########################

def home_onAppStart(app):
  app.customFileName = ''
  app.keyBoardOnly = False
  print(app.keyBoardOnly)

  #from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo5_using_animated_gifs.py
  #gif from https://giphy.com/gifs/kochstrasse-cute-illustration-5niGzdBTajGUCxTrLN
  #background removed with https://onlinegiftools.com/remove-gif-background
  app.sprites = loadAnimatedGif(app, 'rainbowNoBG.gif')
  app.spriteCounter = 9
  app.stepsPerSecond = 10

#from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo5_using_animated_gifs.py
def loadAnimatedGif(app, path):
    pilImages = Image.open(path)
    if pilImages.format != 'GIF':
        raise Exception(f'{path} is not an animated image!')
    if not pilImages.is_animated:
        raise Exception(f'{path} is not an animated image!')
    cmuImages = [ ]
    for frame in range(pilImages.n_frames):
        pilImages.seek(frame)
        pilImage = pilImages.copy()
        cmuImages.append(CMUImage(pilImage))
    return cmuImages

#from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo5_using_animated_gifs.py
def home_onStep(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def home_redrawAll(app):
  drawLabel("RainbowKu!", 200, 325, size = 60, font = "monospace")
  drawLabel("click anywhere to start", 200, 375, size = 20, font = "monospace")

  #from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo5_using_animated_gifs.py
  # Draw the current sprite image:
  sprite = app.sprites[app.spriteCounter]
  drawImage(sprite, 200, 200, align='center')

def home_onKeyPress(app, key):
  if app.mouseOnly == True:
    pass
  else:
    setActiveScreen("settings")

def home_onMousePress(app, mouseX, mouseY):
  if app.keyBoardOnly == True:
    pass
  else:
    setActiveScreen("settings")

###################
# settings screen #
###################

def settings_onAppStart(app):
  app.keyBoardOnly = False
  app.mouseOnly = False
  app.displayKeyboard = False
  app.customName = ''
  # app.board = None
  openMyImage2(app)

# from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo1_drawing_images.py
# image from https://gallery.yopriceville.com/Free-Clipart-Pictures/Rainbows-PNG/Rainbow_Line_PNG_Clip_Art_Image?fb_comment_id=1022624594459796_1235944666461120#.Y5DJB-zMK3I
def openMyImage2(app):
  app.image2 = Image.open('rainbow-line.png')
  # Convert each PIL image to a CMUImage for drawing
  app.image2 = CMUImage(app.image2)

def settings_redrawAll(app):
  drawSettings(app)

def drawSettings(app):
  # from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo1_drawing_images.py
  pilImage = app.image2.image
  drawImage(app.image2, 200, 30, align='center',
            width=pilImage.width//20,
            height=pilImage.height//20)

  drawRect(5, 5, 390, 590, fill = None, borderWidth = 5, border = "black")
  drawLabel("Settings!", 200, 30, size = 30, font = "monospace")

  drawLabel("Mode:", 15, 75, align = 'left', size = 20, font = "monospace")
  if app.keyBoardOnly == app.mouseOnly == False: colorN = "lightgreen"
  else: colorN = None
  drawRect(20, 90, 115, 40, fill = colorN, border = "black")
  drawLabel("normal", 77, 110, font = "monospace", size = 16)
  drawLabel("press 'n'", 77, 120, font = "monospace", size = 8)
  if app.keyBoardOnly == True and app.keyBoardOnly != app.mouseOnly: colorK = "lightgreen"
  else: colorK = None
  drawRect(140, 90, 115, 40, fill = colorK, border = "black")
  drawLabel("keyboard-only", 197, 110, font = "monospace", size = 14)
  drawLabel("press 'k'", 197, 120, font = "monospace", size = 8)
  if app.mouseOnly == True and app.keyBoardOnly != app.mouseOnly: colorM = "lightgreen"
  else: colorM = None
  drawRect(260, 90, 115, 40, fill = colorM, border = "black")
  drawLabel("mouse-only", 317, 110, font = "monospace", size = 14)
  drawLabel("press 'm'", 317, 120, font = "monospace", size = 8)

  drawLabel("Difficulty:", 15, 150, align = 'left', size = 20, font = "monospace")
  if app.modeNumber == 0:
    color0 = "lightgreen"
  else: color0 = None
  drawRect(20, 170, 65, 40, fill = color0, border = "black")
  drawLabel("easy", 52, 190, font = "monospace", size = 16)
  if app.modeNumber == 1:
    color1 = "lightgreen"
  else: color1 = None
  drawRect(92, 170, 65, 40, fill = color1, border = "black")
  drawLabel("medium", 124, 190, font = "monospace", size = 15)
  if app.modeNumber == 2:
    color2 = "lightgreen"
  else: color2 = None
  drawRect(164, 170, 65, 40, fill = color2, border = "black")
  drawLabel("hard", 196, 190, font = "monospace", size = 16)
  if app.modeNumber == 3:
    color3 = "lightgreen"
  else: color3 = None
  drawRect(236, 170, 65, 40, fill = color3, border = "black")
  drawLabel("expert", 268, 190, font = "monospace", size = 16)
  if app.modeNumber == 4:
    color4 = "lightgreen"
  else: color4 = None
  drawRect(308, 170, 65, 40, fill = color4, border = "black")
  drawLabel("evil", 340, 190, font = "monospace", size = 16)

  drawLabel("Custom Board:", 15, 225, align = 'left', size = 20, font = "monospace")
  drawRect(20, 240, 115, 40, fill = None, border = 'black')
  drawLabel("Input Board", 77.5, 255, font = "monospace", size = 14)
  drawLabel("press 'c'", 77.5, 265, font = "monospace", size = 8)
  drawRect(140, 240, 115, 40, fill = None, border = 'black')
  drawLabel(" Load txt file that", 195.5, 250, font = "monospace",size = 10)
  drawLabel(" starts w/'custom'", 195.5, 260, font = "monospace",size = 10)
  drawLabel("press 'C'", 195.5, 270, font = "monospace", size = 8)
  drawRect(260, 240, 115, 40, fill = None, border = 'black')
  drawLabel("Type File Name", 315.5, 255, font = "monospace", size = 12)
  drawLabel("press 't'", 315.5, 265, font = "monospace", size = 8)

  drawLabel("Number of Lives:", 15, 295, align = 'left', size = 20, font = "monospace")
  for i in range(5):
    drawRect(20+i*72.4, 310, 65.4, 20, fill = None, border = 'black')
    if app.lives == i+1:
      drawRect(20+i*72.4, 310, 65.4, 20, fill = "lightgreen", border = 'black')
    drawLabel(i+1, 52.5+i*72.4, 320)
  #maybe be able to choose color schemes with like original colors, countries colors, etc

  drawRect(20, 420, 160, 160, fill = rgb(255, 255, 115), border = "gold")
  drawLabel("Instructions", 100, 490, font = "monospace", size = 20)
  drawLabel("press 'i'", 100, 510, font = "monospace", size = 12)
  drawRect(220, 420, 160, 160, fill = "lightgreen", border = "green")
  drawLabel("Play Game", 300, 490, font = "monospace", size = 20)
  drawLabel("press 'g'", 300, 510, font = "monospace", size = 12)

  if app.displayKeyboard == True:
    drawRect(0, 0, 400, 600, fill = 'lightgrey', opacity = 50)
    drawRect(75, 200, 250, 200, fill = "white", border = "black", borderWidth = 2)
    drawKeyboard(app)
    pass

def drawKeyboard(app):
  drawLabel("file name", 90, 220, align = "left", font = "monospace", size = 14)
  drawRect(90, 230, 220, 15, fill = None, border = "black", borderWidth = 1)
  drawLabel(app.customName, 92, 237.5, align = "left", font = "monospace", size = 12)
  topLine = '1234567890-_'
  for i in range(12):
    drawLabel(topLine[i], 15*i+125, 270, size = 14)
  firstLine = 'qwertyuiop'
  for i in range(10):
    drawLabel(firstLine[i], 15*i+132.5, 290, size = 14)
  secondLine = 'asdfghjkl'
  for i in range(9):
    drawLabel(secondLine[i], 15*i+140, 310, size = 14)
  thirdLine = 'zxcvbnm'
  for i in range(7):
    drawLabel(thirdLine[i], 15*i+155, 330, size = 14)
  drawRect(145, 345, 110, 17, fill = None, border = 'black')
  drawLabel("space", 200, 353.5, size = 14)

  drawRect(90, 345, 40, 40, fill = None, border = "black")
  drawLabel("enter", 110, 360, font = "monospace", size = 10)
  drawLabel("/ save", 110, 370, font = "monospace", size = 10)

  drawRect(270, 345, 40, 40, fill = None, border = "black")
  drawLabel("back-", 290, 360, font = "monospace", size = 10)
  drawLabel("space", 290, 370, font = "monospace", size = 10)

def settings_onKeyPress(app, key):
  if app.mouseOnly == True:
    pass
  else:
    if app.displayKeyboard == True:
      inputFileName(app, key)
    else:
      if key == "i":
        setActiveScreen("instructions")
      elif key == "g":
        setActiveScreen("game")
      elif key == "n":
        app.keyBoardOnly = False
        app.mouseOnly = False
      elif key == "k":
        app.mouseOnly = False
        app.keyBoardOnly = not app.keyBoardOnly
      elif key == "m":
        app.keyBoardOnly = False
        app.mouseOnly = not app.mouseOnly
      elif key == "c":
        app.creatingCustom = True
        app.modeNumber = 5
        app.stateBoard = State()
        setActiveScreen("game")
      elif key == "t":
        app.displayKeyboard = not app.displayKeyboard
        #display the file name
      elif key in ["!", "@", "#", "$", ")", "C"]:
        app.modeNumber = identifyModeNumber(key)
        newGeneratedBoard(app)
      elif key in ["1", "2", "3", "4", "5"]:
        app.lives = int(key)

def settings_onMousePress(app, mouseX, mouseY):
  if app.keyBoardOnly == True:
    pass
  else:
    if app.displayKeyboard == True:
      letter = identifyLetter(app, mouseX, mouseY)
      inputFileName(app, letter)

      #button presses correspond with keyboard
    else:
      #for the modes
      if (20 <= mouseX <= 135) and (90 <= mouseY <= 130):
        app.keyBoardOnly = False
        app.mouseOnly = False
      elif (140 <= mouseX <= 255) and (90 <= mouseY <= 130):
        app.mouseOnly = False
        app.keyBoardOnly = not app.keyBoardOnly
      elif (260 <= mouseX <= 375) and (90 <= mouseY <= 130):
        app.mouseOnly = not app.mouseOnly
        app.keyBoardOnly = False
      #for difficulty
      elif (20 <= mouseX <= 85) and (170 <= mouseY <= 210):
        app.modeNumber = 0
      elif (92 <= mouseX <= 157) and (170 <= mouseY <= 210):
        app.modeNumber = 1
      elif (164 <= mouseX <= 229) and (170 <= mouseY <= 210):
        app.modeNumber = 2
      elif (236 <= mouseX <= 301) and (170 <= mouseY <= 210):
        app.modeNumber = 3
      elif (308 <= mouseX <= 373) and (170 <= mouseY <= 210):
        app.modeNumber = 4
      #for custom
      elif (20 <= mouseX <= 135) and (240 <= mouseY <= 280):
        app.creatingCustom = True
        app.modeNumber = 5
        app.stateBoard = State()
        setActiveScreen("game")
      elif (140 <= mouseX <= 255) and (240 <= mouseY <= 280):
        app.modeNumber = identifyModeNumber('C')
        newGeneratedBoard(app)
        setActiveScreen("game")
      elif (260 <= mouseX <= 375) and (240 <= mouseY <= 280):
        app.displayKeyboard = True
      #for lives
      elif (20 <= mouseX <= 373) and (310 <= mouseY <= 330):
        for i in range(5):
          if (20+65*i <= mouseX <= 85+65*i) and (310 <= mouseY <= 330):
            app.lives = i+1

        #display the keyboard
        #display the file name
      #for screen
      elif (20 <= mouseX <= 180) and (420 <= mouseY <= 580):
        setActiveScreen("instructions")
      elif (220 <= mouseX <= 380) and (420 <= mouseY <= 580):
        setActiveScreen("game")

def inputFileName(app, letter):
  if letter == "backspace":
    app.customName = app.customName[:-1]
  elif letter == "enter":
    app.displayKeyboard = False
    app.customFileName = app.customName
    print(app.customFileName)
    filenameIntoState(app)
  elif letter == "space":
    app.customName = app.customName + " "
  else:
    app.customName = app.customName + str(letter)

def identifyLetter(app, mouseX, mouseY):
  letter = ''
  #top row
  topRow = '1234567890-_'
  for i in range(12):
    if (120+i*15 <= mouseX <= 130+i*15)  and (265 <= mouseY <= 275):
      letter = topRow[i]
  #first row
  firstRow = 'qwertyuiop'
  for i in range(10):
    if (127+i*15 <= mouseX <= 137+i*15)  and (285 <= mouseY <= 295):
      letter = firstRow[i]
  #second row
  secondRow = 'asdfghjkl'
  for i in range(9):
    if (135+i*15 <= mouseX <= 145+i*15)  and (305 <= mouseY <= 315):
      letter = secondRow[i]
  #third row
  thirdRow = 'zxcvbnm'
  for i in range(7):
    if (150+i*15 <= mouseX <= 160+i*15)  and (325 <= mouseY <= 335):
      letter = thirdRow[i]

  if (90 <= mouseX <= 130) and (345 <= mouseY <= 385):
    letter = "enter"
  elif (145 <= mouseX <= 255) and (345 <= mouseY <= 362):
    letter = "space"
  elif (270 <= mouseX <= 320) and (345 <= mouseY <= 385):
    letter = 'backspace'
  return letter

def filenameIntoState(app):
  app.testList = [1, 2, 3]
  print("433", app.customFileName)
  if app.customFileName != "":
    print("not empty")
    try:
      print("trying!!!!")
      newFileContents = ''
      originalBoard = []
      for filename in os.listdir('/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards'):
        if str(filename) == str(app.customFileName):
          pathToFile = f'/Users/annie/Downloads/15-112/sudoku term project/tp-starter-files/boards/{filename}'
          newFileContents = readFile(pathToFile)
          originalBoard.append(newFileContents)
      app.board = originalBoard[0]
      app.modeNumber = 5
      print("board")
      print(app.board)
      fileIntoState(app)
      setActiveScreen("game")
    except:
      print("nope")
      setActiveScreen("game")
  else:
    print("empty")
    setActiveScreen("game")

################################
# start of instructions screen #
################################

def instructions_onAppStart(app):
  pass

def instructions_redrawAll(app):
  # from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo1_drawing_images.py
  pilImage = app.image2.image
  drawImage(app.image2, 200, 25, align='center',
            width=pilImage.width//20,
            height=pilImage.height//20)
  drawInstructions(app)

  drawRect(0, 202, 100, 50, fill = "lightblue", border = "navy")
  drawLabel("Settings", 50, 220, font = "monospace", size = 16)
  drawLabel("press 's'", 50, 230, font = "monospace", size = 10)
  drawRect(300, 202, 100, 50, fill = "lightgreen", border = "forestgreen")
  drawLabel("Play Game", 350, 220, font = "monospace", size = 16)
  drawLabel("press 'g'", 350, 230, font = "monospace", size = 10)

def drawInstructions(app):
  drawRect(5, 5, 390, 580, fill = None, borderWidth = 5, border = "black")
  drawLabel("Instructions!", 200, 25, size = 30, font = "monospace")

  drawRect(20, 40, 360, 180, fill = None, border = "black", borderWidth = 1)
  drawLabel("Rules:", 200, 55, font = 'monospace', size = 18, bold = True)
  rulesStr1 = "The aim of the game is to fill the board so that each number only appears once in each region."
  rulesList1 = rulesStr1.split(" ")
  rulesStr2 = "A region is defined by any row, column, or 'block', which is a 3x3 square on the board."
  rulesList2 = rulesStr2.split(" ")
  rulesStr3 = "There is only one solution to each board and there should never be a point in which you have to guess."
  rulesList3 = rulesStr3.split(" ")
  rulesStr4 = "However, if you get stuck, there are lots of strategies you can use to help you derive the correct answer!"
  rulesList4 = rulesStr4.split(" ")
  for i in range(12):
    currList1 = rulesList1[i*12:(i+1)*12]
    currStr1 = " ".join(currList1)
    drawLabel(currStr1, 25, 70+i*10, font = "monospace", align = "left")
  for i in range(9):
    currList2 = rulesList2[i*9:(i+1)*9]
    currStr2 = " ".join(currList2)
    drawLabel(currStr2, 25, 70+(i+3)*10, font = "monospace", align = "left")
  for i in range(9):
    currList3 = rulesList3[i*9:(i+1)*9]
    currStr3 = " ".join(currList3)
    drawLabel(currStr3, 25, 70+(i+6)*10, font = "monospace", align = "left")
  for i in range(9):
    currList4 = rulesList4[i*9:(i+1)*9]
    currStr4 = " ".join(currList4)
    drawLabel(currStr4, 25, 70+(i+10)*10, font = "monospace", align = "left")

  drawRect(20, 235, 360, 335, fill = None, border = "black", borderWidth = 1)
  drawLabel("Controls:", 200, 250, font = "monospace", size = 18, bold = True)
  drawLabel("all keyboard shortcuts have clickable buttons on screen!", 200, 265, font = "monospace", size = 10)
  #left column
  drawLabel("modes:", 90, 285, italic = True, font = "monospace", size = 11)
  drawLabel("'n' -> normal mode", 25, 300, font = 'monospace', size = 11, align = "left")
  drawLabel("'k' -> keyboard-only mode", 25, 315, font = 'monospace', size = 11, align = "left")
  drawLabel("'m' -> mouse-only mode", 25, 330, font = 'monospace', size = 11, align = "left")
  drawLabel("difficulty:", 90, 360, italic = True, font = "monospace", size = 11)
  drawLabel("'shift+0' -> easy", 25, 375, font = 'monospace', size = 11, align = "left")
  drawLabel("'shift+1' -> medium", 25, 390, font = 'monospace', size = 11, align = "left")
  drawLabel("'shift+2' -> hard", 25, 405, font = 'monospace', size = 11, align = "left")
  drawLabel("'shift+3' -> expert", 25, 420, font = 'monospace', size = 11, align = "left")
  drawLabel("'shift+4' -> evil", 25, 435, font = 'monospace', size = 11, align = "left")
  drawLabel("custom boards:", 90, 465, italic = True, font = "monospace", size = 11)
  drawLabel("'c' -> input custom board", 25, 480, font = 'monospace', size = 11, align = "left")
  drawLabel("'C' -> load custom board", 25, 495, font = 'monospace', size = 11, align = "left")
  drawLabel("'t' -> input file name to", 25, 510, font = 'monospace', size = 11, align = "left")
  drawLabel("load board", 75, 525, font = 'monospace', size = 11, align = "left")
  #right column
  drawLabel("game screen:", 290, 285, italic = True, font = "monospace", size = 11)
  drawLabel("'r' -> load new board", 225, 300, font = 'monospace', size = 11, align = "left")
  drawLabel("'h' -> display a hint", 225, 315, font = 'monospace', size = 11, align = "left")
  drawLabel("'H' -> do a hint", 225, 330, font = 'monospace', size = 11, align = "left")
  drawLabel("'N' -> display notes", 225, 360, font = 'monospace', size = 11, align = "left")
  drawLabel("'M' -> make/edit notes", 225, 375, font = 'monospace', size = 11, align = "left")
  drawLabel("'W' -> show incorrect", 225, 390, font = 'monospace', size = 11, align = "left")
  drawLabel("notes", 270, 405, font = 'monospace', size = 11, align = "left")
  drawLabel("'d' -> display legals", 225, 435, font = 'monospace', size = 11, align = "left")
  drawLabel("'L' -> toggle automatic", 225, 450, font = 'monospace', size = 11, align = "left")
  drawLabel("updated legals", 270, 465, font = 'monospace', size = 11, align = "left")
  drawLabel("'p' -> autoplay", 225, 480, font = 'monospace', size = 11, align = "left")
  drawLabel("singletons", 270, 495, font = 'monospace', size = 11, align = "left")
  drawLabel("'U' -> undo moves", 225, 525, font = 'monospace', size = 11, align = "left")
  drawLabel("'R' -> redo moves", 225, 540, font = 'monospace', size = 11, align = "left")


def instructions_onKeyPress(app, key):
  if app.mouseOnly == True:
    pass
  else:
    if key == "s":
      setActiveScreen("settings")
    elif key == "g":
      setActiveScreen("game")

def instructions_onMousePress(app, mouseX, mouseY):
  if app.keyBoardOnly == True:
    pass
  else:
    if (0 <= mouseX <= 100) and (202 <= mouseY <= 252):
      setActiveScreen("settings")
    elif (300 <= mouseX <= 400) and (202 <= mouseY <= 252):
      setActiveScreen("game")

###############
# game screen #
###############

def game_onAppStart(app):
  openMyImage(app)
  originalBoard = []
  app.modes = [easyBoards, mediumBoards, hardBoards, expertBoards, evilBoards, customBoards, originalBoard]
  app.modesNames = ['easy', 'medium', 'hard', 'expert', 'evil', 'custom']
  app.modeNumber = 0
  app.message = ''
  app.testList = []
  # app.message = f'my board {app.board}'
  app.message = "it did not work"
  newGeneratedBoard(app)
  boardApp(app)

## makes text file into state object
def newGeneratedBoard(app):
  # app.message = f'my mode number {app.modeNumber}'
  app.gameOver = False
  boardIndexLimit = len(app.modes[app.modeNumber])
  app.boardIndex = random.randrange(0, boardIndexLimit)
  # app.message = f'my mode number {app.modeNumber}'
  app.board = app.modes[app.modeNumber][app.boardIndex]
  app.creatingCustom = False
  fileIntoState(app)
  app.banningValues = False
  app.displayNotes = False
  app.displayWrongNotes = False
  app.competitionMode = False
  app.lives = 3
  app.displayLegals = False
  app.movesMade = []
  app.redoList = []
  if app.modeNumber == 0:
    app.isAutoLegals = False
  elif app.modeNumber >= 1:
    app.isAutoLegals = True
  app.wrongLegals = set()
  app.notes = [[set() for i in range(9)] for i in range(9)]
  app.hintMessage = ''
  app.displayHint = False
  app.takingScreenshot = False
  app.stepsPerSecond = 1
  app.steps = 0
  app.alreadyWrong = set()

  # app.message = "no file name"

def fileIntoState(app):
  print("file into state")
  app.stateBoard = State()
  app.solvedBoard = State()
  app.originalBoard = State()
  splitBoard = app.board.splitlines()
  for rowNum in range(len(splitBoard)):
    splitLine = splitBoard[rowNum].split(" ")
    for colNum in range(len(splitLine)):
      app.stateBoard.set(rowNum, colNum, int(splitLine[colNum]))
      app.solvedBoard.set(rowNum, colNum, int(splitLine[colNum]))
      app.originalBoard.set(rowNum, colNum, int(splitLine[colNum]))
  solveSudoku(app)

def game_redrawAll(app):
  drawLabel("SUDOKU!", 200, 25, size = 60, font = "monospace")
  drawBlocks(app)
  drawBoard(app)
  drawBoardBorder(app)
  drawNumbers(app)
  drawLegals(app)
  drawNotes(app)
  drawLives(app)

  #draw the home and settings buttons
  drawRect(25, 15, 40, 40, fill = 'pink', border = 'red')
  drawLabel("S", 45, 35, fill = 'red')
  drawRect(335, 15, 40, 40, fill = rgb(255, 255, 115), border = 'gold')
  drawLabel("I", 355, 35, fill = 'gold')
  drawNumberBoard(app)

  if app.takingScreenshot == False:
    if app.creatingCustom == False:
      message = f"mode: {app.modesNames[app.modeNumber]}"
    elif app.creatingCustom == True:
      message = "custom board"
  else:
    message = "converting to pdf..."
  drawLabel(message, 200, 55, size = 25, font = 'monospace')
  # if app.message != "":
  #   print(app.message)

  if app.creatingCustom == False:
    drawBottomLeft(app)
  else:
    drawBottomLeftCustom(app)

  if app.gameOver == True:
    message = "GAME OVER"
    if app.takingScreenshot == False:
      drawRect(0, 0, 400, 120, fill = "red", opacity = 20)
      drawRect(0, 120, 400, 120, fill = "orange", opacity = 20)
      drawRect(0, 240, 400, 120, fill = "yellow", opacity = 20)
      drawRect(0, 360, 400, 120, fill = "green", opacity = 20)
      drawRect(0, 480, 400, 120, fill = "blue", opacity = 20)
    drawRect(155, 430, 215, 160, fill = "white", border = "black")
    drawRect(160, 490 ,100, 50, fill = "gold", opacity = 50, border = "black", borderWidth = 1)
    drawRect(265, 490, 100, 50, fill = 'pink', opacity = 50, border = "black", borderWidth = 1)
    drawLabel("save as pdf", 210, 515, font = "monospace", bold = True)
    drawLabel("new game", 315, 515, font = "monospace", bold = True)

  else:
    if app.displayHint == True:
      drawRect(0, 0, 400, 600, fill = 'lightgrey', opacity = 50)
      drawRect(100, 150, 200, 200, fill = "white", border = "grey", borderWidth = 5)
      strList = app.hintMessage.split(" ")
      if len(strList) <= 5:
        for i in range(len(strList)//4 + 1):
          currList = strList[i*4:(i+1)*4]
          currStr = ''
          for word in currList:
            currStr = currStr + word + " "
          drawLabel(currStr, 202, 250+i*15, font = "monospace", size = 16)
      elif len(strList) <= 20:
        for i in range(len(strList)//4 + 1):
          currList = strList[i*4:(i+1)*4]
          currStr = ''
          for word in currList:
            currStr = currStr + word + " "
          drawLabel(currStr, 202, 210+i*15, font = "monospace", size = 16)
      else:
        for i in range(len(strList)//5 + 1):
          currList = strList[i*5:(i+1)*5]
          currStr = ''
          for word in currList:
            currStr = currStr + word + " "
          drawLabel(currStr, 202, 180+i*15, font = "monospace", size = 14)

      drawLabel("click anywhere on this box", 200, 300, font = "monospace")
      drawLabel("or press 'D'", 200, 310, font = "monospace")
      drawLabel("to continue the game", 200, 320, font = "monospace")

def game_onKeyPress(app, key):
  if app.mouseOnly == True:
    pass
  elif key == "~":
    app.competitionMode = not app.competitionMode
  else:
    if key == "i":
      setActiveScreen("instructions")
    elif key == "s":
      setActiveScreen("settings")
    elif key in ["!", "@", "#", "$", ")", "C"]:
      app.modeNumber = identifyModeNumber(key)
      newGeneratedBoard(app)
    elif key == "r":
      app.boardIndex = random.randrange(0, 50)
      newGeneratedBoard(app)
    #next 4 lines taken from https://cs3-112-f22.academy.cs.cmu.edu/notes/4189
    elif key == 'left':   moveSelection(app, 0, -1)
    elif key == 'right': moveSelection(app, 0, +1)
    elif key == 'up':    moveSelection(app ,-1, 0)
    elif key == 'down':  moveSelection(app, +1, 0)
    elif key == 'd':
      app.displayLegals = not app.displayLegals
      app.displayNotes = False
    elif key == 'L':
      app.isAutoLegals = not app.isAutoLegals

    if app.gameOver == False:
      if key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and app.creatingCustom == False and app.banningValues == False:
        print("should be able to click")
        row, col = app.selection
        if (row,col) in app.movesMade or app.stateBoard.board[row][col] == 0:
          if app.isAutoLegals == False:
            app.stateBoard.board[row][col] = int(key)
          elif app.isAutoLegals == True:
            app.stateBoard.set(row, col, int(key))
          app.movesMade.append((row, col))
          checkGameOver(app)
      elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and app.creatingCustom == True:
        inputtingCustomBoard(app, key)
      elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and app.creatingCustom == False and app.banningValues == True and app.displayLegals == True:
        banLegals(app, app.stateBoard, key)
      elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and app.creatingCustom == False and app.banningValues == True and app.displayNotes == True:
        changeNotes(app, app.notes, key)
      elif key == "S" and app.creatingCustom == True: #save the board
        app.creatingCustom = False
      elif key == 'c':
        app.creatingCustom = True
        app.modeNumber = 5
        app.stateBoard = State()
      elif key == "p":
        autoPlaySingleton(app)
      elif key == "M": #making/updating notes or legals
        app.banningValues = not app.banningValues
      elif key == "N": #displaying notes
        app.displayNotes = not app.displayNotes
        app.displayNotes = False
      elif key == "W": #showing that notes are wrong
        app.displayWrongNotes = not app.displayWrongNotes
      elif key == "U":
        undoMove(app)
      elif key == "R":
        redoMove(app)
      if app.competitionMode == False:
        if key == "h":
          generateHint(app)
        elif key == "H":
          doHint(app)
      elif key == "D":
        app.displayHint = False

def game_onMousePress(app, mouseX, mouseY):
  if app.keyBoardOnly == True:
    pass
  else:
    if app.displayHint == True and (100 <= mouseX <= 300) and (150 <= mouseY <= 350):
      app.displayHint = False
    #next 6 lines taken from https://cs3-112-f22.academy.cs.cmu.edu/notes/4189
    else:
      selectedCell = getCell(app, mouseX, mouseY)
      if selectedCell != None:
        if selectedCell == app.selection:
          app.selection = None
        else:
          app.selection = selectedCell
          app.selectionList = []

    #pressing home and settings screens
    if (25 <= mouseX <= 65) and (15 <= mouseY <= 55):
      setActiveScreen("settings")
    elif (335 <= mouseX <= 375) and (15 <= mouseY <= 55):
      setActiveScreen("instructions")

    if app.gameOver == False:
      #if pressing the custom board button
      if app.creatingCustom == True:
        if (25 <= mouseX <= 135) and (435 <= mouseY <= 585):
          print("app.creatingCustom = False")
          app.creatingCustom = False

      #first row
      elif (30 <= mouseX <= 60) and (475 <= mouseY <= 505):
        app.boardIndex = random.randrange(0, 50)
        newGeneratedBoard(app)
      if app.competitionMode == False:
        if (60 <= mouseX <= 90) and (475 <= mouseY <= 505):
          generateHint(app)
        elif (100 <= mouseX <= 130) and (475 <= mouseY <= 505):
          doHint(app)
      #second row
      if (30 <= mouseX <= 60) and (510 <= mouseY <= 540):
        app.displayNotes = not app.displayNotes
        app.displayLegals = False
      elif (60 <= mouseX <= 90) and (510 <= mouseY <= 540):
        app.banningValues = not app.banningValues
      elif (100 <= mouseX <= 130) and (510 <= mouseY <= 540):
        app.displayWrongNotes = not app.displayWrongNotes
      #third row
      elif app.modeNumber != 0:
        if (30 <= mouseX <= 60) and (545 <= mouseY <= 575):
          app.displayLegals = not app.displayLegals
          app.displayNotes = False
        elif (60 <= mouseX <= 90) and (545 <= mouseY <= 575):
          app.isAutoLegals = not app.isAutoLegals
        elif (100 <= mouseX <= 130) and (545 <= mouseY <= 575):
          autoPlaySingleton(app)

      #if pressing the number board buttons
      if (155 <= mouseX <= 370) and (430 <= mouseY <= 590): #if it's in that general area
        if (155 <= mouseX <= 205) and (430 <= mouseY <= 485):
          undoMove(app)
        elif (155 <= mouseX <= 205) and (540 <= mouseY <= 590):
          redoMove(app)
        else:
          value = findValuePressed(app, mouseX, mouseY)
          row, col = app.selection
          if ((row,col) in app.movesMade or app.stateBoard.board[row][col] == 0) and app.creatingCustom == False and app.banningValues == False:
            if app.isAutoLegals == False:
              app.stateBoard.board[row][col] = value
            elif app.isAutoLegals == True:
              app.stateBoard.set(row, col, value)
            app.movesMade.append((row, col))
            checkGameOver(app)
          elif app.banningValues == True:
            if app.displayLegals == True:
              banLegals(app, app.stateBoard, value)
            elif app.displayNotes == True:
              changeNotes(app, app.notes, value)
          elif app.creatingCustom == True:
            inputtingCustomBoard(app, value)
    else: #gameOver is true
      if (160 <= mouseX <= 260) and (490 <= mouseY <= 540):
        app.selection = None
        app.gameOver = False
        app.takingScreenshot = True
      elif (265 <= mouseX <= 365) and (490 <= mouseY <= 540):
        app.boardIndex = random.randrange(0, 50)
        newGeneratedBoard(app)

def game_onStep(app):
  if app.takingScreenshot == True:
    if app.steps <= 7:
      app.steps += 1
    #next 3 lines modified from https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
    if app.steps == 1:
      app.stateBoard.board = copy.deepcopy(app.solvedBoard.board)
    if app.steps == 2:
      finishedImage = takeScreenshot1(app)
      finishedImage.save("finishedImage.png")
    if app.steps == 3:
      app.stateBoard.board = copy.deepcopy(app.originalBoard.board)
    #next 3 lines modified from https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
    if app.steps == 4:
      originalImage = takeScreenshot2(app)
      originalImage.save("originalImage.png")
    if app.steps == 5:
      #do the pdf stuff
      #rest of method modified from https://datatofish.com/images-to-pdf-python/
      og_1 = Image.open(r'/Users/annie/Downloads/15-112/sudoku term project/originalImage.png')
      og_1 = og_1.convert('RGB')

      f_1 = Image.open(r'/Users/annie/Downloads/15-112/sudoku term project/finishedImage.png')
      f_1 = f_1.convert('RGB')

      image_list = [f_1]
      og_1.save(r'/Users/annie/Downloads/15-112/sudoku term project/savedSudoku.pdf', save_all=True, append_images=image_list)
    if app.steps >7:
      app.gameOver = False
      newGeneratedBoard(app)

# modified from https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
def takeScreenshot1(app):
  print("taking screenshot")
  finishedImage = pyscreenshot.grab(bbox=(540, 220, 896, 576))
  return finishedImage

# modified from https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
def takeScreenshot2(app):
  originalImage = pyscreenshot.grab(bbox=(540, 220, 896, 576))
  return originalImage

def generateHint(app):
  app.selectionList = []
  app.displayHint = True
  row, col, val = firstHint(app)
  app.selection = (row, col)
  if row == None or col == None or val == None: #no first hint
    app.hintMessage = f'first hint didnt work'
    cells, values = secondHint(app)
    if cells == None or values == None: #no second hint
      app.hintMessage = f"no hints available"
    else: #do the second hint
      app.selectionList = list(cells)
      valuesStr = convertSetToString(values)
      bannedCells = otherCellsInRegion(app, cells)
      cellsStr = convertSetToStringCells(bannedCells)
      app.hintMessage = f'ban the values {valuesStr} at {cellsStr}'
  else: #do the first hint
    app.hintMessage = f'set the value at row {row} column {col} to be {val}'

def doHint(app):
  app.selectionList = []
  row, col, val = firstHint(app)
  app.selection = (row, col)
  if row == None or col == None or val == None: #no first hint
    print("first hint didn't work")
    cells, values = secondHint(app)
    if cells == None or values == None: #no second hint
      app.displayHint = True
      app.hintMessage = f"no hints available"
    else: #do the second hint
      bannedCells = otherCellsInRegion(app, cells)
      print(bannedCells)
      for cell in list(bannedCells):
        row2, col2 = cell
        app.stateBoard.ban(row2, col2, values)
      app.selectionList = set(bannedCells)
  else: #do the first hint
    app.stateBoard.set(row, col, val)
    app.movesMade.append((row, col))
    checkGameOver(app)

def otherCellsInRegion(app, cells):
  cells = list(cells)
  #check if theyre all in the same row region
  previousRowRegion = None
  currRowRegion = None
  sameRow = True
  for i in range(len(cells)):
    row, col = cells[i]
    currRowRegion = app.stateBoard.getRowRegion(row)
    if previousRowRegion != None and previousRowRegion != currRowRegion:
      sameRow = False
      break
    else:
      previousRowRegion = currRowRegion

  #check if theyre all in the same col region
  previousColRegion = None
  currColRegion = None
  sameCol = True
  for i in range(len(cells)):
    row, col = cells[i]
    currColRegion = app.stateBoard.getColRegion(col)
    if previousColRegion != None and previousColRegion != currColRegion:
      sameCol = False
      break
    else:
      previousColRegion = currColRegion

  #check if theyre all in the same block region
  previousBlockRegion = None
  currBlockRegion = None
  sameBlock = True
  for i in range(len(cells)):
    row, col = cells[i]
    currBlockRegion = app.stateBoard.getBlockRegionByCell(row, col)
    if previousBlockRegion != None and previousBlockRegion != currBlockRegion:
      sameBlock = False
      break
    else:
      previousBlockRegion = currBlockRegion

  finalSet = set()
  if sameRow == True:
    finalSet = finalSet.union(set(currRowRegion))
  if sameCol == True:
    finalSet = finalSet.union(set(currColRegion))
  if sameBlock == True:
    finalSet = finalSet.union(set(currBlockRegion))
  finalSet = finalSet.difference(set(cells))

  removeSet = set()
  for row, col in finalSet:
    if app.stateBoard.board[row][col]!=0:
      removeSet.add((row, col))

  finalSet = finalSet.difference(removeSet)

  return finalSet


def convertSetToString(sett):
  listS = list(sett)
  result = ''
  for char in listS:
    result = result + str(char) + ", "
  result = result [:-2]
  return result

def convertSetToStringCells(sett):
  listS = list(sett)
  result = ''
  for coords in listS:
    row, col = coords
    result = f'{result} row {row+1} column {col+1},'
  result = result [:-2]
  return result

def firstHint(app):
  #find singletons and return the row col val of the location
  rows, cols = len(app.stateBoard.board), len(app.stateBoard.board[0])
  for row in range(rows):
    for col in range(cols):
      if len(app.stateBoard.legals[row][col]) == 1:
        for value in app.stateBoard.legals[row][col]:
          singlet = value
          return (row, col, singlet)
  return (None, None, None)

def secondHint(app):
  for n in range(2, 6):
    for region in app.stateBoard.getAllRegions():
      cellCombinations = itertools.combinations(region, n)
      for allCells in cellCombinations:
        allValues = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], n)
        for values in allValues:
          if checkValuesInCombination(app, values, allCells):
            if checkIfLegalHint(app, allCells, values):
              return allCells, values
            else:
              return (None, None)
  return (None, None)

def checkIfLegalHint(app, allCells, values):
  dupState = State()
  dupState.board = copy.deepcopy(app.stateBoard.board)
  dupState.legals = copy.deepcopy(app.stateBoard.legals)

  bannedCellsDup = otherCellsInRegion(app, allCells)
  for cell in list(bannedCellsDup):
    rowDup, colDup = cell
    print("dup state bannin", rowDup, colDup, values)
    dupState.ban(rowDup, colDup, values)

  print(dupState.printLegals())
  print(app.stateBoard.printLegals())

  if dupState.legals == app.stateBoard.legals:
    return False
  return True


def checkValuesInCombination(app, values, allCells):
  seenValues = set()
  for cell in allCells:
    row, col = cell
    seenValues = seenValues.union(app.stateBoard.legals[row][col])
    if len(app.stateBoard.legals[row][col]) == 0:
      return False
  if seenValues != set(values):
    return False
  return True

def undoMove(app):
  if app.movesMade != []:
    moveToAdd = app.movesMade.pop()
    row, col = moveToAdd
    value = app.stateBoard.board[row][col]
    app.redoList.append((moveToAdd, value))
    app.stateBoard.set(row, col, 0)
    regenerateLegals(app)

def redoMove(app):
  if app.redoList != []:
    moveToDo, value = app.redoList.pop()
    row, col = moveToDo
    if app.isAutoLegals == False:
      app.stateBoard.board[row][col] = value
    elif app.isAutoLegals == True:
      app.stateBoard.set(row, col, value)
    app.movesMade.append(moveToDo)

def regenerateLegals(app):
  rows = len(app.stateBoard.board)
  cols = len(app.stateBoard.board[0])
  tempBoard = State()
  tempBoard.board = copy.deepcopy(app.stateBoard.board)
  app.stateBoard.board = [[0 for i in range(9)] for i in range(9)]
  app.stateBoard.legals = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for i in range(9)] for i in range(9)]
  for row in range(rows):
    for col in range(cols):
      app.stateBoard.set(row, col, tempBoard.board[row][col])

## makes typed input into state object
def inputtingCustomBoard(app, key):
  row, col = app.selection
  app.stateBoard.set(row, col, key)

def checkGameOver(app):
  updateLives(app)
  if app.lives <= 0:
    app.gameOver = True
    return
  rows = len(app.stateBoard.board)
  cols = len(app.stateBoard.board[0])
  for row in range(rows):
    for col in range(cols):
      if app.stateBoard.board[row][col] == 0:
        return
  app.gameOver = True
  if app.gameOver == True and app.competitionMode == True:
    #write a file
    writeFinalFile(app)

#modified from https://www.cs.cmu.edu/~112-3/notes/term-project.html
def writeFinalFile(app):
  contents = ''
  rows = len(app.stateBoard.board)
  cols = len(app.stateBoard.board[0])
  for row in range(rows):
    for col in range(cols):
      contents = contents + str(app.stateBoard.board[row][col]) + " "
    contents = contents.strip()
    contents = contents + '\n'
  # print(contents)
  writeFile('/Users/annie/Downloads/15-112/sudoku term project/competitionCompleted.txt', contents)

def updateLives(app):
  print(app.alreadyWrong)
  rows = len(app.stateBoard.board)
  cols = len(app.stateBoard.board[0])
  for row in range(rows):
    for col in range(cols):
      value = app.stateBoard.board[row][col]
      if value != app.solvedBoard.board[row][col] and value != 0 and (row, col) not in app.alreadyWrong:
        app.lives -= 1
        app.alreadyWrong.add((row, col))
        print(app.alreadyWrong)
        return

## creates the board
#modified from 5.3.6
def boardApp(app):
  app.rows = 9
  app.cols = 9
  app.boardLeft = 25
  app.boardTop = 75
  app.boardWidth = 350
  app.boardHeight = 350
  app.cellBorderWidth = 1
  app.selection = (0, 0)
  app.selectionList = []

#modified from 5.3.6
def drawBoard(app):
  for row in range(app.rows):
    for col in range(app.cols):
      drawCell(app, row, col)

#modified from 5.3.6
def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight, fill=None, border='black', borderWidth=2*app.cellBorderWidth)

#modified from 5.3.6
def getCellLeftTop(app, row, col):
  cellWidth, cellHeight = getCellSize(app)
  cellLeft = app.boardLeft + col * cellWidth
  cellTop = app.boardTop + row * cellHeight
  return (cellLeft, cellTop)

#modified from 5.3.6
def getCellSize(app):
  cellWidth = app.boardWidth / app.cols
  cellHeight = app.boardHeight / app.rows
  return (cellWidth, cellHeight)

## selecting the cell using keyboard
#modified from https://cs3-112-f22.academy.cs.cmu.edu/notes/4189
def moveSelection(app, drow, dcol):
  if app.selection != None:
    selectedRow, selectedCol = app.selection
    newSelectedRow = (selectedRow + drow) % app.rows
    newSelectedCol = (selectedCol + dcol) % app.cols
    app.selection = (newSelectedRow, newSelectedCol)
    app.selectionList = []

#taken from https://cs3-112-f22.academy.cs.cmu.edu/notes/4189
def drawCell(app, row, col):
  cellLeft, cellTop = getCellLeftTop(app, row, col)
  cellWidth, cellHeight = getCellSize(app)
  if (row, col) == app.selection or (row, col) in app.selectionList:
    color = 'lightskyblue'
  else:
    color = None
  drawRect(cellLeft, cellTop, cellWidth, cellHeight, fill=color, border='black', borderWidth=app.cellBorderWidth)

## selecting the cell using mouse
#taken from https://cs3-112-f22.academy.cs.cmu.edu/notes/4189
def getCell(app, x, y):
  dx = x - app.boardLeft
  dy = y - app.boardTop
  cellWidth, cellHeight = getCellSize(app)
  row = math.floor(dy / cellHeight)
  col = math.floor(dx / cellWidth)
  if (0 <= row < app.rows) and (0 <= col < app.cols):
    return (row, col)
  else:
    return None

## draws the numbers so that theyre centered
def drawNumbers(app):
  rows = len(app.stateBoard.board)
  cols = len(app.stateBoard.board[0])
  for row in range(rows):
    for col in range(cols):
      if app.stateBoard.board[row][col] == 0:
        pass
      else:
        if (row, col) in app.movesMade:
          if app.stateBoard.board[row][col] == app.solvedBoard.board[row][col]:
            color = "grey"
          else:
            if app.competitionMode == True:
              x = 10/0
            else: color = "red"
        else:
          color = "black"
        drawLabel(app.stateBoard.board[row][col], 44.5+39*col, 94.5+39*row, size = 20, fill = color)

def drawLegals(app):
  if app.displayLegals == True:
    rows = len(app.stateBoard.board)
    cols = len(app.stateBoard.board[0])
    rowKey = [32.5, 6.5, 19.5]
    #loops through each row and col of the board
    for row in range(rows):
      for col in range(cols):
        if app.stateBoard.board[row][col] != 0:
          pass
        else:
          if (row, col) in app.wrongLegals:
            if app.competitionMode == True:
              x = 10/0
            else: color = "red"
          else:
            color = "navy"
          #loop through the numbers in the set of legals
          for i in range(1, 10):
            if i in app.stateBoard.legals[row][col]: #if the number is in the set
              #find the coordinates for the number
              numX = i%3
              finX = rowKey[numX]
              numY = i/3
              if numY <= 1: finY = 6.5
              elif numY <= 2: finY = 19.5
              elif numY <= 3: finY = 32.5
              drawLabel(i, (finX+25) + 39*col, (finY+75) + 39*row, size = 10, fill = color)

def drawNotes(app):
  if app.displayNotes == True:
    rows = len(app.notes)
    cols = len(app.notes[0])
    rowKey = [32.5, 6.5, 19.5]
    #loops through each row and col of the board
    for row in range(rows):
      for col in range(cols):
        if app.stateBoard.board[row][col] != 0:
          pass
        else:
          if (len(app.notes[row][col]) != 1) or (int(app.solvedBoard.board[row][col]) not in set(app.notes[row][col])):
            if app.displayWrongNotes == True:
              color = "red"
            else:
              color = "darkViolet"
          #loop through the numbers in the set of legals
          for i in range(1, 10):
            if i in app.notes[row][col]: #if the number is in the set
              #find the coordinates for the number
              numX = i%3
              finX = rowKey[numX]
              numY = i/3
              if numY <= 1: finY = 6.5
              elif numY <= 2: finY = 19.5
              elif numY <= 3: finY = 32.5
              drawLabel(i, (finX+25) + 39*col, (finY+75) + 39*row, size = 10, fill = color)

## draws the lavender blocks background colors
def drawBlocks(app):
  drawRect(25, 75, 117, 117, fill = "lavender", opacity = 75)
  drawRect(258, 75, 117, 117, fill = "lavender", opacity = 75)
  drawRect(142, 192, 117, 117, fill = "lavender", opacity = 75)
  drawRect(25, 308, 117, 117, fill = "lavender", opacity = 75)
  drawRect(258, 308, 117, 117, fill = "lavender", opacity = 75)

## draws the number board at the bottom right
def drawNumberBoard(app):
  if app.banningValues == True and app.displayLegals == True:
    color = "cyan"
  elif app.banningValues == True and app.displayNotes == True:
    color = "indigo"
  else:
    color = "lightgreen"
  for i in range(3):
    for j in range(3):
      drawRect(210+55*i, 430+55*j, 50, 50, fill = color, border = "black", opacity = 20)
      value = findValuePressed(app, 211+55*i, 431+55*j)
      drawLabel(value, 235+55*i, 455+55*j, size = 20)
  drawRect(155, 485, 50, 50, fill = color, border = "black", opacity = 20)
  drawLabel(0, 180, 510, size = 20)
  #draw two more boxes for undo and redo for part 2
  drawRect(155,430, 50, 50, fill = "pink", border = "red", borderWidth = 1)
  drawLabel("Undo", 180, 455, size = 16, font = "monospace")
  drawRect(155,540, 50, 50, fill = "pink", border = "red", borderWidth = 1)
  drawLabel("Redo", 180, 565, size = 16, font = "monospace")

def drawBottomLeft(app):
  #top row, basic restart and hints functions
  drawCircle(45, 490, 15, fill = "pink", border = "red", borderWidth = 1)
  drawLabel("r", 45, 490)
  drawCircle(80, 490, 15, fill = "pink", border = "red", borderWidth = 1)
  drawLabel("h", 80, 490)
  drawCircle(115, 490, 15, fill = "pink", border = "red", borderWidth = 1)
  drawLabel("H", 115, 490)

  #second row, display notes, make notes, show wrong notes
  drawCircle(45, 525, 15, fill = "pink", border = "red", borderWidth = 1)
  if app.displayNotes == True:
    drawCircle(45, 525, 15, fill = "black", opacity = 20, border = "red", borderWidth = 1)
  drawLabel("N", 45, 525)
  drawCircle(80, 525, 15, fill = "pink", border = "red", borderWidth = 1)
  if app.banningValues == True:
    drawCircle(80, 525, 15, fill = "black", opacity = 20, border = "red", borderWidth = 1)
  drawLabel("M", 80, 525)
  drawCircle(115, 525, 15, fill = "pink", border = "red", borderWidth = 1)
  if app.displayWrongNotes == True:
    drawCircle(115, 525, 15, fill = "black", opacity = 20, border = "red", borderWidth = 1)
  drawLabel("W", 115, 525)

  #bottom row, (only display when modenum != 0) display legals, turn on/off autoupdate legals, autoplay singletons
  if app.modeNumber != 0:
    drawCircle(45, 560, 15, fill = "pink", border = "red", borderWidth = 1)
    if app.displayLegals == True:
      drawCircle(45, 560, 15, fill = "black", opacity = 20, border = "red", borderWidth = 1)
    drawLabel("d", 45, 560)
    drawCircle(80, 560, 15, fill = "pink", border = "red", borderWidth = 1)
    if app.isAutoLegals == True:
      drawCircle(80, 560, 15, fill = "black", opacity = 20, border = "red", borderWidth = 1)
    drawLabel("L", 80, 560)
    drawCircle(115, 560, 15, fill = "pink", border = "red", borderWidth = 1)
    drawLabel("p", 115, 560)

def drawBottomLeftCustom(app):
  drawRect(25, 435, 115, 150, fill = "green", opacity = 100)
  drawLabel("Save Board", 80, 500, size = 18, font = "monospace")
  drawLabel("Press 'S'", 80, 520, size = 20, font = "monospace" )

def drawLives(app):
  drawLabel("Lives Remaining:", 30, 440, align = "left", font = "monospace", size = 12, fill = "darkRed", bold = True)
  for i in range((app.lives)):
    # from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo1_drawing_images.py
    pilImage = app.image.image
    drawImage(app.image, 40+i*22, 460, align='center',
            width=pilImage.width//15,
            height=pilImage.height//15)

# from https://www.cs.cmu.edu/~112-3/notes/term-project.html demo1_drawing_images.py
def openMyImage(app):
  # Load the PIL image
  # image from https://www.freeiconspng.com/images/heart-png
  app.image = Image.open('heart.png')

  # Convert each PIL image to a CMUImage for drawing
  app.image = CMUImage(app.image)

## finds number on number board based on location
def findValuePressed(app, mouseX, mouseY):
  value = 0
  if (155 <= mouseX <= 205) and (485 <= mouseY <= 535):
    value = 0
  elif (210 <= mouseX <= 260) and (430 <= mouseY <= 480):
    value = 1
  elif (265 <= mouseX <= 315) and (430 <= mouseY <= 480):
    value = 2
  elif (320 <= mouseX <= 370) and (430 <= mouseY <= 480):
    value = 3
  elif (210 <= mouseX <= 260) and (485 <= mouseY <= 535):
    value = 4
  elif (265 <= mouseX <= 315) and (485 <= mouseY <= 535):
    value = 5
  elif (320 <= mouseX <= 370) and (485 <= mouseY <= 535):
    value = 6
  elif (210 <= mouseX <= 260) and (540 <= mouseY <= 590):
    value = 7
  elif (265 <= mouseX <= 315) and (540 <= mouseY <= 590):
    value = 8
  elif (320 <= mouseX <= 370) and (540 <= mouseY <= 590):
    value = 9
  return value

def banLegals(app, board, key):
  row, col = app.selection
  key = int(key)
  if key in board.legals[row][col]: #ban it
    values = {key}
    board.ban(row, col, values)
    if app.solvedBoard.board[row][col] in app.stateBoard.legals[row][col] and (row, col) in app.wrongLegals:
      app.wrongLegals.remove((row, col))
  else: #add it
    board.legals[row][col].add(key)
    if app.solvedBoard.board[row][col] != key:
      #make all legals red for that cell
      app.wrongLegals.add((row, col))

def changeNotes(app, board, key):
  row, col = app.selection
  key = int(key)
  if key in board[row][col]: #ban it
    board[row][col].remove(key)
  else: #add it
    board[row][col].add(key)

## autoplays one singleton
def autoPlaySingleton(app):
  if app.competitionMode == False:
    if app.modeNumber >= 1:
      rows, cols = len(app.stateBoard.board), len(app.stateBoard.board[0])
      for row in range(rows):
        for col in range(cols):
          if len(app.stateBoard.legals[row][col]) == 1:
            app.selection = (row, col) #select cell
            for value in app.stateBoard.legals[row][col]: #find the value of the singlet
              singlet = value
            if app.isAutoLegals == False:
              app.stateBoard.board[row][col] = singlet
            elif app.isAutoLegals == True:
              app.stateBoard.set(row, col, singlet)
            app.movesMade.append((row, col))
            # checkGameOver(app)
            return
      print("No more singletons!")

## to identify the mode number
def identifyModeNumber(key):
  if key == "!":
    return 1
  elif key == "@":
    return 2
  elif key == "#":
    return 3
  elif key == "$":
    return 4
  elif key == ")":
    return 0
  elif key == "C":
    return 5

################
# backtracker !!!
# used the first example to help structure the backtracker https://cs3-112-f22.academy.cs.cmu.edu/notes/4085
# used to generate the solution to compare what my code generated https://www.sudoku-solutions.com/index.php?section=sudoku9by9

def solveSudoku(app):
  if isCompletedSudoku(app.solvedBoard.board):
    return app.solvedBoard
  else:
    wasLegals = copy.deepcopy(app.solvedBoard.legals)
    wasBoard = copy.deepcopy(app.solvedBoard.board)
    row, col = findRowCol(app.solvedBoard)
    legalsAtRowCol = list(app.solvedBoard.legals[row][col])
    for i in range(len(legalsAtRowCol)):
      tryVal = legalsAtRowCol[i]
      app.solvedBoard.set(row, col, tryVal)
      if checkBoard(app.solvedBoard): #if it works rn
        #call something to move forward
        solution = solveSudoku(app)
        if solution != None:
          return solution
        app.solvedBoard.board = copy.deepcopy(wasBoard)
        app.solvedBoard.legals = copy.deepcopy(wasLegals)
      else:
        app.solvedBoard.board = copy.deepcopy(wasBoard)
        app.solvedBoard.legals = copy.deepcopy(wasLegals)
    return None

def findRowCol(board):
  rows = len(board.board)
  cols = len(board.board[0])
  lowestNumberOfLegals = None
  lowestRow = None
  lowestCol = None
  for row in range(rows):
    for col in range(cols):
      if (lowestNumberOfLegals == None and board.board[row][col] == 0) or (lowestNumberOfLegals != None and board.board[row][col] == 0 and len(board.legals[row][col]) < lowestNumberOfLegals):
        lowestNumberOfLegals = len(board.legals[row][col])
        lowestRow = row
        lowestCol = col
  return lowestRow, lowestCol

def checkBoard(board): #checks if there are any values where there's no legals
  rows = len(board.board)
  cols = len(board.board[0])
  for row in range(rows):
    for col in range(cols):
      if board.board[row][col] == 0 and len(board.legals[row][col]) == 0:
        return False
  if isLegalSudoku(board.board) == False:
    return False
  return True

def isCompletedSudoku(board):
  rows, cols = len(board), len(board[0])
  for row in range(rows):
    for col in range(cols):
      if board[row][col] == 0:
        return False
  if isLegalSudoku(board) == False:
    return False
  return True

def isLegalSudoku(grid):
    rows, cols = len(grid), len(grid[0])
    if (rows!=4) and (rows!=9):
        return False
    if (rows!=cols):
        return False

    for row in range(rows):
        if not isLegalRow(grid, row):
            return False
    for col in range(cols):
        if not isLegalCol(grid, col):
            return False
    blocks = rows
    for block in range(blocks):
        if not isLegalBlock(grid, block):
            return False
    return True

def isLegalRow(grid, row):
    return areLegalValues(grid[row])

def isLegalCol(grid, col):
    rows = len(grid)
    values = [grid[row][col] for row in range(rows)]
    return areLegalValues(values)

def isLegalBlock(grid, block):
    n = len(grid)
    blockSize = rounded(n**0.5)
    startRow = block // blockSize * blockSize
    startCol = block % blockSize * blockSize
    values = []
    for drow in range(blockSize):
        for dcol in range(blockSize):
            row, col = startRow + drow, startCol + dcol
            values.append(grid[row][col])
    return areLegalValues(values)

def areLegalValues(L):
    n = len(L)
    seen = set()

    for value in L:
        #value is an int
        if (type(value) != int):
            return False
        #value is in range
        if value<0 or value>n:
            return False
        #value is not a duplicate
        if value != 0 and value in seen:
            return False
        #value is legal
        seen.add(value)
    return True
################

###############
# state class #
###############

#method names taken from https://www.cs.cmu.edu/~112-3/notes/tp-sudoku-hints.html
class State:
  def __init__(self):
    self.board = [[0 for i in range(9)] for i in range(9)]
    self.legals = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for i in range(9)] for i in range(9)]

  def set(self, row, col, value):
    if value != 0:
      self.ban(row, col, {1, 2, 3, 4, 5, 6, 7, 8, 9})
      for i in range(9):
        self.ban(row, i, {value})
        self.ban(i, col, {value})
      blockNum = self.getBlock(row, col)
      rowCols = self.getBlockRegion(blockNum)
      for row1, col1 in rowCols:
        self.ban(row1, col1, {value})
    self.board[row][col] = value

  def ban(self, row, col, values):
    self.legals[row][col] = self.legals[row][col].difference(values)

  def unban(self, row, col, values):
    self.legals[row][col] = self.legals[row][col].union(values)

  def myCopy(self, other):
    self.board = copy.deepcopy(other.board)
    self.legals = copy.deepcopy(other.legals)

  def getRowRegion(self, row):
    return [(row, 0), (row, 1), (row, 2), (row, 3), (row, 4), (row, 5), (row, 6), (row, 7), (row, 8)]

  def getColRegion(self, col):
    return [(0, col), (1, col), (2, col), (3, col), (4, col), (5, col), (6, col), (7, col), (8, col)]

  def getBlockRegion(self, block):
    if block == 0:
      return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    elif block == 1:
      return [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    elif block == 2:
      return [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
    elif block == 3:
      return [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    elif block == 4:
      return [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
    elif block == 5:
      return [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
    elif block == 6:
      return [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
    elif block == 7:
      return [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
    elif block == 8:
      return [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]

  def getBlock(self, row, col):
    blockNum = -1
    if (0 <= row <= 2):
      if (0 <= col <= 2):
        blockNum = 0
      elif (3 <= col <= 5):
        blockNum = 1
      elif (6 <= col <= 8):
        blockNum = 2
    elif (3 <= row <= 5):
      if (0 <= col <= 2):
        blockNum = 3
      elif (3 <= col <= 5):
        blockNum = 4
      elif (6 <= col <= 8):
        blockNum = 5
    elif (6 <= row <= 8):
      if (0 <= col <= 2):
        blockNum = 6
      elif (3 <= col <= 5):
        blockNum = 7
      elif (6 <= col <= 8):
        blockNum = 8
    return blockNum

  def getBlockRegionByCell(self, row, col):
    blockNum = self.getBlock(row, col)
    return self.getBlockRegion(blockNum)

  def getCellRegions(self, row, col):
    totalList = []
    totalList.append(self.getRowRegion(row))
    totalList.append(self.getColRegion(col))
    totalList.append(self.getBlockRegionByCell(row, col))
    return totalList

  def getAllRegions(self):
    allRegions = []
    #rows
    for i in range(9):
      allRegions.append(self.getRowRegion(i))
    #cols
    for j in range(9):
      allRegions.append(self.getColRegion(j))
    #blocks
    for k in range(9):
      allRegions.append(self.getBlockRegion(k))
    return allRegions

  def getAllRegionsThatContainTargets(self, targets):
    allRegions = []
    #find the row col with ALL the targets
    rows = len(self.board)
    cols = len(self.board[0])
    for row in range(rows):
      for col in range(cols):
        if self.legals[row][col] == targets:
          allRegions.append(self.getRowRegion(row))
          allRegions.append(self.getColRegion(col))
          allRegions.append(self.getBlockRegionByCell(row, col))
    return allRegions

  def getAllRegionsThatContainAnyTarget(self, targets):
    allRegions = []
    #find the row col with ALL the targets
    rows = len(self.board)
    cols = len(self.board[0])
    targets = list(targets)
    for row in range(rows):
      for col in range(cols):
        for target in targets:
          if target in self.legals[row][col]:
            allRegions.append(self.getRowRegion(row))
            allRegions.append(self.getColRegion(col))
            allRegions.append(self.getBlockRegionByCell(row, col))
    return allRegions

  #code taken from https://www.cs.cmu.edu/~112-3/notes/tp-sudoku-hints.html Debug printing
  def printLegals(self):
          colWidth = 4
          for col in range(9):
              colWidth = max(colWidth, 1+max([len(self.legals[row][col]) for row in range(9)]))
          for row in range(9):
              for col in range(9):
                  label = ''.join([str(v) for v in sorted(self.legals[row][col])])
                  if label == '': label = '-'
                  print(f"{' '*(colWidth - len(label))}{label}", end='')
              print()

#code taken from https://www.cs.cmu.edu/~112-3/notes/tp-sudoku-hints.html Debug printing
#code taken from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing
def maxItemLength(a):
    maxLen = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            maxLen = max(maxLen, len(repr(a[row][col])))
    return maxLen

def print2dList(a):
    if a == []:
        print([])
        return
    print()
    rows, cols = len(a), len(a[0])
    maxCols = max([len(row) for row in a])
    fieldWidth = max(maxItemLength(a), len(f'col={maxCols-1}'))
    rowLabelSize = 5 + len(str(rows-1))
    rowPrefix = ' '*rowLabelSize+' '
    rowSeparator = rowPrefix + '|' + ('-'*(fieldWidth+3) + '|')*maxCols
    print(rowPrefix, end='  ')
    # Prints the column labels centered
    for col in range(maxCols):
        print(f'col={col}'.center(fieldWidth+2), end='  ')
    print('\n' + rowSeparator)
    for row in range(rows):
        # Prints the row labels
        print(f'row={row}'.center(rowLabelSize), end=' | ')
        # Prints each item of the row flushed-right but the same width
        for col in range(len(a[row])):
            print(repr(a[row][col]).center(fieldWidth+1), end=' | ')
        # Prints out missing cells in each column in case the list is ragged
        missingCellChar = chr(10006)
        for col in range(len(a[row]), maxCols):
            print(missingCellChar*(fieldWidth+1), end=' | ')
        print('\n' + rowSeparator)
    print()

def onAppStart(app):
  app.board = None

########
# main #
########

def main():
  runAppWithScreens(initialScreen='home', width=400, height = 600)

main()

