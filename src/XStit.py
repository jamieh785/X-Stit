'''
Created on 12 Jun 2025

@author: metily
'''

from controllers import MainWindowController
from wxViews import MainWindowWXViewFactory
import wx


def wxRun():
    
    app = wx.App()
    controller = MainWindowController(MainWindowWXViewFactory())
    controller.showView()
    app.MainLoop()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    wxRun()