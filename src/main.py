from cmu_graphics import *
from startPage import *
from rules import *
from setUp import *
from prompt import *
from canvas import *
from gallery import *
from preview import *

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

    ##############
    #SETUP APPS
    ##############
    app.numPlayersStr = ''
    app.numPlayersConfirmButton = False
    app.numPlayersConfirmButtonIllum = False
    app.numPlayersType = False
    app.numPlayersShow = False
    app.numPlayersConfirmed = False

    app.playerNames = []
    app.nameIndex = 1
    app.nameType = False
    app.name = ''
    app.nameConfirm = False
    app.nameConfirmButtonIllum = False


    ###########
    #PROMPT APPS
    ###########
    app.writeScreen = True
    app.typePrompt = False
    app.prompt = ''
    app.promptConfirm = False
    app.promptIllum = False
    app.promptList = []

    #canvas dimensions
    app.height = 800
    app.width = 800
    app.canvasHeight = app.height * 0.6
    app.canvasWidth = app.width * 0.9
    app.canvasX = app.width/2              #align = 'center'
    app.canvasY = app.height/2             #align = 'center'

    #default pen
    app.mode = 'pen'
    app.color = 'black'
    app.size = 'med'
    app.penColor = 'black'
    app.penSize = 3
    app.penQualities = (app.penColor, app.penSize)

    #storing free draw points
    app.lines = [[]]
    app.penColorSize = [[]]

    app.eraseCircle = False
    app.eraseCircleX = None
    app.eraseCircleY = None
    
    #testing
    app.drawmode = True

    #canvas selecting variables
    app.blackSelected = True
    app.redSelected, app.blueSelected, app.greenSelected, app.whiteSelected, app.yellowSelected = False, False, False, False, False
    app.penModeIllum, app.shapeModeIllum, app.eraseModeIllum, app.trashModeIllum, app.lineModeIllum, app.textModeIllum = False, False, False, False, False, False
    app.xLargeSelect, app.largeSelect, app.smallSelect = False, False, False
    app.mediumSelect = True
    app.penBack = 'forestGreen'
    app.lineBack, app.textBack, app.deleteBack, app.shapeBack, app.eraseBack = 'white', 'white', 'white', 'white', 'white'
    app.checkIllum = False

    #textMode
    app.text = ''
    app.textModeType = False
    app.textX = None
    app.textY = None
    app.textPositions = []
    app.textList = []

    #lineMode
    app.lineDragMode = False
    app.dragLinePositions = []
    app.lineStartX = None
    app.lineStartY = None
    app.lineEndX = None
    app.lineEndY = None

    #shapeMode
    app.shapeSticker = None
    app.stickX, app.stickY = None, None
    app.stickPos = []

    ###########
    #GALLERY APPS
    ###########
    app.allPlayers = []
    app.canMove = False
    app.drawNextPreview = False
    app.galleryWord = True
    app.drawFinishOn = False

    app.drawHomeIllum = False
    app.drawDrawScreen = True

def start_redrawAll(app):
    drawMenuBox(app)
    drawButtons(app)
    drawIllumButtons(app)

def rules_redrawAll(app):
    drawRulesBox(app)
    drawRule(app)
    drawArrow(app)
    homeButton1(app)
    highlightButton(app)


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
    drawCanvas(app)
    colorButtons(app)
    sizeButtons(app)
    otherButtons(app)
    completeDrawing(app)
    opacitySlider(app)
    selectColor(app)
    illumModes(app)
    selectSize(app)
    writeText(app)
    drawLines(app)
    drawStick(app)
    drawEraser(app)
    drawPromptonCanvas(app)
    drawPopUp(app)
    drawDrawWord(app)


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