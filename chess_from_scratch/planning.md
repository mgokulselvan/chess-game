# CHESS
## Board
```python
Board=[
  "0" ['r' , 'n' , 'b' , 'q' , 'k' , 'b' , 'n' , 'r'],
  "1" ['p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p'],
  "2" ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
  "3" ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
  "4" ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
  "5" ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
  "6" ['P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P'],
  "7" ['R' , 'N' , 'B' , 'Q' , 'K' , 'B' , 'N' , 'R']
]      "0"   "1"   "2"   "3"   "4"   "5"   "6"   "7"
```
> **Legend**
- r/R : Rook
- n/N : Knight
- b/B : Bishop
- q/Q : Queen
- k/K : King
- p/P : Pawn  
**NOTE:** Uppercase for White Pieces and smallcase for Black Pieces

> **Notation for each square**  
![Chess Board](https://upload.wikimedia.org/wikipedia/commons/b/b6/SCD_algebraic_notation.svg)  
(0,0) -> a8  
(0,1) -> b8  
(7,6) -> g1  
(7,7) -> h1  

**Examples:**  
Move: [(1,0),(2,0)] -> a7a6  
Move (when upgrading a piece): [(6,0),(7,0),Q] -> a2a1Q

## Needed Functions
- [ ] Matrix To Chess Notation
- [ ] Chess To Matrix Notation
- [ ] Generate all Moves Possible for the current State of Board
- [ ] Simulation to check if "Check" is possible
- [ ] Simulation to check if "Checkmate" is possible
- [ ] Inputting a move(checking if the move that was input was a legal move)
- [ ] Print the Current State of The Board (With/Without the Notations as a guide)
