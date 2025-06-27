'''
Created on 14 Jun 2025

@author: metily
'''
import unittest

from wxViews import MainWindowWXViewFactory
from Views import MainWindowView
import wx

class MainWindowWXViewTest(unittest.TestCase):


    def test_ViewFactoryCreatesView(self):
        app = wx.App()
        MWVFactory = MainWindowWXViewFactory()
        MWView = MWVFactory.createView()
        
        self.assertIsInstance(MWView, MainWindowView)
        self.assertIsInstance(MWView, wx.Frame)

    def test_ShowView(self):
        app = wx.App()
        MWVFactory = MainWindowWXViewFactory()
        MWView = MWVFactory.createView()
        
        MWView.show()
        app.MainLoop()
        print("Hello there")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()