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
    app.penQualities = (app.penColor, app.penSize)

    #storing free draw points
    app.lines = [[]]
    app.currentLine = []
    app.coloredLines = {}

    app.eraseCircle = False
    app.eraseCircleX = None
    app.eraseCircleY = None
    
    #testing
    app.drawmode = True   

def redrawAll(app):
    eraseButton(app)
    drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
    for quality in app.coloredLines:
        for line in app.coloredLines[quality]:
            for i in range(len(line)-1):
                drawLine(line[i][0], line[i][1], line[i+1][0], line[i+1][1], fill='black', lineWidth=2)
            
    drawLabel(app.drawmode, 0, 0, align='left')
    drawEraser(app)

            
    
def drawEraser(app):
    if app.eraseMode and app.eraseCircle:
        drawCircle(app.eraseCircleX, app.eraseCircleY, 10, border='black', fill='white')

def onMouseRelease(app, mouseX, mouseY):
    app.drawmode = False
    app.eraseCircle = False
    app.coloredLines[app.penQualities].append([])
     
def distanceBetweenPoints(point1, point2):
    return distance(point1[0], point1[1], point2[0], point2[1])
    
def midpoint(point1, point2):
    return ((point1[0]+point2[0])/2, (point2[1]+point2[1])/2)


def onMouseDrag(app, mouseX, mouseY):
    if app.penMode and app.drawmode:
        app.penQualities = (app.penColor, app.penSize)
        if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
            if app.penQualities not in app.coloredLines:
                app.coloredLines[app.penQualities] = [[]]
                app.coloredLines[app.penQualities][-1].append((mouseX, mouseY))
            else:
                app.coloredLines[app.penQualities][-1].append((mouseX, mouseY))

    if app.eraseMode:
        if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
            app.eraseCircle = True
            app.eraseCircleX = mouseX
            app.eraseCircleY = mouseY
            for quality in app.coloredLines:
                for i in range(len(app.coloredLines[quality])):
                    newPoints = []
                    for point in app.coloredLines[quality][i]:
                        distance = ((mouseX - point[0])**2 + (mouseY - point[1])**2)**0.5

                        if distance > 10:
                            newPoints.append(point)
                    app.coloredLines[quality][i] = newPoints

def onMousePress(app, mouseX, mouseY):
    app.drawmode = True
    if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
        app.penMode = True 

    changeMode(app, mouseX, mouseY)
    if (app.canvasX - app.canvasWidth/2 < mouseX < app.canvasX + app.canvasWidth/2
            and app.canvasY - app.canvasHeight/2 < mouseY < app.canvasY + app.canvasHeight/2):
        app.penMode = True 

def eraseButton(app):
    drawRect(app.canvasX - (app.canvasWidth/2) + (15) + 150,app.canvasY + (app.canvasHeight/2) + 25,30,30, fill='black', align='center')

def changeMode(app, mouseX, mouseY):
    if ((app.canvasX - (app.canvasWidth/2) + (15) + 135 <= mouseX <= app.canvasX - (app.canvasWidth/2) + (15) + 165) and 
        (app.canvasY + (app.canvasHeight/2) + 10 <= mouseY <= app.canvasY + (app.canvasHeight/2) + 40)):
        app.penMode = False
        app.eraseMode = True
        
def distance(x0, y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5
        
def main():
    runApp()

main()
