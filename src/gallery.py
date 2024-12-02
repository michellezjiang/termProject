from cmu_graphics import *
from storePlayer import *

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
    app.galleryWord = True
    app.drawFinishOn = False

def drawGalleryWord(app):
    if app.galleryWord:
        drawLabel('click to begin', app.width/2, app.height/2)

def drawEndPromptScreen(app):
    if not app.galleryWord:
        if app.allPlayers[app.nameIndex].prompt != None:
            drawRect(app.width/2, app.height/2, 600, 400, fill='white', border='darkGray', align='center')
            if app.nameIndex == 0:
                drawLabel(f'{app.allPlayers[app.nameIndex].name} decided on the prompt: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top')
                drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
                drawLabel(app.allPlayers[app.nameIndex].prompt, app.width/2- (560/2) + 10, app.height/2, align='left', size=25)
            else:
                drawLabel(f'{app.allPlayers[app.nameIndex].name} thought that drawing was: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top')
                drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
                drawLabel(app.allPlayers[app.nameIndex].prompt, app.width/2- (560/2) + 10, app.height/2, align='left', size=25)

def drawFinalLines(app):
    if not app.galleryWord:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[0])):
            for j in range(len(app.allPlayers[app.nameIndex].drawing[0][i])-1):
                drawLine(app.allPlayers[app.nameIndex].drawing[0][i][j][0], app.allPlayers[app.nameIndex].drawing[0][i][j][1], app.allPlayers[app.nameIndex].drawing[0][i][j+1][0], app.allPlayers[app.nameIndex].drawing[0][i][j+1][1], fill=app.allPlayers[app.nameIndex].drawing[1][i][0][0], lineWidth=app.allPlayers[app.nameIndex].drawing[1][i][0][1])

def drawFinalDragLines(app):
    if not app.galleryWord:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[2])):
            drawLine(app.allPlayers[app.nameIndex].drawing[2][i][0], app.allPlayers[app.nameIndex].drawing[2][i][1], app.allPlayers[app.nameIndex].drawing[2][i][2], app.allPlayers[app.nameIndex].drawing[2][i][3], fill=app.allPlayers[app.nameIndex].drawing[2][i][4], lineWidth=app.allPlayers[app.nameIndex].drawing[2][i][5])

def drawFinalStick(app):
    if not app.galleryWord:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[3])):
            if app.allPlayers[app.nameIndex].drawing[3][i][0] == 'sq':
                drawRect(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], app.allPlayers[app.nameIndex].drawing[3][i][3], fill=app.allPlayers[app.nameIndex].drawing[3][i][4])
            elif app.allPlayers[app.nameIndex].drawing[3][i][0] == 'cir':
                drawCircle(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], fill=app.allPlayers[app.nameIndex].drawing[3][i][4])
            elif app.allPlayers[app.nameIndex].drawing[3][i][0] == 'star':
                drawStar(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], 5)

def drawFinalText(app):
    if not app.galleryWord:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[4])):
            drawLabel(app.allPlayers[app.nameIndex].drawing[4][i], app.allPlayers[app.nameIndex].drawing[5][i][0], app.allPlayers[app.nameIndex].drawing[5][i][1], align='left-top', fill=app.allPlayers[app.nameIndex].drawing[5][i][2], size=app.allPlayers[app.nameIndex].drawing[5][i][3])

def drawDrawingScreen(app):
    if not app.galleryWord:
        if app.allPlayers[app.nameIndex].drawing != None:
            drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
            drawRect(app.canvasX, app.canvasY - app.canvasHeight/2 - 50, app.canvasWidth, 50, fill="white", align='center', border='darkGray')
            drawLabel(f'{app.allPlayers[app.nameIndex].name} drew:', app.canvasX - app.canvasWidth/2 + 18, app.canvasY - app.canvasHeight/2 - 50, size=20, align= 'left')
            drawFinalLines(app)
            drawFinalDragLines(app)
            drawFinalStick(app)
            drawFinalText(app)

def drawArrow(app):
    if not app.galleryWord:
        if app.allPlayers[app.nameIndex].drawing != None:
            drawRect(app.canvasX + app.canvasWidth/2, app.canvasY + app.canvasHeight/2 + 45 + 18, 45, 45, fill='white', border='darkGray', align='right-bottom')
            drawLabel(">", app.canvasX + app.canvasWidth/2 - 45/2, app.canvasY + app.canvasHeight/2 + 45 + 18 - 45/2, align='center', size=30)

        elif app.allPlayers[app.nameIndex].prompt != None:
            drawRect(app.width/2 + 300, app.height/2 + 200 + 45 + 18, 45, 45, fill='white', border='darkGray', align='right-bottom')
            drawLabel(">", app.width/2 + 300 - 45/2, app.height/2 + 200 + 45 + 18 - 45/2, align='center', size=30)

def gallery_onMousePress(app, mouseX, mouseY):
    if app.galleryWord:
        app.nameIndex = 0
        app.galleryWord = False
    if app.allPlayers[app.nameIndex].drawing != None:
        if ((app.canvasX + app.canvasWidth/2 - 45<= mouseX <= app.canvasX + app.canvasWidth/2) and 
            (app.canvasY + app.canvasHeight/2 + 18 <= mouseY <=app.canvasY + app.canvasHeight/2 + 45 + 18)):
            if app.nameIndex < len(app.allPlayers) - 1:
                app.nameIndex += 1
            else:
                app.drawFinishOn = True
    elif app.allPlayers[app.nameIndex].prompt != None:
        if ((app.width/2 + 300 - 45 <= mouseX <= app.width/2 + 300) and 
            (app.height/2 + 200 + 45 + 18 - 45 <= mouseY <= app.height/2 + 200 + 45 + 18)):
            if app.nameIndex < len(app.allPlayers) - 1:
                app.nameIndex += 1
            else:
                app.drawFinishOn = True

def drawFinish(app):
    if app.drawFinishOn:
        drawRect(0, 0, app.width, app.height, fill='white')
        drawLabel('finish', app.width/2, app.height/2)



