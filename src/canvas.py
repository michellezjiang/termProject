from cmu_graphics import *
from storePlayer import *
import string

def onAppStart(app):
    ##############
    #START PAGE APPS
    ##############
    #menu dimensions
    app.height = 800
    app.width = 800
    app.menuX = app.width/2
    app.menuY = app.height/2
    app.menuWidth = 400
    app.menuHeight = 500

    #logo
    app.logoX = app.width/2
    app.logoY = app.menuY - app.menuHeight/2 - 75

    #startButtons
    app.newGameX = app.width/2
    app.newGameY = app.height/2 - 100
    
    app.rulesX = app.width/2
    app.rulesY = app.height/2 + 100

    app.startButtonWidth = 300
    app.startButtonHeight = 50

    app.illumStartButton = False
    app.illumRulesButton = False

    ##############
    #RULES APP
    ##############
    #use same dimensions as menu
    app.drawRule1 = True
    app.drawRule2 = False
    app.drawRule3 = False
    app.drawRule4 = False
    app.drawRule5 = False

    app.arrowIllumButton = False
    app.resetIllumButton = False
    app.homeIllumButton = False

    ##############
    #SETUP APPS
    ##############
    app.numPlayersStr = ''
    app.numPlayersConfirmButton = False
    app.numPlayersConfirmButtonIllum = False
    app.numPlayersType = False
    app.numPlayersShow = False
    app.numPlayersConfirmed = False

    app.playerNames = []
    app.nameIndex = 1
    app.nameType = False
    app.name = ''
    app.nameConfirm = False
    app.nameConfirmButtonIllum = False


    ###########
    #PROMPT APPS
    ###########
    app.writeScreen = True
    app.typePrompt = False
    app.prompt = ''
    app.promptConfirm = False
    app.promptIllum = False
    app.promptList = []

    #canvas dimensions
    app.height = 800
    app.width = 800
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width/2              #align = 'center'
    app.canvasY = app.height/2             #align = 'center'

    #default pen
    app.mode = 'pen'
    app.color = 'black'
    app.size = 'med'
    app.penColor = 'black'
    app.penSize = 3
    app.penQualities = (app.penColor, app.penSize)

    #storing free draw points
    app.lines = [[]]
    app.penColorSize = [[]]

    app.eraseCircle = False
    app.eraseCircleX = None
    app.eraseCircleY = None
    
    #testing
    app.drawmode = True

    #canvas selecting variables
    app.blackSelected = True
    app.redSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.yellowSelected = False, False, False, False, False
    app.penModeIllum, app.shapeModeIllum, app.eraseModeIllum, app.trashModeIllum, app.lineModeIllum, app.textModeIllum = False, False, False, False, False, False
    app.xLargeSelect, app.largeSelect, app.smallSelect = False, False, False
    app.mediumSelect = True
    app.penBack = 'plum'
    app.lineBack, app.textBack, app.deleteBack, app.shapeBack, app.eraseBack = 'white', 'white', 'white', 'white', 'white'
    app.checkIllum = False

    #textMode
    app.text = ''
    app.textModeType = False
    app.textX = None
    app.textY = None
    app.textPositions = []
    app.textList = []

    #lineMode
    app.lineDragMode = False
    app.dragLinePositions = []
    app.lineStartX = None
    app.lineStartY = None
    app.lineEndX = None
    app.lineEndY = None

    #shapeMode
    app.shapeSticker = None
    app.stickX, app.stickY = None, None
    app.stickPos = []


    ###########
    #GALLERY APPS
    ###########
    app.allPlayers = []
    app.canMove = False
    app.drawNextPreview = False
    app.galleryWord = True
    app.drawFinishOn = False

#####temporary variables
    app.erasedPositions = [[]]
    app.drawHomeIllum = False


def drawCanvas(app):
    bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/7035853.jpg')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/7035853.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.45, height=bg1Height*0.45)
    drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
    for i in range(len(app.lines)):
        for j in range(len(app.lines[i])-1):
            drawLine(app.lines[i][j][0], app.lines[i][j][1], app.lines[i][j+1][0], app.lines[i][j+1][1], fill=app.penColorSize[i][0][0], lineWidth=app.penColorSize[i][0][1])



