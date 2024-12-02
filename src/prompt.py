from cmu_graphics import *
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

def drawWriteScreen(app):
    if app.writeScreen:
        writeWidth, writeHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/write.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/write.png', app.width/2, app.height/2, align='center', width=writeWidth*0.4, height=writeHeight*0.4)
        drawLabel('click to begin', app.width/2, app.height/2 + 200, align='center', fill='darkGray')

def prompt_onMousePress(app, mouseX, mouseY):
    if app.writeScreen:
        app.writeScreen = False
        app.nameIndex = 0

    else:
        if (((app.width/2)-(560/2) <= mouseX <= (app.width/2)+(560/2)) and 
            ((app.height/2)- (45/2) <= mouseY <= (app.height/2)+(45/2))):
            print('hi')
            app.typePrompt = True

        if app.promptConfirm:
            if ((app.width/2 + (560/2) - 70<= mouseX <= app.width/2 + (560/2)) and 
                (app.height/2+(45/2) + 68 - 45 <= mouseY <=app.height/2+(45/2) + 68)):
                if app.nameIndex < len(app.playerNames) - 1:
                    app.promptList.append(app.prompt)
                    app.nameIndex += 1
                    setActiveScreen('canvas')
                else:
                    app.promptList.append(app.prompt)
                    setActiveScreen('gallery')

def drawPromptScreen(app):
    if not app.writeScreen:
        drawRect(app.width/2, app.height/2, 600, 400, fill='white', border='darkGray', align='center')
        if app.nameIndex == 0:
            drawLabel(f'{app.playerNames[app.nameIndex]}, please enter a prompt below: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top')
            drawLabel('let your imagination run wild...', app.width/2 - 300 + 18, app.height/2 - 200 + 18 + 30, size=15, align='left-top')

        else:
            drawLabel(f'{app.playerNames[app.nameIndex]}, what did you just see? ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top')
            drawLabel('let your imagination run wild...', app.width/2 - 300 + 18, app.height/2 - 200 + 18 + 30, size=15, align='left-top')

        drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
        drawLabel(f'{50-len(app.prompt)}/50', app.width/2 + (560/2), app.height/2+(45/2)+10, fill='darkGray', align='right-bottom')

        if app.promptConfirm:
            drawRect(app.width/2 + (560/2), app.height/2+(45/2) + 68, 70, 45, fill='white', align='right-bottom', border='darkGray')
            checkWidth, checkHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/rules.png')
            drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.width/2 + (560/2) - 70/2, app.height/2+(45/2) + 65 - 45/2, width=checkWidth*0.015, height=checkWidth*0.015, align='center')


def prompt_onKeyPress(app, key):
    if app.typePrompt:
        if key == 'backspace':
            app.prompt = app.prompt[:-1]
            if len(app.prompt) == 0:
                app.promptConfirm = False
        elif len(app.prompt) < 50 and key in string.ascii_letters or key in string.digits:
            app.promptConfirm = True
            if app.prompt == '|':
                app.prompt = key
            else:
                app.prompt += key
        elif key == 'space':
            app.prompt += ' '

def drawPrompt(app):
    if app.typePrompt:
        drawLabel(app.prompt + '|', app.width/2- (560/2) + 10, app.height/2, align='left', size=25)

def prompt_onMouseMove(app, mouseX, mouseY):
    if ((app.width/2 + (560/2) - 70<= mouseX <= app.width/2 + (560/2)) and 
                (app.height/2+(45/2) + 68 - 45 <= mouseY <=app.height/2+(45/2) + 68)):
        app.promptIllum = True
    else:
        app.promptIllum = False

def promptConfirmIllum(app):
        if app.promptIllum:
            drawRect(app.width/2 + (560/2), app.height/2+(45/2) + 68, 70, 45, fill='purple', align='right-bottom', border='darkGray', opacity=60)

    
