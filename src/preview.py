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


    ###########
    #GALLERY APPS
    ###########
    app.allPlayers = []
    app.canMove = False
    app.drawNextPreview = False
    app.galleryWord = True
    app.drawFinishOn = False

    app.erasedPositions = [[]]
    app.drawHomeIllum = False




def drawPreview(app):
    if app.drawNextPreview:
        drawRect(0, 0, app.width, app.height, fill='white')
        drawRect(app.canvasX, app.canvasY - app.canvasHeight/2 - 50, app.canvasWidth, 50, fill="white", align='center', border='darkGray')
        drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
        drawLabel(f'{app.playerNames[app.nameIndex]}, observe this drawing. ', app.canvasX - app.canvasWidth/2 + 18, app.canvasY - app.canvasHeight/2 - 50, size=20, align= 'left', font='monospace')
        for i in range(len(app.lines)):
            for j in range(len(app.lines[i])-1):
                drawLine(app.lines[i][j][0], app.lines[i][j][1], app.lines[i][j+1][0], app.lines[i][j+1][1], fill=app.penColorSize[i][0][0], lineWidth=app.penColorSize[i][0][1])
        drawPreviewScreen(app)
        drawLabel(f'click anywhere to contine',  app.width/2, app.canvasY+app.canvasHeight/2+15, fill='darkGray', align='center', font='monospace')



def drawPreviewLines(app):
    for i in range(len(app.allPlayers[-1].drawing[0])):
        for j in range(len(app.allPlayers[-1].drawing[0][i])-1):
            drawLine(app.allPlayers[-1].drawing[0][i][j][0], app.allPlayers[-1].drawing[0][i][j][1], app.allPlayers[-1].drawing[0][i][j+1][0], app.allPlayers[-1].drawing[0][i][j+1][1], fill=app.allPlayers[-1].drawing[1][i][0][0], lineWidth=app.allPlayers[-1].drawing[1][i][0][1])

def drawPreviewDragLines(app):
    for i in range(len(app.allPlayers[-1].drawing[2])):
        drawLine(app.allPlayers[-1].drawing[2][i][0], app.allPlayers[-1].drawing[2][i][1], app.allPlayers[-1].drawing[2][i][2], app.allPlayers[-1].drawing[2][i][3], fill=app.allPlayers[-1].drawing[2][i][4], lineWidth=app.allPlayers[-1].drawing[2][i][5])

def drawPreviewStick(app):
    for i in range(len(app.allPlayers[-1].drawing[3])):
        if app.allPlayers[-1].drawing[3][i][0] == 'sq':
            drawRect(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], app.allPlayers[-1].drawing[3][i][3], fill=app.allPlayers[-1].drawing[3][i][4])
        elif app.allPlayers[-1].drawing[3][i][0] == 'cir':
            drawCircle(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], fill=app.allPlayers[-1].drawing[3][i][4])
        elif app.allPlayers[-1].drawing[3][i][0] == 'star':
            drawStar(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], 5)

def drawPreviewText(app):
    for i in range(len(app.allPlayers[-1].drawing[4])):
        drawLabel(app.allPlayers[-1].drawing[4][i], app.allPlayers[-1].drawing[5][i][0], app.allPlayers[-1].drawing[5][i][1], align='left-top', fill=app.allPlayers[-1].drawing[5][i][2], size=app.allPlayers[-1].drawing[5][i][3])

def drawPreviewScreen(app):
    drawPreviewLines(app)
    drawPreviewDragLines(app)
    drawPreviewStick(app)
    drawPreviewText(app)

def preview_onMousePress(app, mouseX, mouseY):
    app.drawNextPreview = False
    setActiveScreen('prompt')