def onResize(app):
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width/2              
    app.canvasY = app.height/2      


def drawEraser(app):
    if app.mode=='erase' and app.eraseCircle:
        drawCircle(app.eraseCircleX, app.eraseCircleY, 10, border='black', fill='white')
            
def canvas_onMouseRelease(app, mouseX, mouseY):
    app.drawmode = False
    if app.eraseCircle == True:
        app.eraseCircle = False
    if app.mode == 'pen':
        app.penColorSize.append([])
        app.lines.append([])
    if app.mode == 'delete':
        app.deleteMode = False
        app.deleteBack = 'white'
    if app.mode == 'line' and (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
        and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
        if app.lineEndX != None:
            app.dragLinePositions.append([app.lineStartX, app.lineStartY, app.lineEndX, app.lineEndY, app.penColor, app.penSize])
        app.lineStartX = None
        app.lineStartY = None
        app.lineEndX = None
        app.lineEndY = None
        app.lineDragMode = False

def drawPopUp(app):
    #all three images are from Freepik Flaticon
    if app.mode=='shape':
        drawRect(0, 0, app.width, app.height, fill='black', opacity = 70)
        drawRect(app.width/2, app.height/2, 300, 400, fill='white', align='center')
        drawRect(app.width/2 - 90, app.height/2 - 80, 60, 60, fill='white', border='black')
        squareWidth, squareHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/black-square.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/black-square.png', app.width/2 - 90 + 30, app.height/2 - 80 + 30, width=squareWidth*0.07, height=squareHeight*0.07, align='center')
        drawRect(app.width/2 + 30, app.height/2 - 80, 60, 60, fill='white', border='black')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/new-moon.png', app.width/2 + 60, app.height/2 - 80 + 30, width=squareWidth*0.07, height=squareHeight*0.07, align='center')
        drawRect(app.width/2 - 30, app.height/2 + 20, 60, 60, fill='white', border='black')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/star.png', app.width/2, app.height/2 + 50, width=squareWidth*0.07, height=squareHeight*0.07, align='center')
        
                
def distanceBetweenPoints(point1, point2):
    return distance(point1[0], point1[1], point2[0], point2[1])
    
def midpoint(point1, point2):
    return ((point1[0]+point2[0])/2, (point2[1]+point2[1])/2)


def canvas_onMouseDrag(app, mouseX, mouseY):
    if app.mode =='pen' and app.drawmode:
        app.penQualities = (app.penColor, app.penSize)
        if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
            app.penColorSize[-1].append(app.penQualities)
            app.lines[-1].append((mouseX, mouseY))

    if app.mode == 'erase':
        if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
            app.eraseCircle = True
            app.eraseCircleX = mouseX
            app.eraseCircleY = mouseY
            app.erasedPositions[-1].append((app.eraseCircleX, app.eraseCircleY))
            # for quality in app.coloredLines:
            #     newPoints = []
            #     for point in app.coloredLines[quality]:
            #         distance = ((mouseX - point[0])**2 + (mouseY - point[1])**2)**0.5
            #         if distance > 10:
            #             newPoints.append(point)
            #     app.coloredLines[quality] = newPoints

    if app.mode == 'line' and app.lineDragMode:
        app.lineEndX = mouseX
        app.lineEndY = mouseY

def drawLines(app):
    if app.lineDragMode and app.lineStartX != None and app.lineEndX != None:
        drawLine(app.lineStartX, app.lineStartY, app.lineEndX, app.lineEndY, fill=app.penColor, lineWidth=app.penSize)

    for i in range(len(app.dragLinePositions)):
        drawLine(app.dragLinePositions[i][0], app.dragLinePositions[i][1], app.dragLinePositions[i][2], app.dragLinePositions[i][3], fill=app.dragLinePositions[i][4], lineWidth=app.dragLinePositions[i][5])

def canvas_onMousePress(app, mouseX, mouseY):
    if ((app.canvasX - (app.canvasWidth/2) + 500 + 180 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + 500 + 180 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 110 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)) and not app.drawNextPreview:
        newPlayer = Player(app.playerNames[app.nameIndex], None, [app.lines, app.penColorSize, app.dragLinePositions, app.stickPos, app.textList, app.textPositions])
        app.allPlayers.append(newPlayer)
        if app.nameIndex == len(app.playerNames) - 1:
            setActiveScreen('gallery')

        elif app.nameIndex < len(app.playerNames) - 1:
            app.drawNextPreview = True
            app.nameIndex += 1
            app.mode = 'pen'
            app.color = 'black'
            app.size = 'med'
            app.penColor = 'black'
            app.penSize = 3
            app.penQualities = (app.penColor, app.penSize)

            #storing free draw points
            app.lines = [[]]
            app.penColorSize = [[]]

            app.eraseCircle = False
            app.eraseCircleX = None
            app.eraseCircleY = None
            
            #testing
            app.drawmode = True

            #canvas selecting variables
            app.blackSelected = True
            app.redSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.yellowSelected = False, False, False, False, False
            app.penModeIllum, app.shapeModeIllum, app.eraseModeIllum, app.trashModeIllum, app.lineModeIllum, app.textModeIllum = False, False, False, False, False, False
            app.xLargeSelect, app.largeSelect, app.smallSelect = False, False, False
            app.mediumSelect = True
            app.penBack = 'mediumPurple'
            app.lineBack, app.textBack, app.deleteBack, app.shapeBack, app.eraseBack = 'white', 'white', 'white', 'white', 'white'

            #textMode
            app.text = ''
            app.textModeType = False
            app.textX = None
            app.textY = None
            app.textPositions = []
            app.textList = []

            #lineMode
            app.lineDragMode = False
            app.dragLinePositions = []
            app.lineStartX = None
            app.lineStartY = None
            app.lineEndX = None
            app.lineEndY = None

            #shapeMode
            app.shapeSticker = None
            app.stickX, app.stickY = None, None
            app.stickPos = []

            setActiveScreen('preview')

    if app.mode == 'shape' and ((mouseX < app.width/2 - 150 or mouseX > app.width/2 + 150)
        or (mouseY < app.height/2 - 200 or mouseY > app.width/2 + 200)) and not app.drawNextPreview:
        app.mode = 'pen'
    changeColor(app, mouseX, mouseY)
    changeSize(app, mouseX, mouseY)
    changeMode(app, mouseX, mouseY)
    buttonBack(app)
    app.drawmode = True

    if app.mode == 'text' and (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
        and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2) and not app.drawNextPreview:
        app.textModeType = True
        app.textX = mouseX
        app.textY = mouseY

    if app.mode == 'line' and (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
        and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2) and not app.drawNextPreview:
        app.lineDragMode = True
        app.lineStartX = mouseX
        app.lineStartY = mouseY

    if app.mode == 'shape' and ((app.width/2 - 150<= mouseX <= app.width/2 + 150) and (app.height/2 - 200 <= mouseY <= app.height/2 + 200)) and not app.drawNextPreview:
        if ((app.width/2 - 90<= mouseX <= app.width/2 - 90 + 60)
            and (app.height/2 - 80<= mouseY <= app.height/2-80+60)) :
            app.shapeSticker = 'sq'
            app.mode = 'shapeDraw'

        elif ((app.width/2 + 30<= mouseX <= app.width/2 + 30+60)
            and (app.height/2 - 80<= mouseY <= app.height/2-80+60)):
            app.shapeSticker = 'cir'
            app.mode = 'shapeDraw'


        elif ((app.width/2 - 30<= mouseX <= app.width/2 - 30 + 60)
            and (app.height/2 + 20<= mouseY <= app.height/2 + 20+60)):
            app.shapeSticker = 'star'
            app.mode = 'shapeDraw'

    if app.mode == 'shapeDraw' and (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
        and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2) and not app.drawNextPreview:
        app.stickX = mouseX
        app.stickY = mouseY


    
        

def drawStick(app):
    if app.mode == 'shapeDraw':
        if app.stickX != None and app.shapeSticker=='sq':
            drawRect(app.stickX, app.stickY, app.penSize**2, app.penSize**2, fill=app.penColor)
            drawCircle(app.stickX, app.stickY, 5, fill='darkGray')
        elif app.stickX != None and app.shapeSticker == 'cir':
            drawCircle(app.stickX, app.stickY, app.penSize**2, fill=app.penColor)
            drawCircle(app.stickX, app.stickY, 5, fill='darkGray')
        elif app.stickX != None and app.shapeSticker == 'star':
            drawStar(app.stickX, app.stickY, app.penSize**2, 5, fill=app.penColor)
            drawCircle(app.stickX, app.stickY, 5, fill='darkGray')
    for i in range(len(app.stickPos)):
        if app.stickPos[i][0] == 'sq':
            drawRect(app.stickPos[i][1], app.stickPos[i][2], app.stickPos[i][3], app.stickPos[i][3], fill=app.stickPos[i][4])
        elif app.stickPos[i][0] == 'cir':
            drawCircle(app.stickPos[i][1], app.stickPos[i][2], app.stickPos[i][3], fill=app.stickPos[i][4])
        elif app.stickPos[i][0] == 'star':
            drawStar(app.stickPos[i][1], app.stickPos[i][2], app.stickPos[i][3], 5, fill=app.stickPos[i][4])

    


def canvas_onKeyPress(app, key):
    if app.textModeType:
        if key in string.ascii_letters or key in string.digits or key in string.punctuation:
            app.text += key
        elif key == 'backspace':
            app.text = app.text[:-1]
        elif key == 'space':
            app.text += ' '
        elif key == 'enter':
            app.textList.append(app.text)
            app.textPositions.append((app.textX, app.textY, app.penColor, app.penSize**2))
            app.text = ''
            app.textModeType = False

    if app.mode == 'shapeDraw':
        if key == 'enter':
            app.stickPos.append((app.shapeSticker, app.stickX, app.stickY, app.penSize**2, app.penColor))
            app.stickX = None
            app.stickY = None
            app.mode = 'pen'



def writeText(app):
    if app.textModeType == True:
        drawCircle(app.textX, app.textY, 5, fill='darkGray')
        drawLabel(app.text, app.textX, app.textY, align='left-top', fill=app.penColor, size=app.penSize**2)
    for i in range(len(app.textPositions)):
        drawLabel(app.textList[i], app.textPositions[i][0], app.textPositions[i][1], align='left-top', fill=app.textPositions[i][2], size=app.textPositions[i][3])

def colorButtons(app):
    drawCircle(app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 35, 25, fill='red')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 35, 25, fill='yellow')
    drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 35, 25, fill='blue')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 110, 25, fill='green')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 110, 25, fill='white')
    drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 110, 25, fill='black')
    drawLine(app.canvasX - (app.canvasWidth/2) + (30) + 200, app.canvasY + (app.canvasHeight/2) + 10, app.canvasX - (app.canvasWidth/2) + (30) + 200, app.canvasY + (app.canvasHeight/2) + 135, fill='black')

