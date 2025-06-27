'''
Created on 14 Jun 2025

@author: metily
'''
import Views
import wx
import inspect,sys

class WXViewFactory(Views.ViewsFactory):
    '''
    classdocs
    '''
    def __init__(self):
        wxViews = {}
        members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for member in members:
            wxViews[member[0]] = member[1]
        #Remove ViewFactory as its not a View
        wxViews.pop("WXViewFactory")
        
        Views.ViewsFactory.__init__(self,wxViews)
    
class MainWindowView(wx.Frame,Views.MainWindowView):
    
    def __init__(self, controller, parentView):
        wx.Frame.__init__(self,parentView, -1, "Main Window",size=(600, 500))
        self.makeMenuBar(controller)
   
    def show(self):
        self.Show()
        
    def exit(self):
        self.Close(True)
        
        
    def makeMenuBar(self, controller):
        fileMenu = wx.Menu()
        
        newItem = fileMenu.Append(wx.ID_NEW)
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")

        self.SetMenuBar(menuBar)
         
        self.Bind(wx.EVT_MENU, controller.onExit, exitItem)
        self.Bind(wx.EVT_MENU, controller.onNewCrossStitch, newItem)
        
        
class CrossStitchWorkView(wx.Frame, Views.CrossStitchWorkView):
   
    def __init__(self, controller,parentView):
        wx.Frame.__init__(self,parentView, -1, "Cross Stitch",size=(300, 250))
        
        self.panels = []
        
        maxColoumn = 3
        i = 0
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        
        while i < maxColoumn:
            panel = wx.Panel(self,-1, style=wx.SUNKEN_BORDER,size=(30, 25),name=str(i))
            panel.BackgroundColour = wx.WHITE
            panel.Bind(wx.EVT_LEFT_UP,controller.onStichclick)
            box.Add(panel, 1, wx.EXPAND)
            self.panels.append(panel)
            i+=1
        
        self.SetAutoLayout(False)
        self.SetSizer(box)
        self.Layout()
        
    def show(self):
        self.Show()
        
    def updateStich(self,name):
        print(name)
        self.panels[int(name)].SetBackgroundColour(wx.BLACK)
        self.Refresh(eraseBackground=True, rect=None)
    