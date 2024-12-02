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

def drawSetUpBox(app):
    drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill=None, border='darkGray')
    imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/DrawPhone.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/DrawPhone.png', app.logoX, app.logoY, width = 0.25*imageWidth, height= 0.25*imageHeight, align='center')

def homeButton(app):
    drawRect(8, 8, 90, 45, fill=None, border='darkGray')
    drawLabel('Home', 53, 8 + 45/2, size=25)

def numPlayers(app):
    drawLabel("Number of Players:", app.menuX - app.menuWidth/2 + 25, app.menuY - app.menuHeight/2 + 70, size = 25, align='left')
    drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 70 + 45/2, 125, 45, fill=None, border='darkGray', align='right-bottom')
    if app.numPlayersConfirmButton:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 70 + 45/2+ 60, 70, 45, fill=None, border='darkGray', align='right-bottom')

def setUp_onMousePress(app, mouseX, mouseY):
    if ((8 <= mouseX <= 89) and (8 <= mouseY <= 8 + 45)):
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
        setActiveScreen('start')

    if ((app.menuX + app.menuWidth/2 - 25 - 125<= mouseX <= app.menuX + app.menuWidth/2 - 25) and
        (app.menuY - app.menuHeight/2 + 70 + 45/2 - 45 <= mouseY <=app.menuY - app.menuHeight/2 + 70 + 45/2)):
        app.numPlayersType = True
        app.numPlayersShow = True

    if ((app.menuX + app.menuWidth/2 - 25 - 70 <= mouseX <= app.menuX + app.menuWidth/2 - 25) and 
        (app.menuY - app.menuHeight/2 + 70 + 45/2+ 60 - 45 <= mouseY <= app.menuY - app.menuHeight/2 + 70 + 45/2+ 60)):
        app.numPlayersConfirmed = True
        app.numPlayersType = False
        app.numPlayersShow = True

    if app.numPlayersConfirmed:
        if ((app.menuX - app.menuWidth/2 + 25<=mouseX<=app.menuX - app.menuWidth/2 + 25+app.menuWidth - 50) and 
            (app.menuY + 50 - 45/2 <= mouseY <=app.menuY + 50 + 45/2)):
            app.nameType = True

    if app.nameConfirm:
        if ((app.menuX + app.menuWidth/2 - 90 <= mouseX <= app.menuX + app.menuWidth/2 - 25) and 
            (app.menuY + 50 + 45/2 + 60 - 45<= mouseY <= app.menuY + 50 + 45/2 + 60)):
            if app.nameIndex < int(app.numPlayersStr):
                app.nameIndex += 1
                app.playerNames.append(app.name)
                print(app.playerNames)
                app.name = ''
                app.nameConfirm = False
                app.nameConfirmButtonIllum = False
            else:
                app.playerNames.append(app.name)
                setActiveScreen('prompt')

def drawNameConfirmButton(app):
    if app.nameConfirm:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY + 50 + 45/2 + 60, 70, 45, align='right-bottom', fill=None, border='darkGray')

def setUp_onKeyPress(app, key):
    if app.numPlayersType:
        if key == 'backspace':
            app.numPlayersStr = app.numPlayersStr[:-1]
        elif len(app.numPlayersStr) < 8:
            if key.isdigit():
                app.numPlayersStr += str(key)
                app.numPlayersConfirmButton = True

    if app.nameType:
        if key == 'backspace':
            app.name = app.name[:-1]
            if len(app.name) == 0:
                app.nameConfirm = False
        elif len(app.name) < 19 and key in string.ascii_letters or key in string.digits:
            app.name += key
            app.nameConfirm = True

def drawNumPlayers(app):
    if app.numPlayersShow:
        drawLabel(app.numPlayersStr + '|', app.menuX + app.menuWidth/2 - 25 - 125 + 8, app.menuY - app.menuHeight/2 + 70, size=25, align='left')

def enterNames(app):
    if app.numPlayersConfirmed and app.nameIndex < int(app.numPlayersStr)+1:
        drawLabel(f'Player {app.nameIndex} Name:', app.menuX - app.menuWidth/2 + 25, app.menuY, size=25, align='left')
        drawRect(app.menuX - app.menuWidth/2 + 25, app.menuY + 50, app.menuWidth - 50,45, fill=None, border='darkGray', align='left')
        if app.nameType:
            drawLabel(app.name + '|', app.menuX - app.menuWidth/2 + 25 + 8, app.menuY + 50, size=25, align = 'left')

def drawButtonLabels(app):
    if app.numPlayersConfirmButton:
        checkWidth, checkHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/rules.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.menuX + app.menuWidth/2 - 25 - 70/2, app.menuY - app.menuHeight/2 + 70 + 60, width=checkWidth*0.015, height=checkWidth*0.015, align='center')

    if app.nameConfirm:
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.menuX + app.menuWidth/2 - 25 - 70/2, app.menuY + 50 + 45/2 + 60 - 45/2, width=checkWidth*0.015, height=checkWidth*0.015, align='center')

def setUp_onMouseMove(app, mouseX, mouseY):
    if (8 <= mouseX <= 89) and (8 <= mouseY <= 8 + 45):
        app.homeIllumButton = True
        app.numPlayersConfirmButtonIllum = False
        app.nameConfirmButtonIllum = False
    else:
        app.homeIllumButton = False

    if app.numPlayersConfirmButton:
        if ((app.menuX + app.menuWidth/2 - 25 - 70 <= mouseX <= app.menuX + app.menuWidth/2 - 25) and 
            (app.menuY - app.menuHeight/2 + 70 + 45/2+ 60 - 45 <= mouseY <= app.menuY - app.menuHeight/2 + 70 + 45/2+ 60)):
            app.numPlayersConfirmButtonIllum = True
            app.nameConfirmButtonIllum = False
            app.homeIllumButton = False
        else:
            app.numPlayersConfirmButtonIllum = False

    if app.nameConfirm:
        if ((app.menuX + app.menuWidth/2 - 90 <= mouseX <= app.menuX + app.menuWidth/2 - 25) and 
            (app.menuY + 50 + 45/2 + 60 - 45<= mouseY <= app.menuY + 50 + 45/2 + 60)): 
            app.nameConfirmButtonIllum = True
            app.homeIllumButton = False
            app.numPlayersConfirmButtonIllum = False
        else:
            app.nameConfirmButtonIllum = False

def drawButtonIlluminations(app):
    if app.homeIllumButton:
        drawRect(8, 8, 90, 45, fill='red', border='darkGray', opacity=60)
    if app.numPlayersConfirmButtonIllum:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 70 + 45/2+ 60, 70, 45, fill='purple', opacity=60,border='darkGray', align='right-bottom')
    if app.nameConfirmButtonIllum:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY + 50 + 45/2 + 60, 70, 45, align='right-bottom', fill='purple', border='darkGray', opacity = 60)


    

