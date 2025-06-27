'''
Created on 14 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock, patch
from controllers import MainWindowController, CrossStitchWorkConttoller
import Views
#Define Test wide veriables
ViewFactory = Mock(spec=Views.ViewsFactory)
MWView = Mock(spec=Views.MainWindowView)
ViewFactory.createView = MagicMock(return_value=MWView)

CrossStitchWorkConttoller = Mock(spec=CrossStitchWorkConttoller)


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
    def test_NewCrossStitchWorkArea(self, mockedCSWCoontrollerInit):
        mockedCSWCoontrollerInit.return_value = CrossStitchWorkConttoller
        self.MWController.onNewCrossStitch(None)
        
        mockedCSWCoontrollerInit.assert_called_once_with(ViewFactory,MWView)
        CrossStitchWorkConttoller.showView.assert_called_once()
        self.assertEqual(self.MWController.cSWAController, CrossStitchWorkConttoller)
        
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ControllerUsesFactoryToCreateView']
    unittest.main()