def opacitySlider(app):
    drawLine(app.canvasX - (app.canvasWidth/2) + (30) + 505, app.canvasY + (app.canvasHeight/2) + 110, app.canvasX - (app.canvasWidth/2) + 500 + 180 - 25 - 25, app.canvasY + (app.canvasHeight/2) + 110, fill='darkGray')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 180 - 25 - 25, app.canvasY + (app.canvasHeight/2) + 110, 7, fill='black')
    drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 500, app.canvasY + (app.canvasHeight/2) + 110, 7, fill=None, border='darkGray')

def completeDrawing(app):
    #icon from Flaticon Freepik
    drawRect(app.canvasX - (app.canvasWidth/2) + 500 + 180, app.canvasY + (app.canvasHeight/2) + 110, 50,50, fill=None, align='center', border='black')
    checkWidth, checkHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/check.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.canvasX - (app.canvasWidth/2) + 500 + 180, app.canvasY + (app.canvasHeight/2) + 110, width=checkWidth*0.06, height=checkWidth*0.06, align='center')

def changeColor(app, mouseX, mouseY):
    if distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 35) <= 25:
        app.penColor = 'red'
        app.redSelected = True
        app.yellowSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.blackSelected = False, False, False, False, False

    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 35) <= 25:
        app.penColor = 'yellow'
        app.yellowSelected = True
        app.redSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.blackSelected = False, False, False, False, False

    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 35) <= 25:
        app.penColor = 'blue'
        app.blueSelected = True
        app.redSelected, app.yellowSelected, app.greenSelected, app.whiteSelected, app.blackSelected = False, False, False, False, False

    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 110) <= 25:
        app.penColor = 'green'
        app.greenSelected = True
        app.redSelected, app.blueSelected, app.yellowSelected, app.whiteSelected, app.blackSelected = False, False, False, False, False

    
    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 110) <= 25:
        app.penColor = 'white'
        app.whiteSelected = True
        app.redSelected, app.blueSelected, app.greenSelected, app.yellowSelected, app.blackSelected = False, False, False, False, False


    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 110) <= 25:
        app.penColor = 'black'
        app.blackSelected = True        
        app.redSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.yellowSelected = False, False, False, False, False


