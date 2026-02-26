def isValidNotation(move):
    notationLength = len(move)
    if notationLength not in (4,5):
        return False
    
    if not (move[0].isalpha() and move[2].isalpha()):
        return False
    
    if not (move[1].isdigit() and move[3].isdigit()):
        return False


    if not (0<int(move[1])<9 and 0<int(move[3])<9):
        return False

    if not ('a'<=move[0]<='h' and 'a'<=move[2]<='h'):
        return False
    
    if notationLength == 5:
        if not move[4].lower() in [ 'r' , 'n' , 'b' , 'q']:
            return False

    return True

