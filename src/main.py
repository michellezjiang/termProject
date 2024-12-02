from cmu_graphics import *
from startPage import *
from rules import *
from setUp import *

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

def main():
    runAppWithScreens(initialScreen='start')

main()