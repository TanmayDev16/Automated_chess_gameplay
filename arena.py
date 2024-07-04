import chess
import group1
import group2
import chess.svg
from time import sleep
import cairosvg
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

board = chess.Board()
white = group1.group1("white")
black = group2.group2("black")
winner = "tie"

gameOver = False
iterations = 0
turn =-1
svgcontent = chess.svg.board(board, size=350)
img_png = cairosvg.svg2png(svgcontent)
img = Image.open(BytesIO(img_png))
plt.imshow(img)
plt.draw()
plt.pause(0.001)
plt.draw()
plt.pause(0.001)
plt.draw()
plt.pause(0.001)
sleep(1)

while not gameOver and (iterations<10000):
    if(turn<0):
        #logic for white move
        print('Whites move')
        move = white.makemove(board)
        if chess.Move.from_uci(move) in board.legal_moves:
            uci_move = chess.Move.from_uci(move)
            board.push(uci_move)
        else:
            winner = "black"
            gameOver = True
        
        if board.is_checkmate():
            winner = "white"
            gameOver = True
            
        if board.is_stalemate():
            winner = "tie"
            gameOver = True
            
        svgcontent = chess.svg.board(board, size=350)
        img_png = cairosvg.svg2png(svgcontent)
        img = Image.open(BytesIO(img_png))
        plt.imshow(img)
        plt.draw()
        plt.pause(0.001)
            
    else:
        #logic for black move
        print('Blacks move')
        move = black.makemove(board)
        if chess.Move.from_uci(move) in board.legal_moves:
            uci_move = chess.Move.from_uci(move)
            board.push(uci_move)
        else:
            winner = "white"
            gameOver = True
            
        if board.is_checkmate():
            winner = "black"
            gameOver = True
            
        if board.is_stalemate():
            winner = "tie"
            gameOver = True
            
        svgcontent = chess.svg.board(board, size=350)
        img_png = cairosvg.svg2png(svgcontent)
        img = Image.open(BytesIO(img_png))
        plt.imshow(img)
        plt.draw()
        plt.pause(0.001)
        
    iterations = iterations+1
    turn = turn*-1
    sleep(1)
    
print("And the winner is .... "+winner)
    