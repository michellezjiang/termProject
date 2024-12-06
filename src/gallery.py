from cmu_graphics import *
from storePlayer import *
from similarityChecker import *


def drawGalleryWord(app):
    if app.galleryWord and not (app.drawFinishOn):
        #Image by Freepik
        bgW, bgH = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg', app.width/2, app.height/2, align='center', width=0.2*bgW, height=0.2*bgH, opacity=60)
        #Font by 1001 fonts Fontalicious
        gW, gH = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/gallery.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/gallery.png', app.width/2, app.height/2, align='center', width=0.45*gW, height=0.45*gH)
        drawLabel('click to begin', app.width/2, app.height/2 + 100, align='center', fill='black', font='monospace', size=15, bold=True)

def drawEndPromptScreen(app):
    if not app.galleryWord and (not app.drawFinishOn or not app.scoresOn):
        if app.allPlayers[app.nameIndex].prompt != None:
            #Image by Freepik
            bgW, bgH = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg')
            drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg', app.width/2, app.height/2, align='center', width=0.25*bgW, height=0.25*bgH, opacity=60)
            drawRect(app.width/2, app.height/2, 600, 400, fill='white', border='black', align='center')
            if app.nameIndex == 0:
                drawLabel(f'{app.allPlayers[app.nameIndex].name} decided on the prompt: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top', font='monospace')
                drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
                drawLabel(app.allPlayers[app.nameIndex].prompt, app.width/2- (560/2) + 10, app.height/2, align='left', size=18, font='monospace')
            else:
                drawLabel(f'{app.allPlayers[app.nameIndex].name} thought that drawing was: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top', font='monospace')
                drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
                drawLabel(app.allPlayers[app.nameIndex].prompt, app.width/2- (560/2) + 10, app.height/2, align='left', size=20, font='monospace')

def drawFinalLines(app):
    if not app.galleryWord and not app.drawFinishOn:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[0])):
            for j in range(len(app.allPlayers[app.nameIndex].drawing[0][i])-1):
                drawLine(app.allPlayers[app.nameIndex].drawing[0][i][j][0], app.allPlayers[app.nameIndex].drawing[0][i][j][1], app.allPlayers[app.nameIndex].drawing[0][i][j+1][0], app.allPlayers[app.nameIndex].drawing[0][i][j+1][1], fill=app.allPlayers[app.nameIndex].drawing[1][i][0][0], lineWidth=app.allPlayers[app.nameIndex].drawing[1][i][0][1])

def drawFinalDragLines(app):
    if not app.galleryWord and not app.drawFinishOn:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[2])):
            drawLine(app.allPlayers[app.nameIndex].drawing[2][i][0], app.allPlayers[app.nameIndex].drawing[2][i][1], app.allPlayers[app.nameIndex].drawing[2][i][2], app.allPlayers[app.nameIndex].drawing[2][i][3], fill=app.allPlayers[app.nameIndex].drawing[2][i][4], lineWidth=app.allPlayers[app.nameIndex].drawing[2][i][5])

def drawFinalStick(app):
    if not app.galleryWord and not app.drawFinishOn:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[3])):
            if app.allPlayers[app.nameIndex].drawing[3][i][0] == 'sq':
                drawRect(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], app.allPlayers[app.nameIndex].drawing[3][i][3], fill=app.allPlayers[app.nameIndex].drawing[3][i][4])
            elif app.allPlayers[app.nameIndex].drawing[3][i][0] == 'cir':
                drawCircle(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], fill=app.allPlayers[app.nameIndex].drawing[3][i][4])
            elif app.allPlayers[app.nameIndex].drawing[3][i][0] == 'star':
                drawStar(app.allPlayers[app.nameIndex].drawing[3][i][1], app.allPlayers[app.nameIndex].drawing[3][i][2], app.allPlayers[app.nameIndex].drawing[3][i][3], 5, fill=app.allPlayers[app.nameIndex].drawing[3][i][4])

def drawFinalText(app):
    if not app.galleryWord and not app.drawFinishOn:
        for i in range(len(app.allPlayers[app.nameIndex].drawing[4])):
            drawLabel(app.allPlayers[app.nameIndex].drawing[4][i], app.allPlayers[app.nameIndex].drawing[5][i][0], app.allPlayers[app.nameIndex].drawing[5][i][1], align='left-top', fill=app.allPlayers[app.nameIndex].drawing[5][i][2], size=app.allPlayers[app.nameIndex].drawing[5][i][3])

