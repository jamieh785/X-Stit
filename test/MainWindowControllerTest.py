'''
Created on 14 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock
from controllers import MainWindowController
from Views import MainWindowViewFactory, MainWindowView

#Define Test wide veriables
MWVFactory = Mock(spec=MainWindowViewFactory)
MWView = Mock(spec=MainWindowView)
MWVFactory.createView = MagicMock(return_value=MWView)

class MainWindowControllerTests(unittest.TestCase):

    def tearDown(self):
        MWVFactory.reset_mock()
        MWView.reset_mock()
        
    def test_ControllerUsesFactoryToCreateView(self):
        
        MWController = MainWindowController(MWVFactory)
        
        MWVFactory.createView.assert_called_once()
        self.assertEqual(MWController.View, MWView)
        
    def test_ContorllerShowMethod(self):
        
        MWController = MainWindowController(MWVFactory)
        MWController.showView()
        MWView.show.assert_called_once()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ControllerUsesFactoryToCreateView']
    unittest.main()