def sizeButtons(app):
    drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 500, app.canvasY + (app.canvasHeight/2) + 35, 8, fill='black')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 80, app.canvasY + (app.canvasHeight/2) + 35, 12, fill='black')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 130, app.canvasY + (app.canvasHeight/2) + 35, 15, fill='black')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 180, app.canvasY + (app.canvasHeight/2) + 35, 18, fill='black')

def selectSize(app):
    if app.smallSelect:
        drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 500, app.canvasY + (app.canvasHeight/2) + 35, 13, fill=None, border='black')
    if app.mediumSelect:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 80, app.canvasY + (app.canvasHeight/2) + 35, 17, border='black', fill=None)
    if app.largeSelect:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 130, app.canvasY + (app.canvasHeight/2) + 35, 20, border='black', fill=None)
    if app.xLargeSelect:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 500 + 180, app.canvasY + (app.canvasHeight/2) + 35, 23, border='black', fill=None)

def changeSize(app, mouseX, mouseY):
    if app.mode == 'pen' or app.mode=='text' or app.mode=='line' or app.mode=='shapeDraw':
        if distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + (30) + 500, app.canvasY + (app.canvasHeight/2) + 35) <= 8:
            app.penSize = 1
            app.smallSelect = True
            app.mediumSelect, app.largeSelect, app.xLargeSelect = False, False, False

        elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 500 + 80, app.canvasY + (app.canvasHeight/2) + 35) <= 12:
            app.penSize = 3
            app.mediumSelect = True
            app.smallSelect, app.largeSelect, app.xLargeSelect = False, False, False

        elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 500 + 130, app.canvasY + (app.canvasHeight/2) + 35) <= 15:
            app.penSize = 5
            app.largeSelect = True
            app.mediumSelect, app.smallSelect, app.xLargeSelect = False, False, False

        elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 500 + 180, app.canvasY + (app.canvasHeight/2) + 35) <= 18:
            app.penSize = 7
            app.xLargeSelect = True
            app.mediumSelect, app.largeSelect, app.smallSelect = False, False, False

    if app.mode == 'erase':
        if distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15, app.canvasY + (app.canvasHeight/2) + 75,) <= 8:
            app.penSize = 2
            app.penMode = True

        elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15 + 50, app.canvasY + (app.canvasHeight/2) + 75) <= 12:
            app.penSize = 4

        elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15 + 100, app.canvasY + (app.canvasHeight/2) + 75) <= 15:
            app.penSize = 4.5


