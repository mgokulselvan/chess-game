from cli import gameStart
from gui.gui import startGUI

if(input("Enter C to start the game in CLI:")=='C'):
    gameStart()
if(input("Enter G to start the game in GUI:")=='G'):
    startGUI()

print("Thank you for playing the game")
