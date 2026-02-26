def printBoard(board):
    for colGuide in ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ]:
        print(colGuide,end = " ")

    print()

    for _ in range(8):
        print("_" , end = " ")

    print()

    for (rowNo,row) in enumerate(board):
        for box in row:
            print(box,end = " ")
        print("|",8-rowNo)
