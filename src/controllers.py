'''
Created on 12 Jun 2025

@author: metily
'''

class MainWindowController(object):
    '''
    classdocs
    '''


    def __init__(self,viewFactory):
        '''
        Constructor
        '''
        self.View = viewFactory.createView()
        
    def showView(self):
        self.View.show()