from utils import util
import chcklgl


board = util.createRandomBoard()

util.prettifier(board)
turn = util.randTurn()
print "turn: "+turn
chcklgl.checkLegal(board,turn)


