'''
Created on 14 Jun 2025

@author: metily
'''
import Views
import wx

class MainWindowWXViewFactory(Views.MainWindowViewFactory):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def createView(self):
        return MainWindowWXView()
    
class MainWindowWXView(wx.Frame,Views.MainWindowView):
    
    def __init__(self):
        wx.Frame.__init__(self,None, -1, "Main Window",size=(300, 250))

        
    def show(self):
        self.Show()