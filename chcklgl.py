

def checkLegal(board, turn):
    #check nifu
    for filen in range(9):
        if [line[filen] for line in board].count("P")>1:
            print "nifu for sente"
            legal = False
        if [line[filen] for line in board].count("p")>1:
            print "nifu for gote"
            legal = False
    #check furthest pawn, lance, penultimate knight
    if "P" in board[0]:
        print "furthest pawn for sente"
        legal = False
    if "L" in board[0]:
        print "furthest lance for sente"
        legal = False
    for line in board[:2]:
        if "N" in line:
            print "penultimate knight for sente"
            legal = False
    if "p" in board[8]:
        print "furthest pawn for gote"
        legal = False
    if "l" in board[8]:
        print "furthest lance for gote"
        legal = False
    for line in board[7:]:
        if "n" in line:
            print "penultimate knight for gote"
            legal = False
    #check king check
    if turn == "gote":
        for linen in range(9):
             if "K" in board[linen]:
                 kfilen = board[linen].index("K")
                 klinen = linen
                 break
        if klinen > 1 :
            #check knight's check
            if kfilen == 8:
                if board[klinen-2][kfilen-1] == "n":
                    legal = False
                    print "knight is checking to sente"
            elif kfilen == 0:
                if board[klinen-2][kfilen+1] == "n":
                    legal = False
                    print "knight is checking to sente"
            else:
                if board[klinen-2][kfilen-1] == "n" or board[klinen-2][kfilen+1] == "n":
                    legal = False
                    print "knight is checking to sente"
        if klinen != 0 :
            #check king's front check
            if board[klinen-1][kfilen] in ["p","l","s","g","k","r","+p","+l","+n","+s","+b","+r"]:
                legal = False
                print "{} is checking to sente from the front".format(board[klinen-1][kfilen])
            if kfilen == 8:
                if board[klinen-1][kfilen-1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the front right".format(board[klinen-1][kfilen-1])
            elif kfilen == 0:
                if board[klinen-1][kfilen+1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the front left".format(board[klinen-1][kfilen+1])
            else:
                if board[klinen-1][kfilen-1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the front right".format(board[klinen-1][kfilen-1])
                if board[klinen-1][kfilen+1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the front left".format(board[klinen-1][kfilen+1])

        if kfilen != 0:
            #check king's right side
            if board[klinen][kfilen-1] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                legal = False
                print "{} is checking to sente from the right".format(board[klinen][kfilen-1])
        if kfilen != 8:
            #check king's left side
            if board[klinen][kfilen+1] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                legal = False
                print "{} is checking to sente from the left".format(board[klinen][kfilen+1])
        if klinen != 8:
            #check king's back
            if board[klinen+1][kfilen] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                legal = False
                print "{} is checking to sente from the back".format(board[klinen+1][kfilen])
            if kfilen == 8:
                if board[klinen+1][kfilen-1] in ["s","k","b","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the back right".format(board[klinen+1][kfilen-1])
            elif kfilen == 0:
                if board[klinen+1][kfilen+1] in ["s","k","b","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the back left".format(board[klinen+1][kfilen+1])
            else:
                if board[klinen+1][kfilen-1] in ["s","k","b","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the back right".format(board[klinen+1][kfilen-1])
                if board[klinen+1][kfilen+1] in ["s","k","b","+b","+r"]:
                    legal = False
                    print "{} is checking to sente from the back left".format(board[klinen+1][kfilen+1])
        #check rook's check
        for piece in reversed(board[klinen][:kfilen]):
            if piece == "r" or piece == "+r":
                legal = False
                print "rook is checking from the right"
                break
            elif piece != "":
                break
        for piece in board[klinen][kfilen+1:]:
            if piece == "r" or piece == "+r":
                legal = False
                print "rook is checking from the left"
                break
            elif piece != "":
                break
        for piece in reversed([line[kfilen] for line in board][:klinen]):
            if piece == "r" or piece == "+r":
                legal = False
                print "rook is checking from the front"
                break
            elif piece != "":
                break
        for piece in [line[kfilen] for line in board][klinen+1:]:
            if piece == "r" or piece == "+r":
                legal = False
                print "rook is checking from the back"
                break
            elif piece != "":
                break
        #check bishop's check #the hardest part
        for i in range(1,9):
            if kfilen+i > 8 or klinen+i > 8:
                break
            if board[klinen+i][kfilen+i] == "b" or board[klinen+i][kfilen+i] == "+b":
                legal = False
                print "bishop is checking from the back left"
                break
            elif board[klinen+i][kfilen+i] != "":
                break
        for i in range(1,9):
            if kfilen-i < 0 or klinen-i < 0:
                break
            if board[klinen-i][kfilen-i] == "b" or board[klinen-i][kfilen-i] == "+b":
                legal = False
                print "bishop is checking from the front right"
                break
            elif board[klinen-i][kfilen-i] != "":
                break
        for i in range(1,9):
            if kfilen+i > 8 or klinen-i < 0:
                break
            if board[klinen-i][kfilen+i] == "b" or board[klinen-i][kfilen+i] == "+b":
                legal = False
                print "bishop is checking from the front left"
                break
            elif board[klinen-i][kfilen+i] != "":
                break
        for i in range(1,9):
            if kfilen-i < 0 or klinen+i > 8:
                break
            if board[klinen+i][kfilen-i] == "b" or board[klinen+i][kfilen-i] == "+b":
                legal = False
                print "bishop is checking from the back right"
                break
            elif board[klinen+i][kfilen-i] != "":
                break


