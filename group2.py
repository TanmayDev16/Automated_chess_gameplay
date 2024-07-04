# import chess
# # Piece evaluation matrices
# pawn_eval_white = [
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#     [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
#     [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
#     [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
#     [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
#     [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
#     [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# ]

# pawn_eval_black = list(reversed(pawn_eval_white))

# knight_eval = [
#     [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
#     [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
#     [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
#     [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
#     [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
#     [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
#     [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
#     [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
# ]

# bishop_eval_white = [
#     [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
#     [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
#     [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
#     [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
#     [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
#     [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
#     [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
#     [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
# ]

# bishop_eval_black = list(reversed(bishop_eval_white))

# rook_eval_white = [
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#     [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
#     [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
#     [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
#     [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
#     [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
#     [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
#     [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
# ]

# rook_eval_black = list(reversed(rook_eval_white))

# queen_eval = [
#     [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
#     [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
#     [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
#     [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
#     [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
#     [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
#     [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
#     [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
# ]

# king_eval_white = [
#     [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
#     [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
#     [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
#     [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
#     [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
#     [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
#     [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
#     [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
# ]

# king_eval_black = list(reversed(king_eval_white))

# class group2:
#     def __init__(self, color):
#         self.color = color

#     def makemove(self, board):
#         best_move = self.make_best_move_alpha_beta(board, depth=4)  
#         return board.uci(best_move) if best_move else None

#     def evaluate_board(self, board):
#         total_evaluation = 0
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             piece_value = self.get_piece_value(piece, square)
#             if piece_value is not None:
#                 total_evaluation += piece_value
#         return total_evaluation

#     def get_piece_value(self, piece, square):
#         if piece is None:
#             return 0
            
#         piece_type = piece.piece_type
#         piece_color = piece.color

#         if piece_type == chess.PAWN:
#             return 10 + (pawn_eval_white[square // 8][square % 8] if piece_color == chess.WHITE else -pawn_eval_black[square // 8][square % 8])
#         elif piece_type == chess.KNIGHT:
#             return 30 + (knight_eval[square // 8][square % 8] if piece_color == chess.WHITE else -knight_eval[square // 8][square % 8])
#         elif piece_type == chess.BISHOP:
#             return 30 + (bishop_eval_white[square // 8][square % 8] if piece_color == chess.WHITE else -bishop_eval_black[square // 8][square % 8])
#         elif piece_type == chess.ROOK:
#             return 50 + (rook_eval_white[square // 8][square % 8] if piece_color == chess.WHITE else -rook_eval_black[square // 8][square % 8])
#         elif piece_type == chess.QUEEN:
#             return 90 + (queen_eval[square // 8][square % 8] if piece_color == chess.WHITE else -queen_eval[square // 8][square % 8])
#         elif piece_type == chess.KING:
#             return 900 + (king_eval_white[square // 8][square % 8] if piece_color == chess.WHITE else -king_eval_black[square // 8][square % 8])

#     def make_best_move_alpha_beta(self, board, depth):
#         best_move = None
#         best_value = -float('inf')
#         alpha = -float('inf')
#         beta = float('inf')

#         # Sort moves primarily by capture, which is a common heuristic to improve pruning
#         moves = list(board.legal_moves)
#         moves.sort(key=lambda move: self.move_heuristic(board, move), reverse=True)

#         for move in moves:
#             board.push(move)
#             board_value = -self.minimax_alpha_beta(depth - 1, board, alpha, beta, False)
#             board.pop()
#             if board_value > best_value:
#                 best_value = board_value
#                 best_move = move
#                 alpha = max(alpha, board_value)  # Update alpha after finding a new best move
#         return best_move

#     def minimax_alpha_beta(self, depth, board, alpha, beta, is_maximizing_player):
#         if depth == 0 or board.is_game_over():
#             return self.evaluate_board(board)

#         legal_moves = list(board.legal_moves)
#         if is_maximizing_player:
#             max_eval = -float('inf')
#             for move in legal_moves:
#                 board.push(move)
#                 current_eval = self.minimax_alpha_beta(depth - 1, board, alpha, beta, False)
#                 board.pop()
#                 max_eval = max(max_eval, current_eval)
#                 alpha = max(alpha, current_eval)
#                 if beta <= alpha:
#                     break
#             return max_eval
#         else:
#             min_eval = float('inf')
#             for move in legal_moves:
#                 board.push(move)
#                 current_eval = self.minimax_alpha_beta(depth - 1, board, alpha, beta, True)
#                 board.pop()
#                 min_eval = min(min_eval, current_eval)
#                 beta = min(beta, current_eval)
#                 if beta <= alpha:
#                     break
#             return min_eval

