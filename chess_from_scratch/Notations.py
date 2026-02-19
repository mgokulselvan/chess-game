def Notation(move):
    (r1, c1) = move[0]  #extracting from moves tuple
    (r2, c2) = move[1]

    column1=chr(97+c1)  
    column2=chr(97+c2)
    row1=str(8-r1)
    row2=str(8-r2)

    notation=column1+row1+column2+row2
    if len(move) == 3: #promotion
        notation += move[2]

    return notation

def moves(notation):

    c1 = ord(notation[0]) - 97
    c2 = ord(notation[2]) - 97
    r1 = 8 - int(notation[1])
    r2 = 8 - int(notation[3])

    if len(notation) == 5:  # promotion
        return [(r1,c1),(r2,c2),notation[4]]
    return [(r1,c1),(r2,c2)]