def drawDrawingScreen(app):
    if not app.galleryWord and not app.drawFinishOn and not app.scoresOn:
        if app.allPlayers[app.nameIndex].drawing != None:
            #Image by Freepik
            bgW, bgH = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg')
            drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg', app.width/2, app.height/2, align='center', width=0.2*bgW, height=0.2*bgH, opacity=60)
            drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
            drawRect(app.canvasX, app.canvasY - app.canvasHeight/2 - 50, app.canvasWidth, 50, fill="white", align='center', border='darkGray')
            drawLabel(f'{app.allPlayers[app.nameIndex].name} drew:', app.canvasX - app.canvasWidth/2 + 18, app.canvasY - app.canvasHeight/2 - 50, size=20, align= 'left', font='monospace')
            drawFinalLines(app)
            drawFinalDragLines(app)
            drawFinalStick(app)
            drawFinalText(app)

def drawFinalArrow(app):
    if not app.galleryWord and (not app.drawFinishOn or not app.scoresOn):
        if app.allPlayers[app.nameIndex].drawing != None:
            drawRect(app.canvasX + app.canvasWidth/2, app.canvasY + app.canvasHeight/2 + 45 + 18, 45, 45, fill='white', border='black', align='right-bottom')
            drawLabel(">", app.canvasX + app.canvasWidth/2 - 45/2, app.canvasY + app.canvasHeight/2 + 45 + 18 - 45/2, align='center', size=30)

        elif app.allPlayers[app.nameIndex].prompt != None:
            drawRect(app.width/2 + 300, app.height/2 + 200 + 45 + 18, 45, 45, fill='white', border='black', align='right-bottom')
            drawLabel(">", app.width/2 + 300 - 45/2, app.height/2 + 200 + 45 + 18 - 45/2, align='center', size=30)

def gallery_onMousePress(app, mouseX, mouseY):
    if app.galleryWord and app.drawFinishOn != True:
        app.nameIndex = 0
        app.galleryWord = False

    if app.allPlayers[app.nameIndex].drawing != None and app.drawFinishOn != True:
        if ((app.canvasX + app.canvasWidth/2 - 45<= mouseX <= app.canvasX + app.canvasWidth/2) and 
            (app.canvasY + app.canvasHeight/2 + 18 <= mouseY <=app.canvasY + app.canvasHeight/2 + 45 + 18)):
            if app.nameIndex < len(app.allPlayers) - 1:
                app.nameIndex += 1
            else:
                if app.gameMode == 'classic':
                    app.drawFinishOn = True
                elif app.gameMode == 'competitive':
                    app.scoresOn = True
                    determineWinner(app)


    elif app.allPlayers[app.nameIndex].prompt != None and app.drawFinishOn != True:
        if ((app.width/2 + 300 - 45 <= mouseX <= app.width/2 + 300) and 
            (app.height/2 + 200 + 45 + 18 - 45 <= mouseY <= app.height/2 + 200 + 45 + 18)):
            if app.nameIndex < len(app.allPlayers) - 1:
                app.nameIndex += 1
            else:
                if app.gameMode == 'classic':
                    app.drawFinishOn = True
                elif app.gameMode == 'competitive':
                    app.scoresOn = True
                    determineWinner(app)

    if app.drawFinishOn:
        if ((app.width/2 - 100 <= mouseX <= app.width/2 + 100) and 
            (app.height/2 + 100 - 45/2 <= mouseY <= app.height/2 + 100 + 45/2)):
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

            ############
            #SETUP APPS
            ###########
            app.gameMode = None
            app.namesOn = False
            app.numPlayersOn = False

            ###########
            #PROMPT APPS
            ###########
            app.writeScreen = True
            app.typePrompt = False
            app.prompt = ''
            app.promptConfirm = False
            app.promptIllum = False
            app.promptList = []

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
            app.penBack = 'forestGreen'
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
            app.drawHomeIllum = False


            setActiveScreen('start')

    if app.scoresOn:
        if ((app.menuX - app.menuWidth/2 + 50<=mouseX<=app.menuX - app.menuWidth/2 + 50 + 110)
            and (app.height/2+100-45/2<= mouseY <=app.height/2+100+45/2)):
            app.numPlayersStr = ''
            app.numPlayersConfirmButton = False
            app.numPlayersConfirmButtonIllum = False
            app.numPlayersType = False
            app.numPlayersShow = False
            app.numPlayersConfirmed = False

            firstPlayer = app.playerNames[0]
            app.playerNames.pop(0)
            app.playerNames.append(firstPlayer)
            app.nameIndex = 1
            app.nameType = False
            app.name = ''
            app.nameConfirm = False
            app.nameConfirmButtonIllum = False

            ############
            #SETUP APPS
            ###########
            app.namesOn = False
            app.numPlayersOn = False

            ###########
            #PROMPT APPS
            ###########
            app.writeScreen = True
            app.typePrompt = False
            app.prompt = ''
            app.promptConfirm = False
            app.promptIllum = False
            app.promptList = []

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
            app.penBack = 'forestGreen'
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
            app.drawHomeIllum = False
            app.scoresOn = False


            setActiveScreen('prompt')
    
        elif ((app.menuX + app.menuWidth/2 - 50 - 8 + 8 - (110)<=mouseX<=app.menuX + app.menuWidth/2 - 50 - 8 + 8) and 
              (app.height/2+100-45/2<= mouseY <=app.height/2+100+45/2)):
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

            ############
            #SETUP APPS
            ###########
            app.gameMode = None
            app.namesOn = False
            app.numPlayersOn = False

            ###########
            #PROMPT APPS
            ###########
            app.writeScreen = True
            app.typePrompt = False
            app.prompt = ''
            app.promptConfirm = False
            app.promptIllum = False
            app.promptList = []

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
            app.drawHomeIllum = False


            setActiveScreen('start')


        