#     def move_heuristic(self, board, move):
#         score = 0
#         if board.is_capture(move):
#             return 10 + abs(self.get_piece_value(board.piece_at(move.to_square), move.to_square))
        
#         if move.to_square in [chess.D4, chess.D5, chess.E4, chess.E5]:
#             score += 5 
#         return score   
            




import chess
import random

class group2:
    def __init__(self, color):
        self.color = color
        
    def makemove(self, board):
        retmove=""
        legal_moves = board.legal_moves
        print("The list of legal moves are: ")
        print(legal_moves)
        chosen_move = random.choice(list(legal_moves))
        retmove = board.uci(chosen_move)

        return retmove


# import chess

# class group2:
#     def __init__(self, color):
#         self.color = color

#     def evaluate_board(self, board):
#         evaluation = 0
#         evaluation += self.material_score(board)
#         evaluation += self.positional_score(board)
#         return evaluation

#     def material_score(self, board):
#         material_score = 0
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             if piece is not None:
#                 value = {
#                     chess.PAWN: 100,
#                     chess.KNIGHT: 320,
#                     chess.BISHOP: 330,
#                     chess.ROOK: 500,
#                     chess.QUEEN: 900,
#                     chess.KING: 20000
#                 }.get(piece.piece_type, 0)
#                 material_score += value if piece.color == chess.WHITE else -value
#         return material_score

#     def positional_score(self, board):
#         positional_score = 0
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             if piece is not None:
#                 value = {
#                     chess.PAWN: self.pawn_table[square],
#                     chess.KNIGHT: self.knight_table[square],
#                     chess.BISHOP: self.bishop_table[square],
#                     chess.ROOK: self.rook_table[square],
#                     chess.QUEEN: self.queen_table[square],
#                     chess.KING: self.king_table_endgame[square] if board.is_checkmate() else self.king_table[square]
#                 }.get(piece.piece_type, 0)
#                 positional_score += value if piece.color == chess.WHITE else -value
#         return positional_score

#     # Tables for positional scores (adjust these as needed)
#     pawn_table = [
#         0,  0,  0,  0,  0,  0,  0,  0,
#         5, 10, 10,-20,-20, 10, 10,  5,
#         5, -5,-10,  0,  0,-10, -5,  5,
#         0,  0,  0, 20, 20,  0,  0,  0,
#         5,  5, 10, 25, 25, 10,  5,  5,
#         10, 10, 20, 30, 30, 20, 10, 10,
#         50, 50, 50, 50, 50, 50, 50, 50,
#         0,  0,  0,  0,  0,  0,  0,  0
#     ]

#     knight_table = [
#         -50,-40,-30,-30,-30,-30,-40,-50,
#         -40,-20,  0,  0,  0,  0,-20,-40,
#         -30,  0, 10, 15, 15, 10,  0,-30,
#         -30,  5, 15, 20, 20, 15,  5,-30,
#         -30,  0, 15, 20, 20, 15,  0,-30,
#         -30,  5, 10, 15, 15, 10,  5,-30,
#         -40,-20,  0,  5,  5,  0,-20,-40,
#         -50,-40,-20,-30,-30,-20,-40,-50
#     ]

#     bishop_table = [
#         -20,-10,-10,-10,-10,-10,-10,-20,
#         -10,  0,  0,  0,  0,  0,  0,-10,
#         -10,  0,  5, 10, 10,  5,  0,-10,
#         -10,  5,  5, 10, 10,  5,  5,-10,
#         -10,  0, 10, 10, 10, 10,  0,-10,
#         -10, 10, 10, 10, 10, 10, 10,-10,
#         -10,  5,  0,  0,  0,  0,  5,-10,
#         -20,-10,-40,-10,-10,-40,-10,-20
#     ]

#     rook_table = [
#         0,  0,  0,  0,  0,  0,  0,  0,
#         5, 10, 10, 10, 10, 10, 10,  5,
#     -5,  0,  0,  0,  0,  0,  0, -5,
#     -5,  0,  0,  0,  0,  0,  0, -5,
#     -5,  0,  0,  0,  0,  0,  0, -5,
#     -5,  0,  0,  0,  0,  0,  0, -5,
#     -5,  0,  0,  0,  0,  0,  0, -5,
#         0,  0,  0,  5,  5,  0,  0,  0
#     ]


