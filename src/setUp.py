from cmu_graphics import *
import string

def drawSetUpBox(app):
    #Image by Freepik (https://www.freepik.com/free-vector/gradient-purple-swirl-background_34709911.htm#fromView=keyword&page=1&position=26&uuid=c5de668e-f514-4325-bada-f9b32c9e8f82)
    bgWidth, bgHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg', app.width/2, app.height/2, align='center', width=0.4*bgWidth, height=0.4*bgHeight, opacity=80)
    drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill='lavender', border='black', opacity=90)
    imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/DrawPhone.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/DrawPhone.png', app.logoX, app.logoY, width = 0.5*imageWidth, height= 0.5*imageHeight, align='center')

def homeButton(app):
    drawRect(8, 8, 90, 45, fill='lavender', border='black', opacity=90)
    drawLabel('Home', 53, 8 + 45/2, size=20, font='monospace')

def drawMode(app):
    drawLabel("Mode:", app.menuX - app.menuWidth/2 + 25, app.menuY - app.menuHeight/2 + 70, size = 20, align='left', font='monospace')
    drawRect(app.menuX - app.menuWidth/2 + 25, app.menuY - app.menuHeight/2 + 70 + 50, app.menuWidth/2 - 30, 45, align='left', fill=None, border='black')

def numPlayers(app):
    drawLabel("Number of Players:", app.menuX - app.menuWidth/2 + 25, app.menuY - app.menuHeight/2 + 150, size = 20, align='left', font='monospace')
    drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 150 + 45/2, 125, 45, fill='white', border='darkGray', align='right-bottom')
    if app.numPlayersConfirmButton:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 150 + 45/2+ 60, 70, 45, fill=None, border='black', align='right-bottom')

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
                app.name = ''
                app.nameConfirm = False
                app.nameConfirmButtonIllum = False
            else:
                app.playerNames.append(app.name)
                setActiveScreen('prompt')

def drawNameConfirmButton(app):
    if app.nameConfirm:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY + 50 + 45/2 + 60, 70, 45, align='right-bottom', fill=None, border='black')

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
        drawLabel(app.numPlayersStr + '|', app.menuX + app.menuWidth/2 - 25 - 125 + 8, app.menuY - app.menuHeight/2 + 70, size=20, align='left', font='monospace')

def enterNames(app):
    if app.numPlayersConfirmed and app.nameIndex < int(app.numPlayersStr)+1:
        drawLabel(f'Player {app.nameIndex} Name:', app.menuX - app.menuWidth/2 + 25, app.menuY, size=20, align='left', font='monospace')
        drawRect(app.menuX - app.menuWidth/2 + 25, app.menuY + 50, app.menuWidth - 50,45, fill='white', border='darkGray', align='left')
        if app.nameType:
            drawLabel(app.name + '|', app.menuX - app.menuWidth/2 + 25 + 8, app.menuY + 50, size=20, align = 'left', font='monospace')

def drawButtonLabels(app):
    if app.numPlayersConfirmButton:
        checkWidth, checkHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/check.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.menuX + app.menuWidth/2 - 25 - 70/2, app.menuY - app.menuHeight/2 + 70 + 60, width=checkWidth*0.06, height=checkWidth*0.06, align='center')

    if app.nameConfirm:
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.menuX + app.menuWidth/2 - 25 - 70/2, app.menuY + 50 + 45/2 + 60 - 45/2, width=checkWidth*0.06, height=checkWidth*0.06, align='center')

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
        drawRect(8, 8, 90, 45, fill='mediumPurple', border='black', opacity=60)
    if app.numPlayersConfirmButtonIllum:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY - app.menuHeight/2 + 70 + 45/2+ 60, 70, 45, fill='mediumPurple', opacity=60,border='black', align='right-bottom')
    if app.nameConfirmButtonIllum:
        drawRect(app.menuX + app.menuWidth/2 - 25, app.menuY + 50 + 45/2 + 60, 70, 45, align='right-bottom', fill='mediumPurple', border='black', opacity = 60)


    

