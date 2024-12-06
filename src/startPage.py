from cmu_graphics import *

def onResize(app):
    app.menuX = app.width/2
    app.menuY = app.height/2
    app.newGameX = app.width/2
    app.newGameY = app.height/2 - 100
    app.rulesX = app.width/2
    app.rulesY = app.height/2 + 100
    app.logoX = app.width/2
    app.logoY = app.menuY - app.menuHeight/2 - 50

def drawMenuBox(app):
    #Image by Freepik
    bgWidth, bgHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4814420.jpg', app.width/2, app.height/2, align='center', width=0.4*bgWidth, height=0.4*bgHeight, opacity=80)
    drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill='lavender', border='black', opacity=90)
    #Font is from 1001 fonts Fontalicious
    imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/drawphone.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/drawphone.png', app.logoX, app.logoY, width = 0.5*imageWidth, height= 0.5*imageHeight, align='center')

def drawButtons(app):
    drawRect(app.newGameX, app.newGameY, app.startButtonWidth, app.startButtonHeight, fill=None, border = 'black', align='center')
    drawRect(app.rulesX, app.rulesY, app.startButtonWidth, app.startButtonHeight, fill=None, border = 'black', align='center')
    drawLabel("New Game", app.newGameX, app.newGameY, size=25, align='center', font='monospace')
    drawLabel("How to Play", app.rulesX, app.rulesY, size=25, align='center', font='monospace')

def drawIllumButtons(app):
    if app.illumStartButton:
        drawRect(app.newGameX, app.newGameY, app.startButtonWidth, app.startButtonHeight, fill='mediumPurple', border = 'darkGray', align='center', opacity=60)

    if app.illumRulesButton:
        drawRect(app.rulesX, app.rulesY, app.startButtonWidth, app.startButtonHeight, fill='mediumPurple', border = 'darkGray', align='center', opacity=60)

def start_onMouseMove(app, mouseX, mouseY):
    if ((app.newGameX - app.startButtonWidth/2 <= mouseX <= app.newGameX + app.startButtonWidth/2) and 
        (app.newGameY - app.startButtonHeight/2 <= mouseY <= app.newGameY + app.startButtonHeight/2)):
        app.illumStartButton = True
        app.illumRulesButton = False
    else:
        app.illumStartButton = False

    if ((app.rulesX - app.startButtonWidth/2 <= mouseX <= app.rulesX + app.startButtonWidth/2) and 
        (app.rulesY - app.startButtonHeight/2 <= mouseY <= app.rulesY + app.startButtonHeight/2)):
        app.illumStartButton = False
        app.illumRulesButton = True
    else:
        app.illumRulesButton = False
        

def start_onMousePress(app, mouseX, mouseY):
    if ((app.newGameX - app.startButtonWidth/2 <= mouseX <= app.newGameX + app.startButtonWidth/2) and 
        (app.newGameY - app.startButtonHeight/2 <= mouseY <= app.newGameY + app.startButtonHeight/2)):
        setActiveScreen('setUp')

    if ((app.rulesX - app.startButtonWidth/2 <= mouseX <= app.rulesX + app.startButtonWidth/2) and 
        (app.rulesY - app.startButtonHeight/2 <= mouseY <= app.rulesY + app.startButtonHeight/2)):
        setActiveScreen('rules')