#     queen_table = [
#         -20,-10,-10, -5, -5,-10,-10,-20,
#         -10,  0,  0,  0,  0,  0,  0,-10,
#         -10,  0,  5,  5,  5,  5,  0,-10,
#          -5,  0,  5,  5,  5,  5,  0, -5,
#           0,  0,  5,  5,  5,  5,  0, -5,
#         -10,  5,  5,  5,  5,  5,  0,-10,
#         -10,  0,  5,  0,  0,  0,  0,-10,
#         -20,-10,-10, -5, -5,-10,-10,-20
#     ]

#     king_table = [
#         -30,-40,-40,-50,-50,-40,-40,-30,
#         -30,-40,-40,-50,-50,-40,-40,-30,
#         -30,-40,-40,-50,-50,-40,-40,-30,
#         -30,-40,-40,-50,-50,-40,-40,-30,
#         -20,-30,-30,-40,-40,-30,-30,-20,
#         -10,-20,-20,-20,-20,-20,-20,-10,
#          20, 20,  0,  0,  0,  0, 20, 20,
#          20, 30, 10,  0,  0, 10, 30, 20
#     ]

#     king_table_endgame = [
#         -50,-40,-30,-20,-20,-30,-40,-50,
#         -30,-20,-10,  0,  0,-10,-20,-30,
#         -30,-10, 20, 30, 30, 20,-10,-30,
#         -30,-10, 30, 40, 40, 30,-10,-30,
#         -30,-10, 30, 40, 40, 30,-10,-30,
#         -30,-10, 20, 30, 30, 20,-10,-30,
#         -30,-30,  0,  0,  0,  0,-30,-30,
#         -50,-30,-30,-30,-30,-30,-30,-50
#     ]

#     def evaluate_board(self, board):
#         evaluation = 0
#         evaluation += self.material_score(board)
#         evaluation += self.positional_score(board)
#         return evaluation

#     def material_score(self, board):
#         material_score = 0
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             if piece is not None:
#                 value = {
#                     chess.PAWN: 100,
#                     chess.KNIGHT: 320,
#                     chess.BISHOP: 330,
#                     chess.ROOK: 500,
#                     chess.QUEEN: 900,
#                     chess.KING: 20000
#                 }.get(piece.piece_type, 0)
#                 material_score += value if piece.color == chess.WHITE else -value
#         return material_score

#     def positional_score(self, board):
#         positional_score = 0
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             if piece is not None:
#                 value = {
#                     chess.PAWN: self.pawn_table[square],
#                     chess.KNIGHT: self.knight_table[square],
#                     chess.BISHOP: self.bishop_table[square],
#                     chess.ROOK: self.rook_table[square],
#                     chess.QUEEN: self.queen_table[square],
#                     chess.KING: self.king_table_endgame[square] if board.is_checkmate() else self.king_table[square]
#                 }.get(piece.piece_type, 0)
#                 positional_score += value if piece.color == chess.WHITE else -value
#         return positional_score

#     def makemove(self, board):
#         best_move = None
#         max_eval = float('-inf')
#         alpha = float('-inf')
#         beta = float('inf')
#         depth = 4  # Depth of minimax search

#         legal_moves = list(board.legal_moves)
#         history_table = {}  # Initialize history table

#         for move in legal_moves:
#             board.push(move)
#             eval = self.minimax(board, depth - 1, alpha, beta, False)
#             board.pop()
#             if eval > max_eval:
#                 max_eval = eval
#                 best_move = move
#             alpha = max(alpha, eval)

#             # Update history table
#             if move in history_table:
#                 history_table[move] += 1
#             else:
#                 history_table[move] = 1

#         return best_move.uci() if best_move is not None else None

#     def minimax(self, board, depth, alpha, beta, maximizing_player):
#         if depth == 0 or board.is_game_over():
#             return self.evaluate_board(board)

#         legal_moves = list(board.legal_moves)
#         if maximizing_player:
#             max_eval = float('-inf')
#             for move in legal_moves:
#                 board.push(move)
#                 eval = self.minimax(board, depth - 1, alpha, beta, False)
#                 board.pop()
#                 max_eval = max(max_eval, eval)
#                 alpha = max(alpha, eval)
#                 if beta <= alpha:
#                     break  # Alpha-beta pruning
#             return max_eval
#         else:
#             min_eval = float('inf')
#             for move in legal_moves:
#                 board.push(move)
#                 eval = self.minimax(board, depth - 1, alpha, beta, True)
#                 board.pop()
#                 min_eval = min(min_eval, eval)
#                 beta = min(beta, eval)
#                 if beta <= alpha:
#                     break  # Alpha-beta pruning
#             return min_eval