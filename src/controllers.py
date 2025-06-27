'''
Created on 12 Jun 2025

@author: metily
'''

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
        self.cSWAController = CrossStitchWorkConttoller(self.viewFactory,self.View)
        self.cSWAController.showView()
    
class CrossStitchWorkConttoller(object):
    def __init__(self,viewFactory,parentView):
        self.view = viewFactory.createView("CrossStitchWorkView",self,parentView)
        
    def showView(self):
        self.view.show()
        
    def onStichclick(self,event):
        self.view.updateStich(event.EventObject.Name)
        