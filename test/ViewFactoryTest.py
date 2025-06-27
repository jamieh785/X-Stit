'''
Created on 15 Jun 2025

@author: metily
'''
import unittest

import Views

controller = None
parentView = None
        
class testClass(): 
    def __init__(self,controller, parentView): pass

class ViewFactoryTests(unittest.TestCase):

    def test_FactoryCreatesDefualtMainWindowView(self):
        viewFactory = Views.ViewsFactory()

        view = viewFactory.createView("MainWindowView",controller, parentView)
        self.assertIsInstance(view, Views.MainWindowView)

    def test_FactoryCreatesImplementedMainWindowView(self):
        viewFactory = Views.ViewsFactory({"MainWindowView" : testClass})

        view = viewFactory.createView("MainWindowView",controller,parentView)
        self.assertIsInstance(view, testClass)
        
    def test_FactoryCreatsDefualtCrossStitchWorkView(self):
        viewFactory = Views.ViewsFactory()
        
        view = viewFactory.createView("CrossStitchWorkView",controller,parentView)
        self.assertIsInstance(view, Views.CrossStitchWorkView)
        
    def test_FactoryCreatesImplementedCrossStitchWorkView(self):
        viewFactory = Views.ViewsFactory({"CrossStitchWorkView" : testClass})
        
        view = viewFactory.createView("CrossStitchWorkView",controller,parentView)
        self.assertIsInstance(view, testClass)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
