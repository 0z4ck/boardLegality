import random


def createRandomBoard():
    pieces = ["p"]*18+["l"]*4+["n"]*4+["s"]*4+["g"]*4+["k","K"]+["r"]*2+["b"]*2
    freeplace = range(81)
    board = [["" for i in xrange(9)] for j in xrange(9)]
    for p in pieces:
        if p == "g":
            piece = random.choice([p.upper(),p])
        elif p=="k" or p=="K":
            piece = p
        else:
            piece = random.choice([p.upper(),p,"+"+p.upper(),"+"+p])
        
        pl = random.choice(freeplace)
        freeplace.remove(pl)
        filen = pl%9
        linen = pl/9
        board[linen][filen] = piece

    return board

def randTurn():
    return random.choice(["gote","sente"])


def prettifier(board):

    for bline in board:
        print(list(reversed(["  " if i==""  else i+" " if len(i)==1 else i for i in bline ])))
