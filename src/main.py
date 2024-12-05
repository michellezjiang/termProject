from cmu_graphics import *
from startPage import *
from rules import *
from setUp import *
from prompt import *
from canvas import *
from gallery import *
from preview import *

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
    completeDrawing(app)
    opacitySlider(app)
    selectColor(app)
    illumModes(app)
    selectSize(app)
    writeText(app)
    drawLines(app)
    drawStick(app)
    drawEraserLines(app)
    drawEraser(app)
    drawPromptonCanvas(app)
    drawPopUp(app)

def preview_redrawAll(app):
    drawPreview(app)

def gallery_redrawAll(app):
    drawGalleryWord(app)
    drawEndPromptScreen(app)
    drawDrawingScreen(app)
    drawFinalArrow(app)
    drawFinish(app)
    drawReturnHomeIllum(app)

def main():
    runAppWithScreens(initialScreen='start')

main()