def printBoard(board):
    for colGuide in ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ]:
        print(colGuide + '\u0332' ,end = " \u0332")

    print()

    for (rowNo,row) in enumerate(board):
        for box in row:
            print(box,end = " ")
        print("│",str(8-rowNo)+'\u0332' , sep = '' )