def changeMode(app, mouseX, mouseY):
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 250 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 250 + 25) and 
        (app.canvasY + (app.canvasHeight/2) + 35 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 35 + 25)):
        app.mode = 'pen'
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 250 - 25<=mouseX<= app.canvasX - (app.canvasWidth/2) + (30) + 250+ 25) and 
        (app.canvasY + (app.canvasHeight/2) + 110 - 25<= mouseY<=app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.mode='erase'
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 325 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 325 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 35 - 25<= mouseY <=app.canvasY + (app.canvasHeight/2) + 35+ 25)):
        app.mode='shape'
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 325 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 325 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 110 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.mode='line'
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 400 - 25<= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 400 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 35 - 25<= mouseY <=app.canvasY + (app.canvasHeight/2) + 35+ 25)):     
        app.mode='text'
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 400 - 25<= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 400 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 110 - 25<= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.lines = [[]]  
        app.penColorSize = [[]]
        app.textList = []
        app.textPositions = []
        app.stickPos = []
        app.mode='delete'


def otherButtons(app):
    ########
    #All icons from Flaticon Pixel Perfect and Freepik
    ########
    #pen
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 250,app.canvasY + (app.canvasHeight/2) + 35,50,50, fill=app.penBack, align='center', border='black')
    pencilWidth, pencilHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/pencil.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/pencil.png', app.canvasX - (app.canvasWidth/2) + (30) + 250, app.canvasY + (app.canvasHeight/2) + 35, width=pencilWidth*0.06, height=pencilHeight*0.06, align='center')
    #eraser
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 250,app.canvasY + (app.canvasHeight/2) + 110,50,50, fill=app.eraseBack, align='center', border='black')
    eraserHeight, eraserWidth = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/eraser.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/eraser.png', app.canvasX - (app.canvasWidth/2) + (30) + 250, app.canvasY + (app.canvasHeight/2) + 110, width=eraserWidth*0.06, height=eraserHeight*0.06, align='center')
    #shapes
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 325,app.canvasY + (app.canvasHeight/2) + 35,50,50, fill=app.shapeBack, align='center', border='black')
    shapeHeight, shapeWidth = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/shape.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/shape.png', app.canvasX - (app.canvasWidth/2) + (30) + 325,app.canvasY + (app.canvasHeight/2) + 35, width=shapeWidth*0.06, height=shapeHeight*0.06, align='center')
    #line
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 325, app.canvasY + (app.canvasHeight/2) + 110,50,50, fill=app.lineBack, align='center', border='black')
    lineHeight, lineWidth = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/line-segment.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/line-segment.png', app.canvasX - (app.canvasWidth/2) + (30) + 325, app.canvasY + (app.canvasHeight/2) + 110, width=lineWidth*0.06, height=lineHeight*0.06, align='center')
    #text
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 35,50,50, fill=app.textBack, align='center', border='black')
    textHeight, textWidth = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/type-removebg-preview.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/type-removebg-preview.png', app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 35, width=textWidth*0.06, height=textHeight*0.06, align='center')
    #delete
    drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 110,50,50, fill=app.deleteBack, align='center', border='black')
    deleteHeight, deleteWidth = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/bin.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/bin.png', app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 110, width=textWidth*0.06, height=textHeight*0.06, align='center')
    drawLine(app.canvasX - (app.canvasWidth/2) + (30) + 450, app.canvasY + (app.canvasHeight/2) + 10, app.canvasX - (app.canvasWidth/2) + (30) + 450, app.canvasY + (app.canvasHeight/2) + 135, fill='black')

