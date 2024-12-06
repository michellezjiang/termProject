from cmu_graphics import *
from storePlayer import *
import string

def drawWriteScreen(app):
    #font is from 1001 fonts Fontalicious
    # bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/7035853.jpg')
    # drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/7035853.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.45, height=bg1Height*0.45)
    if app.writeScreen:
        bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.45, height=bg1Height*0.45, opacity=60)
        writeWidth, writeHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/write.png')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/write.png', app.width/2, app.height/2, align='center', width=writeWidth*0.45, height=writeHeight*0.45)
        drawLabel('click to begin', app.width/2, app.height/2 + 100, align='center', fill='black', font='monospace', size=15, bold=True)

def prompt_onMousePress(app, mouseX, mouseY):
    if app.writeScreen:
        app.writeScreen = False
        app.nameIndex = 0

    else:
        if (((app.width/2)-(560/2) <= mouseX <= (app.width/2)+(560/2)) and 
            ((app.height/2)- (45/2) <= mouseY <= (app.height/2)+(45/2))):
            app.typePrompt = True

        if app.promptConfirm:
            if ((app.width/2 + (560/2) - 70<= mouseX <= app.width/2 + (560/2)) and 
                (app.height/2+(45/2) + 68 - 45 <= mouseY <=app.height/2+(45/2) + 68)):
                if app.nameIndex < len(app.playerNames) - 1:
                    app.promptList.append(app.prompt)
                    newPlayer = Player(app.playerNames[app.nameIndex], app.prompt, None)
                    app.allPlayers.append(newPlayer)
                    app.nameIndex += 1
                    app.prompt = ''
                    setActiveScreen('canvas')
                else:
                    newPlayer = Player(app.playerNames[app.nameIndex], app.prompt, None)
                    app.allPlayers.append(newPlayer)
                    app.promptList.append(app.prompt)
                    app.prompt = ''
                    setActiveScreen('gallery')

def drawPromptScreen(app):
    if not app.writeScreen:
        bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.45, height=bg1Height*0.45, opacity=60)
        drawRect(app.width/2, app.height/2, 600, 400, fill='darkSeaGreen', border='black', align='center', opacity=60)
        if app.nameIndex == 0:
            drawLabel(f'{app.playerNames[app.nameIndex]}, please enter a prompt below: ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top', font='monospace')
            drawLabel('let your imagination run wild...', app.width/2 - 300 + 18, app.height/2 - 200 + 18 + 30, size=15, align='left-top', font='monospace')

        else:
            drawLabel(f'{app.playerNames[app.nameIndex]}, what did you just see? ', app.width/2 - 300 + 18, app.height/2 - 200 + 18, size=20, align='left-top', font='monospace')
            drawLabel('let your imagination run wild...', app.width/2 - 300 + 18, app.height/2 - 200 + 18 + 30, size=15, align='left-top', font='monospace')

        drawRect(app.width/2, app.height/2, 560, 45, fill='white', align='center', border='darkGray')
        drawLabel(f'{50-len(app.prompt)}/50', app.width/2 + (560/2), app.height/2+(45/2)+10, fill='black', align='right-bottom', font='monospace')

        if app.promptConfirm:
            drawRect(app.width/2 + (560/2), app.height/2+(45/2) + 68, 70, 45, fill='white', align='right-bottom', border='black')
            checkWidth, checkHeight = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/check.png')
            drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/check.png', app.width/2 + (560/2) - 70/2, app.height/2+(45/2) + 65 - 45/2, width=checkWidth*0.06, height=checkWidth*0.06, align='center')
            #icon from Flaticon Freepik

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
        drawLabel(app.prompt + '|', app.width/2- (560/2) + 10, app.height/2, align='left', size=18, font='monospace')

def prompt_onMouseMove(app, mouseX, mouseY):
    if ((app.width/2 + (560/2) - 70<= mouseX <= app.width/2 + (560/2)) and 
                (app.height/2+(45/2) + 68 - 45 <= mouseY <=app.height/2+(45/2) + 68)):
        app.promptIllum = True
    else:
        app.promptIllum = False

def promptConfirmIllum(app):
    if not app.writeScreen:
        if app.promptIllum:
            drawRect(app.width/2 + (560/2), app.height/2+(45/2) + 68, 70, 45, fill='darkSeaGreen', align='right-bottom', border='black', opacity=60)

    
