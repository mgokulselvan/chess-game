# Missing Chess Features and Rule Fixes

## Game-ending conditions

- [x] Distinguish checkmate from stalemate when the current player has no legal moves.
- [x] Detect threefold repetition using complete position state: piece placement, side to move, castling rights, and en-passant availability.
- [ ] Implement the fifty-move draw rule by tracking moves without a pawn move or capture.
- [ ] Implement the automatic seventy-five-move draw rule.
- [ ] Detect draws by insufficient material (dead positions), including king vs. king, king and bishop vs. king, and king and knight vs. king.
- [ ] Add a command for a player to resign.
- [ ] Add a draw-offer and draw-agreement flow.
- [ ] Add optional time controls and declare a loss on time, subject to standard insufficient-mating-material exceptions.

## Rule correctness and game-state tracking

- [x] Reset castling rights when a new game is started or the game is restarted.
- [ ] Represent en-passant availability explicitly as game state rather than inferring it only from coordinate move history.
- [x] Correct attack-square detection so pawn attacks are recognized even when their target square is empty; this is required for legal castling validation.
- [x] Verify that the required king and rook are present on their original squares before allowing castling.
- [ ] Track complete position state after every move so draw rules and future rule checks use reliable data.

## Player feedback and quality

- [ ] Notify the player when their king is in check.
- [ ] Display the game result and its reason clearly (checkmate, stalemate, repetition, fifty-move rule, insufficient material, resignation, agreement, or timeout).
- [ ] Add automated tests for legal moves, check, checkmate, stalemate, castling, en passant, promotion, and every draw condition.