def buttonBack(app):
    if app.mode=='pen':
        app.penBack = 'mediumPurple'
    else:
        app.penBack = 'white'

    if app.mode=='erase':
        app.eraseBack = 'mediumPurple'
    else:
        app.eraseBack = 'white'

    if app.mode=='shape' or app.mode=='shapeDraw':
        app.shapeBack = 'mediumPurple'
    else:
        app.shapeBack = 'white'

    if app.mode=='line':
        app.lineBack = 'mediumPurple'
    else:
        app.lineBack = 'white'

    if app.mode=='text':
        app.textBack = 'mediumPurple'
    else:
        app.textBack = 'white'

    if app.mode=='delete':
        app.deleteBack = 'mediumPurple'
    else:
        app.deleteBack = 'white'
        
def selectColor(app):
    if app.blackSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 110, 30, fill=None, border='black')
    elif app.yellowSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 35, 30, fill=None, border='black')
    elif app.redSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 35, 30, fill=None, border='black')
    elif app.blueSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + (30) + 150, app.canvasY + (app.canvasHeight/2) + 35, 30, fill=None, border='black')
    elif app.greenSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 30, app.canvasY + (app.canvasHeight/2) + 110, 30, fill=None, border='black')
    elif app.whiteSelected:
        drawCircle(app.canvasX - (app.canvasWidth/2) + 30 + 75, app.canvasY + (app.canvasHeight/2) + 110, 30, fill=None, border='black')

