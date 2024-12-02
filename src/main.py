from cmu_graphics import *
from startPage import *
from rules import *
from setUp import *
from prompt import *
from canvas import *
from gallery import *

def start_redrawAll(app):
    drawMenuBox(app)
    drawButtons(app)
    drawIllumButtons(app)

def rules_redrawAll(app):
    drawRulesBox(app)
    drawRule(app)
    drawArrow(app)
    highlightButton(app)
    homeButton(app)

def setUp_redrawAll(app):
    drawSetUpBox(app)
    homeButton(app)
    numPlayers(app)
    drawNumPlayers(app)
    enterNames(app)
    drawNameConfirmButton(app)
    drawButtonLabels(app)
    drawButtonIlluminations(app)

def prompt_redrawAll(app):
    drawWriteScreen(app)
    drawPromptScreen(app)
    promptConfirmIllum(app)
    drawPrompt(app)


def canvas_redrawAll(app):
    colorButtons(app)
    sizeButtons(app)
    otherButtons(app)
    drawRect(app.canvasX, app.canvasY, app.canvasWidth, app.canvasHeight, align='center', fill='white', border='darkGray')
    for i in range(len(app.lines)):
        for j in range(len(app.lines[i])-1):
            drawLine(app.lines[i][j][0], app.lines[i][j][1], app.lines[i][j+1][0], app.lines[i][j+1][1], fill=app.penColorSize[i][0][0], lineWidth=app.penColorSize[i][0][1])
    drawEraser(app)
    completeDrawing(app)
    opacitySlider(app)
    selectColor(app)
    illumModes(app)
    selectSize(app)
    writeText(app)
    drawLines(app)
    drawStick(app)
    drawPromptonCanvas(app)
    drawPopUp(app)

def gallery_redrawAll(app):
    drawGalleryWord(app)
    drawEndPromptScreen(app)
    drawDrawingScreen(app)
    drawArrow(app)
    drawFinish(app)

def main():
    runAppWithScreens(initialScreen='start')

main()