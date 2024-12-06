from cmu_graphics import *
from storePlayer import *
import string


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
            drawStar(app.allPlayers[-1].drawing[3][i][1], app.allPlayers[-1].drawing[3][i][2], app.allPlayers[-1].drawing[3][i][3], 5, fill=app.allPlayers[-1].drawing[3][i][4])

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