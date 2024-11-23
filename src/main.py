from cmu_graphics import *

def onAppStart(app):
    #canvas dimensions
    app.height = 800
    app.width = 800
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width/2              #align = 'center'
    app.canvasY = app.height/2             #align = 'center'

    #default pen
    app.penMode = True
    app.eraseMode = False
    app.penColor = 'black'
    app.penSize = 3

    #storing free draw points
    app.lines = [[]]
    app.currentLine = []
    app.coloredLines = {}

def onResize(app):
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width/2              
    app.canvasY = app.height/2      

def redrawAll(app):
    colorButtons(app)
    drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
    for line in app.lines:
        for i in range(len(line)-1):
            drawLine(line[i][0], line[i][1], line[i+1][0], line[i+1][1], lineWidth=app.penSize, fill=app.penColor)
            print(app.lines)


def onMouseDrag(app, mouseX, mouseY):
    if app.penMode:
        if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
            app.lines[-1].append((mouseX, mouseY))

    if app.eraseMode:
        if (mouseX, mouseY) in app.lines:
            app.lines.remove((mouseX, mouseY))

def onMouseRelease(app, mouseX, mouseY):
    app.lines.extend([])

def onMousePress(app, mouseX, mouseY):
    changeColor(app, mouseX, mouseY)
    if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
        app.penMode = True 

def colorButtons(app):
    drawCircle(app.canvasX - (app.canvasWidth/2) + 15, app.canvasY + (app.canvasHeight/2) + 25, 15, fill='red')
    drawCircle(app.canvasX - (app.canvasWidth/2) + 15 + 50, app.canvasY + (app.canvasHeight/2) + 25, 15, fill='yellow')
    drawCircle(app.canvasX - (app.canvasWidth/2) + (15) + 100, app.canvasY + (app.canvasHeight/2) + 25, 15, fill='blue')

def changeColor(app, mouseX, mouseY):
    if distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15, app.canvasY + (app.canvasHeight/2) + 25) <= 15:
        app.penColor = 'red'

    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15 + 50, app.canvasY + (app.canvasHeight/2) + 25) <= 15:
        app.penColor = 'yellow'

    elif distance(mouseX, mouseY, app.canvasX - (app.canvasWidth/2) + 15 + 100, app.canvasY + (app.canvasHeight/2) + 25) <= 15:
        app.penColor = 'blue'


def main():
    runApp()

main()