def drawFinish(app):
    if app.drawFinishOn:
        #Image from Freepik
        bgWidth, bgHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg', app.width/2, app.height/2, align='center', width=0.4*bgWidth, height=0.4*bgHeight, opacity=100)
        drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill='lavender', border='black', opacity=90)
        drawRect(app.width/2, app.height/2+100, 200, 45, fill=None, border='black', align='center')
        drawLabel('Return Home', app.width/2, app.height/2+100, size=20, fill='black', font='monospace')
        #font by 1001 Fonts Fontalicious
        imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/thanks.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/thanks.png', app.width/2, app.height/2 - 50, width = 0.3*imageWidth, height= 0.3*imageHeight, align='center')

def gallery_onMouseMove(app, mouseX, mouseY):
    if app.drawFinishOn and ((app.width/2 - 100 <= mouseX <= app.width/2 + 100) and 
        (app.height/2 + 100 - 45/2 <= mouseY <= app.height/2 + 100 + 45/2)):
        app.drawHomeIllum = True
    else:
        app.drawHomeIllum = False

    if app.scoresOn and ((app.menuX - app.menuWidth/2 + 50<=mouseX<=app.menuX - app.menuWidth/2 + 50 + 110)
        and (app.height/2+100-45/2<= mouseY <=app.height/2+100+45/2)):
        app.drawReplayIllum = True
    else:
        app.drawReplayIllum = False

    if app.scoresOn and ((app.menuX + app.menuWidth/2 - 50 - 8 + 7 - (110)<=mouseX<=app.menuX + app.menuWidth/2 - 50 - 8 + 7) and 
        (app.height/2+100-45/2<= mouseY <=app.height/2+100+45/2)):
        app.drawHome2Illum = True
    else:
        app.drawHome2Illum = False

def drawReturnHomeIllum(app):
    if app.drawHomeIllum:
        drawRect(app.width/2, app.height/2+100, 200, 45, fill='mediumPurple', border='black', align='center', opacity=70)

    if app.drawHome2Illum:
        drawRect(app.menuX + app.menuWidth/2 - 50 - 8 + 8, app.height/2+100, 110, 45, fill='lightBlue', border='black', align='right', opacity=60)

    if app.drawReplayIllum:
        drawRect(app.menuX - app.menuWidth/2 + 50, app.height/2+100, 100, 45, fill='lightBlue', border='black', align='left', opacity=60)


def gallery_onKeyPress(app, key):
    if app.gameMode == 'competitive' and app.scoresOn:
        if key == 'space':
            app.showWinner = True

def drawScores(app):
    if app.gameMode == 'competitive' and app.scoresOn:
        #Image by Freepik
        bgW, bgH = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/669.jpg', app.width/2, app.height/2, align='center', width=0.25*bgW, height=0.25*bgH, opacity=100)
        drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill='lavender', border='black', opacity=90)
        if not app.showWinner:
            drawLabel("And the winner is...", app.menuX, app.menuY, font='monospace', size=20)
            drawLabel("press space to reveal", app.menuX, app.menuY + 45, font='monspace', size=15, bold=True)
        else:
            drawLabel(app.playerNames[app.winner+2]+'!', app.menuX, app.menuY - 150, font='monospace', size=30, bold=True)
            #Font by 1001 fonts Fontalicious
            imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/thanks.png')
            drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/thanks.png', app.width/2, app.height/2 - 50, width = 0.3*imageWidth, height= 0.3*imageHeight, align='center')
            drawLabel("Play Again", app.menuX - app.menuWidth/2 + 50 + 5, app.height/2+100, size=15, fill='black', font='monospace', align='left')
            drawRect(app.menuX - app.menuWidth/2 + 50, app.height/2+100, 100, 45, fill=None, border='black', align='left')
            drawLabel("Return Home", app.menuX + app.menuWidth/2 -50, app.height/2+100, size=15, fill='black', font='monospace', align='right')
            drawRect(app.menuX + app.menuWidth/2 - 50 - 8 + 8, app.height/2+100, 110, 45, fill=None, border='black', align='right')


def determineWinner(app):
    reference = app.allPlayers[0].prompt
    winner = postProcessing(reference, app.promptList[1:])
    app.winner = winner
