from enum import Enum

#CUSTOM ERROR
class InvalidMoveError(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return self.message

#ENUM FOR MOVE STATUS
class TURN(Enum):
    WHITE = "white"
    BLACK = "black"

def is_enemy(piece,turn):
    if (turn==TURN.WHITE and piece.islower())\
            or\
        (turn==TURN.BLACK and piece.isupper()):
        return True
    else:
        return False
