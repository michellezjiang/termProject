from cmu_graphics import *

def onAppStart(app):
    # Canvas dimensions
    app.height = 800
    app.width = 800
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width / 2              # Align = 'center'
    app.canvasY = app.height / 2             # Align = 'center'

    # Default pen
    app.penMode = True
    app.eraseMode = False
    app.penColor = 'black'
    app.penSize = 3
    app.penQualities = (app.penColor, app.penSize)

    # Storing free draw points
    app.lines = [[]]
    app.currentLine = []
    app.coloredLines = {}

    app.eraseCircle = False
    app.eraseCircleX = None
    app.eraseCircleY = None
    app.eraseRadius = 10  # Eraser size
    
    # Testing
    app.drawmode = True


def redrawAll(app):
    eraseButton(app)
    drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, 
             align='center', fill='white', border='darkGray')
    # Draw all lines
    for quality in app.coloredLines:
        for line in app.coloredLines[quality]:
            for i in range(len(line) - 1):
                drawLine(line[i][0], line[i][1], line[i + 1][0], line[i + 1][1], 
                         fill=quality[0], lineWidth=quality[1])
    # Draw the eraser circle
    drawEraser(app)

def drawEraser(app):
    if app.eraseMode and app.eraseCircle:
        drawCircle(app.eraseCircleX, app.eraseCircleY, app.eraseRadius, 
                   border='black', fill=None)

def onMouseRelease(app, mouseX, mouseY):
    app.drawmode = False
    app.eraseCircle = False
    if app.penMode:
        app.coloredLines[app.penQualities].append([])

def onMouseDrag(app, mouseX, mouseY):
    if app.penMode and app.drawmode:
        # Drawing mode
        app.penQualities = (app.penColor, app.penSize)
        if (app.canvasX - app.canvasWidth / 2 < mouseX < app.canvasX + app.canvasWidth / 2
            and app.canvasY - app.canvasHeight / 2 < mouseY < app.canvasY + app.canvasHeight / 2):
            if app.penQualities not in app.coloredLines:
                app.coloredLines[app.penQualities] = [[]]
                app.coloredLines[app.penQualities][-1].append((mouseX, mouseY))
            else:
                app.coloredLines[app.penQualities][-1].append((mouseX, mouseY))

    if app.eraseMode:
        # Eraser mode
        if (app.canvasX - app.canvasWidth / 2 < mouseX < app.canvasX + app.canvasWidth / 2
            and app.canvasY - app.canvasHeight / 2 < mouseY < app.canvasY + app.canvasHeight / 2):
            app.eraseCircle = True
            app.eraseCircleX = mouseX
            app.eraseCircleY = mouseY
            eraseLines(app)

def eraseLines(app):
    # Check each line segment in every stored line
    for i in range(len(app.lines)):  # Use list to avoid modifying while iterating
        newLines = []
        newCurrentLine = []
        for i in range(len(app.lines[i]) - 1):
            p1, p2 = app.lines[i], app.lines[i + 1]
            if not isSegmentIntersectingCircle(app, p1, p2):
                    newCurrentLine.append(p1)
            else:
                if newCurrentLine:
                    newLines.append(newCurrentLine)
                    newCurrentLine = []
            # Add the remaining valid segment
            if newCurrentLine or (len(app.lines[i]) == 1 and not isPointInCircle(app, app.lines[0])):
                newCurrentLine.append(app.lines[-1])
                newLines.append(newCurrentLine)
        # Update the lines with the new ones
        app.lines[i] = [l for l in newLines if len(l) > 1]

def isPointInCircle(app, point):
    # Check if a point is inside the eraser circle
    return distance(app.eraseCircleX, app.eraseCircleY, point[0], point[1]) <= app.eraseRadius

def isSegmentIntersectingCircle(app, p1, p2):
    # Check if a line segment (p1 to p2) intersects the eraser circle
    cx, cy, r = app.eraseCircleX, app.eraseCircleY, app.eraseRadius
    x1, y1, x2, y2 = *p1, *p2
    
    # Compute the distance of the line from the circle center
    dx, dy = x2 - x1, y2 - y1
    a = dx**2 + dy**2
    b = 2 * (dx * (x1 - cx) + dy * (y1 - cy))
    c = (x1 - cx)**2 + (y1 - cy)**2 - r**2
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return False  # No intersection
    discriminant = discriminant**0.5
    t1 = (-b - discriminant) / (2 * a)
    t2 = (-b + discriminant) / (2 * a)
    return (0 <= t1 <= 1 or 0 <= t2 <= 1)

def onMousePress(app, mouseX, mouseY):
    app.drawmode = True
    changeMode(app, mouseX, mouseY)

def eraseButton(app):
    drawRect(app.canvasX - (app.canvasWidth / 2) + 15 + 150,
             app.canvasY + (app.canvasHeight / 2) + 25, 
             30, 30, fill='black', align='center')

def changeMode(app, mouseX, mouseY):
    if ((app.canvasX - (app.canvasWidth / 2) + 15 + 135 <= mouseX <= app.canvasX - (app.canvasWidth / 2) + 15 + 165) and 
        (app.canvasY + (app.canvasHeight / 2) + 10 <= mouseY <= app.canvasY + (app.canvasHeight / 2) + 40)):
        app.penMode = False
        app.eraseMode = True

def distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5

def main():
    runApp()

main()