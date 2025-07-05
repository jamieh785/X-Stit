'''
Created on 12 Jun 2025

@author: metily
'''

import Models

class MainWindowController(object):
    '''
    classdocs
    '''
    def __init__(self,viewFactory):
        self.View = viewFactory.createView("MainWindowView",self, None)
        self.viewFactory = viewFactory
        
    def showView(self):
        self.View.show()
        
    def onExit(self,event):
        self.View.exit()
        
    def onNewCrossStitch(self,event):
        crossStitch = Models.CrossStitch(10,10)
        self.cSWAController = CrossStitchWorkConttoller(self.viewFactory,self.View,crossStitch)
        self.cSWAController.showView()
    
class CrossStitchWorkConttoller(object):
    def __init__(self,viewFactory,parentView,crossStitch):
        self.crossStitch = crossStitch
        self.view = viewFactory.createView("CrossStitchWorkView",self,parentView,crossStitch.rows,crossStitch.coloumns)
        
    def showView(self):
        self.view.show()
        
    def onStichclick(self,event):
        stitchID = event.EventObject.Name
        x,y = self.stitchIDtoXY(stitchID)
        self.crossStitch.updateStitch(x,y)
        self.view.updateStich(stitchID)
        
    def onStichRightClick(self,event):
        stitchID = event.EventObject.Name
        x,y = self.stitchIDtoXY(stitchID)
        self.crossStitch.clearStitch(x,y)
        self.view.clearStich(stitchID)
        
    def stitchIDtoXY(self,stitchID):
        splitID = stitchID.split(",")
        return int(splitID[0]), int(splitID[1])