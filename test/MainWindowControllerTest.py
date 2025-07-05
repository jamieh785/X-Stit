'''
Created on 14 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock, patch
import Models
from controllers import MainWindowController, CrossStitchWorkConttoller

import Views
#Define Test wide veriables
ViewFactory = Mock(spec=Views.ViewsFactory)
MWView = Mock(spec=Views.MainWindowView)
ViewFactory.createView = MagicMock(return_value=MWView)

mockedCrossStitch = Mock(spec=Models.CrossStitch)
mockCrossStitchWorkConttoller = Mock(spec=CrossStitchWorkConttoller)


class MainWindowControllerTests(unittest.TestCase):

    def setUp(self):
        self.MWController = MainWindowController(ViewFactory)
        
    def tearDown(self):
        ViewFactory.reset_mock()
        MWView.reset_mock()
        del self.MWController
        
    def test_ControllerUsesFactoryToCreateView(self):       
        ViewFactory.createView.assert_called_once_with("MainWindowView",self.MWController,None)
        self.assertEqual(self.MWController.View, MWView)
        
    def test_ContorllerShowMethod(self):
        self.MWController.showView()
        MWView.show.assert_called_once()

    def test_OnExitFunctioncallsViewExit(self):
        self.MWController.onExit(None)
        MWView.exit.assert_called_once()
        
        
    @patch('controllers.CrossStitchWorkConttoller')
    @patch('Models.CrossStitch')
    def test_NewCrossStitchWorkArea(self, mockedCrossStitchInit,mockedCSWCoontrollerInit):
        mockedCrossStitchInit.return_value = mockedCrossStitch
        mockedCSWCoontrollerInit.return_value = mockCrossStitchWorkConttoller
        self.MWController.onNewCrossStitch(None)
        
        mockedCrossStitchInit.assert_called_once()
        mockedCSWCoontrollerInit.assert_called_once_with(ViewFactory,MWView,mockedCrossStitch)
        mockCrossStitchWorkConttoller.showView.assert_called_once()
        self.assertEqual(self.MWController.cSWAController, mockCrossStitchWorkConttoller)
        
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ControllerUsesFactoryToCreateView']
    unittest.main()