from settings import *
class Game:
    def __init__(self):
        
        self.score=0
    
    def drawGrid(self,surface):
        #draw matrix
        for i in range(21):
            pygame.draw.line(surface, "white", (HOLD_BOX+(2+PADDING),PADDING+(i*CELL)), (HOLD_BOX+(2+PADDING)+BOARD_WIDTH,PADDING+(i*CELL)), width=1) 
        for i in range(11):
            pygame.draw.line(surface, "white", (HOLD_BOX+(2+PADDING)+(i*CELL),(PADDING)+BOARD_HEIGHT), (HOLD_BOX+(2+PADDING)+(i*CELL),PADDING), width=1) 
        
    def drawNextPieces(self, surface):
        return

    def drawHold(self,surface):
        return
    def drawScore(self, surface):
        return


        


        return
    