def canvas_onMouseMove(app, mouseX, mouseY):
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 250 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 250 + 25) and 
        (app.canvasY + (app.canvasHeight/2) + 35 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 35 + 25)):
        app.penModeIllum = True
    else: 
        app.penModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 250 - 25<=mouseX<= app.canvasX - (app.canvasWidth/2) + (30) + 250+ 25) and 
        (app.canvasY + (app.canvasHeight/2) + 110 - 25<= mouseY<=app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.eraseModeIllum = True
    else:
        app.eraseModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 325 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 325 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 35 - 25<= mouseY <=app.canvasY + (app.canvasHeight/2) + 35+ 25)):
        app.shapeModeIllum = True
    else:
        app.shapeModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 325 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 325 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 110 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.lineModeIllum = True
    else:
        app.lineModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 400 - 25<= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 400 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 35 - 25<= mouseY <=app.canvasY + (app.canvasHeight/2) + 35+ 25)):
        app.textModeIllum = True
    else:
        app.textModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + (30) + 400 - 25<= mouseX <= app.canvasX - (app.canvasWidth/2) + (30) + 400 + 25)
        and (app.canvasY + (app.canvasHeight/2) + 110 - 25<= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.trashModeIllum = True
    else:
        app.trashModeIllum = False
    if ((app.canvasX - (app.canvasWidth/2) + 500 + 180 - 25 <= mouseX <= app.canvasX - (app.canvasWidth/2) + 500 + 180 + 25) and 
        (app.canvasY + (app.canvasHeight/2) + 110 - 25 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 110 + 25)):
        app.checkIllum = True
    else:
        app.checkIllum = False

def illumModes(app):
    if app.penModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 250,app.canvasY + (app.canvasHeight/2) + 35,50,50, fill='lavender', align='center', border='darkGray', opacity=60)
    if app.eraseModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 250,app.canvasY + (app.canvasHeight/2) + 110,50,50, fill='lavender', align='center', border='darkGray', opacity=60)
    if app.shapeModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 325,app.canvasY + (app.canvasHeight/2) + 35,50,50, fill='lavender', align='center', border='darkGray', opacity=60)
    if app.lineModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 325, app.canvasY + (app.canvasHeight/2) + 110,50,50, fill='lavender', align='center', border='darkGray', opacity=60)
    if app.textModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 35,50,50, fill='lavender', align='center', border='darkGray', opacity=60)
    if app.trashModeIllum:
        drawRect(app.canvasX - (app.canvasWidth/2) + (30) + 400, app.canvasY + (app.canvasHeight/2) + 110,50,50, fill='lavender', align='center', border='darkGray', opacity=60)

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5

def drawPromptonCanvas(app):
    drawRect(app.canvasX, app.canvasY - app.canvasHeight/2 - 50, app.canvasWidth, 50, fill="white", align='center', border='darkGray')
    if len(app.promptList) > 0:
        drawLabel(f'{app.playerNames[app.nameIndex]}, draw: ' + app.promptList[-1], app.canvasX - app.canvasWidth/2 + 18, app.canvasY - app.canvasHeight/2 - 50, size=20, align= 'left', font='monospace')