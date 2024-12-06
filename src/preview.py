from cmu_graphics import *
from storePlayer import *

def drawPreview(app):
    if app.drawNextPreview:
        #Image from FreePik
        bg1Width, bg1Height = getImageSize('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg')
        drawImage('/Users/michellejiang/Documents/GitHub/termProject/src/4943857.jpg', app.width/2, app.height/2, align='center', width=bg1Width*0.45, height=bg1Height*0.45, opacity=60)
        drawRect(app.canvasX, app.canvasY - app.canvasHeight/2 - 50, app.canvasWidth, 50, fill="white", align='center', border='darkGray')
        drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
        drawLabel(f'{app.playerNames[app.nameIndex]}, observe this drawing. ', app.canvasX - app.canvasWidth/2 + 18, app.canvasY - app.canvasHeight/2 - 50, size=20, align= 'left', font='monospace')
        for i in range(len(app.lines)):
            for j in range(len(app.lines[i])-1):
                drawLine(app.lines[i][j][0], app.lines[i][j][1], app.lines[i][j+1][0], app.lines[i][j+1][1], fill=app.penColorSize[i][0][0], lineWidth=app.penColorSize[i][0][1])
        drawPreviewScreen(app)
        drawLabel(f'click anywhere to continue',  app.width/2, app.canvasY+app.canvasHeight/2+15, fill='black', align='center', font='monospace', bold=True)



def drawPreviewLines(app):
    if app.gameMode == 'classic':
        for i in range(len(app.allPlayers[-1].drawing[0])):
            for j in range(len(app.allPlayers[-1].drawing[0][i])-1):
                drawLine(app.allPlayers[-1].drawing[0][i][j][0], app.allPlayers[-1].drawing[0][i][j][1], app.allPlayers[-1].drawing[0][i][j+1][0], app.allPlayers[-1].drawing[0][i][j+1][1], fill=app.allPlayers[-1].drawing[1][i][0][0], lineWidth=app.allPlayers[-1].drawing[1][i][0][1])

    elif app.gameMode == 'competitive':
        for i in range(len(app.allPlayers[1].drawing[0])):
            for j in range(len(app.allPlayers[1].drawing[0][i])-1):
                drawLine(app.allPlayers[1].drawing[0][i][j][0], app.allPlayers[1].drawing[0][i][j][1], app.allPlayers[1].drawing[0][i][j+1][0], app.allPlayers[1].drawing[0][i][j+1][1], fill=app.allPlayers[1].drawing[1][i][0][0], lineWidth=app.allPlayers[1].drawing[1][i][0][1])

def drawPreviewDragLines(app):
    if app.gameMode == 'classic':
        for i in range(len(app.allPlayers[-1].drawing[2])):
            drawLine(app.allPlayers[-1].drawing[2][i][0], app.allPlayers[-1].drawing[2][i][1], app.allPlayers[-1].drawing[2][i][2], app.allPlayers[-1].drawing[2][i][3], fill=app.allPlayers[-1].drawing[2][i][4], lineWidth=app.allPlayers[-1].drawing[2][i][5])

    elif app.gameMode == 'competitive':
        for i in range(len(app.allPlayers[1].drawing[2])):
            drawLine(app.allPlayers[1].drawing[2][i][0], app.allPlayers[1].drawing[2][i][1], app.allPlayers[1].drawing[2][i][2], app.allPlayers[1].drawing[2][i][3], fill=app.allPlayers[1].drawing[2][i][4], lineWidth=app.allPlayers[1].drawing[2][i][5])

def drawPreviewStick(app):
    if app.gameMode == 'classic':
        for i in range(len(app.allPlayers[-1].drawing[3])):
            if app.allPlayers[-1].drawing[3][i][0] == 'sq':
                drawRect(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], app.allPlayers[-1].drawing[3][i][3], fill=app.allPlayers[-1].drawing[3][i][4])
            elif app.allPlayers[-1].drawing[3][i][0] == 'cir':
                drawCircle(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], fill=app.allPlayers[-1].drawing[3][i][4])
            elif app.allPlayers[-1].drawing[3][i][0] == 'star':
                drawStar(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], 5, fill=app.allPlayers[-1].drawing[3][i][4])

    elif app.gameMode == 'competitive':
        for i in range(len(app.allPlayers[1].drawing[3])):
            if app.allPlayers[1].drawing[3][i][0] == 'sq':
                drawRect(app.allPlayers[1].drawing[3][i][1], app.allPlayers[1].drawing[3][i][2], app.allPlayers[1].drawing[3][i][3], app.allPlayers[1].drawing[3][i][3], fill=app.allPlayers[1].drawing[3][i][4])
            elif app.allPlayers[1].drawing[3][i][0] == 'cir':
                drawCircle(app.allPlayers[1].drawing[3][i][1], app.allPlayers[1].drawing[3][i][2], app.allPlayers[1].drawing[3][i][3], fill=app.allPlayers[1].drawing[3][i][4])
            elif app.allPlayers[1].drawing[3][i][0] == 'star':
                drawStar(app.allPlayers[1].drawing[3][i][1], app.allPlayers[1].drawing[3][i][2], app.allPlayers[1].drawing[3][i][3], 5, fill=app.allPlayers[1].drawing[3][i][4])


def drawPreviewText(app):
    if app.gameMode == 'classic':
        for i in range(len(app.allPlayers[-1].drawing[4])):
            drawLabel(app.allPlayers[-1].drawing[4][i], app.allPlayers[-1].drawing[5][i][0], app.allPlayers[-1].drawing[5][i][1], align='left-top', fill=app.allPlayers[-1].drawing[5][i][2], size=app.allPlayers[-1].drawing[5][i][3])

    elif app.gameMode == 'competitive':
        for i in range(len(app.allPlayers[1].drawing[4])):
            drawLabel(app.allPlayers[1].drawing[4][i], app.allPlayers[1].drawing[5][i][0], app.allPlayers[1].drawing[5][i][1], align='left-top', fill=app.allPlayers[1].drawing[5][i][2], size=app.allPlayers[1].drawing[5][i][3])

def drawPreviewScreen(app):
    
    drawPreviewLines(app)
    drawPreviewDragLines(app)
    drawPreviewStick(app)
    drawPreviewText(app)

def preview_onMousePress(app, mouseX, mouseY):
    app.drawNextPreview = False
    setActiveScreen('prompt')