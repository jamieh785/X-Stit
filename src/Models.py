'''
Created on 28 Jun 2025

@author: metily
'''

class CrossStitch(object):
    '''
    Model of Cross Stitch pattern 
    '''
    def __init__(self,rows,coloumns):
        self.rows=rows
        self.coloumns = coloumns
        self.stitch=[]

        for y in range(coloumns):
            self.stitch.append(self.__createRow(rows))
        
    def getStitch(self, x, y):
        return self.stitch[x][y]
    
    def updateStitch(self,x,y):
        self.stitch[x][y] = (255,255,255)
    
    def clearStitch(self,x,y):
        self.stitch[x][y] = None
    
    
    
    def __createRow(self, maxColoumns):
        row = []
        
        for x in range(maxColoumns):
            row.append(None)
            
        return row