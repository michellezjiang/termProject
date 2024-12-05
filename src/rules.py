from cmu_graphics import *

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
    app.drawNextPreview = False
    app.canMove = False
    app.galleryWord = True
    app.drawFinishOn = False

    app.erasedPositions = [[]]
    app.drawHomeIllum = False

def rules_onResize(app):
    app.logoX = app.width/2
    app.logoY = app.menuY - app.menuHeight/2 - 75


def drawRulesBox(app):
    #font is from 1001 fonts Fontalicious
    bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/background1.jpg')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/background1.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.85, height=bg1Height*0.85)
    imageWidth, imageHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/rules.png')
    drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/rules.png', app.logoX, app.logoY, width = 0.23*imageWidth, height= 0.23*imageHeight, align='center')
    drawRect(app.menuX, app.menuY, app.menuWidth, app.menuHeight, align='center', fill='lavender', border='black', opacity=90)

def drawRule(app):
    if app.drawRule1:
        drawLabel("1.   The first player begins ", app.width/2, app.height/2-90, size=18, font='monospace')
        drawLabel("by writing a funny sentence.", app.width/2, app.height/2-45, size=18, font='monospace')
        drawLabel("Be creative!", app.width/2, app.height/2, size=20, font='monospace')
        drawLabel("The more unique the sentence,", app.width/2, app.height/2+45, size=18, font='monospace')
        drawLabel("the better the experience!", app.width/2, app.height/2+90, size=18, font='monospace')

    if app.drawRule2:
        drawLabel("2.   The next player then", app.width/2, app.height/2 - 45, size=18, font='monospace')
        drawLabel("draws what the previous player", app.width/2, app.height/2, size=18, font='monospace')
        drawLabel('wrote in 25 seconds.', app.width/2, app.height/2 + 45, size=18, font='monospace')

    if app.drawRule3:
        drawLabel("3.   Then the next player", app.width/2, app.height/2 - 45, size=18, font='monospace')
        drawLabel("has to guess what the", app.width/2, app.height/2, size=18, font='monospace')
        drawLabel("previous player drew.", app.width/2, app.height/2 + 45, size=18, font='monospace')
         
    if app.drawRule4:
        drawLabel("4.   The game continues until", app.width/2, app.height/2 - 45, size=18, font='monospace')
        drawLabel("all the players", app.width/2, app.height/2, size=18, font='monospace')
        drawLabel("either drew or guessed.", app.width/2, app.height/2 + 45, size=18, font='monospace')

    if app.drawRule5:
        drawLabel("5.   Everyone will then get to", app.width/2, app.height/2 - 45, size=18, font='monospace')
        drawLabel("look at all of the", app.width/2, app.height/2, size=18, font='monospace')
        drawLabel("fun drawings and guesses!", app.width/2, app.height/2+45, size=18, font='monospace')

def drawArrow(app):
    if not app.drawRule5:
        drawRect(app.menuX + app.menuWidth/2 - 8, app.menuY + app.menuHeight/2 - 8, 45, 45, fill=None, border='black', align = 'right-bottom')
        drawLabel(">", app.menuX + app.menuWidth/2 - 8 - 45 /2, app.menuY + app.menuHeight/2 - 8 - 45/2, size=30, align='center', font='monospace')

    else:
        drawRect(app.menuX + app.menuWidth/2 - 8, app.menuY + app.menuHeight/2 - 8, 90, 45, fill=None, border='black', align='right-bottom')
        drawLabel("Restart", app.menuX + app.menuWidth/2 - 8 - 45, app.menuY + app.menuHeight/2 - 8 - 45/2, size=20, align='center', font='monospace')

def rules_onMousePress(app, mouseX, mouseY):
    if ((8 <= mouseX <= 89) and (8 <= mouseY <= 8 + 45)):
        setActiveScreen('start')

    if ((app.menuX + app.menuWidth/2 - 8 - 45 <= mouseX <= app.menuX + app.menuWidth/2 - 8) and
        (app.menuY + app.menuHeight/2 - 8 - 45 <= mouseY <= app.menuY + app.menuHeight/2 - 8)):

        if app.drawRule1:
            app.drawRule1, app.drawRule2 = False, True

        elif app.drawRule2:
            app.drawRule2, app.drawRule3 = False, True

        elif app.drawRule3:
            app.drawRule3, app.drawRule4 = False, True

        elif app.drawRule4:
            app.drawRule4, app.drawRule5 = False, True
            app.resetIllumButton = True
            app.arrowIllumButton = False

        elif app.drawRule5:
            app.drawRule5 = False
            app.drawRule1 = True
            app.arrowIllumButton = True
            app.resetIllumButton = False

    elif ((app.menuX + app.menuWidth/2 - 8 - 90 <= mouseX <= app.menuX + app.menuWidth/2 - 8) and 
        (app.menuY + app.menuHeight/2 - 8 - 45 <= mouseY <= app.menuY + app.menuHeight/2 - 8)):
        if app.drawRule5:
            app.drawRule5 = False
            app.drawRule1 = True
            app.arrowIllumButton = True
            app.resetIllumButton = False

def rules_onMouseMove(app, mouseX, mouseY):
    if ((not app.drawRule5 and app.menuX + app.menuWidth/2 - 8 - 45 <= mouseX <= app.menuX + app.menuWidth/2 - 8) and
        (app.menuY + app.menuHeight/2 - 8 - 45 <= mouseY <= app.menuY + app.menuHeight/2 - 8)):
        app.arrowIllumButton = True
        app.homeIllumButton = False
        app.resetIllumButton = False
    elif ((app.menuX + app.menuWidth/2 - 8 - 90 <= mouseX <= app.menuX + app.menuWidth/2 - 8) and 
        (app.menuY + app.menuHeight/2 - 8 - 45 <= mouseY <= app.menuY + app.menuHeight/2 - 8) and app.drawRule5):
        app.arrowIllumButton = False
        app.homeIllumButton = False
        app.resetIllumButton = True
    elif ((8 <= mouseX <= 89) and (8 <= mouseY <= 8 + 45)):
        app.homeIllumButton = True
        app.resetIllumButton = False
        app.arrowIllumButton = False
    else:
        app.arrowIllumButton = False
        app.resetIllumButton = False
        app.homeIllumButton = False

def highlightButton(app):
    if app.arrowIllumButton:
        drawRect(app.menuX + app.menuWidth/2 - 8, app.menuY + app.menuHeight/2 - 8, 45, 45, fill='plum', border='black', align = 'right-bottom', opacity=60)

    if app.resetIllumButton:
        drawRect(app.menuX + app.menuWidth/2 - 8, app.menuY + app.menuHeight/2 - 8, 90, 45, fill='plum', border='black', align='right-bottom', opacity=60)

    if app.homeIllumButton:
        drawRect(8, 8, 90, 45, fill='plum', border='black', opacity=60)

def homeButton(app):
    drawRect(8, 8, 90, 45, fill='black', border='black')
    drawLabel('Home', 53, 8 + 45/2, size=25, font='monospace')