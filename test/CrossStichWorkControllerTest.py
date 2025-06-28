'''
Created on 16 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock, call

import Views
from controllers import CrossStitchWorkConttoller

#Define Test wide veriables
MWView = Mock(spec=Views.MainWindowView)

ViewFactory = Mock(spec=Views.ViewsFactory)
CSWiew = Mock(spec=Views.CrossStitchWorkView)

mockEvent = Mock()
mockEventObject = Mock()

EventObject = Mock()

ViewFactory.createView = MagicMock(return_value=CSWiew)


class CrossStichWorkControllerTest(unittest.TestCase):


    def setUp(self):
        self.CSWController = CrossStitchWorkConttoller(ViewFactory,MWView)
        mockEvent.EventObject = mockEventObject

    def tearDown(self):
        ViewFactory.reset_mock()
        CSWiew.reset_mock()
        mockEvent.reset_mock()
        mockEventObject.reset_mock()
        del self.CSWController

    def test_UsesViewFactorytoCreateView(self):
        ViewFactory.createView.assert_called_once_with("CrossStitchWorkView",self.CSWController,MWView,10,10)
        self.assertEqual(self.CSWController.view, CSWiew)
        
    def test_ShowViewFunctionShowsView(self):
        self.CSWController.showView()
        CSWiew.show.assert_called_once()

    def test_StitchClickUpdatesStitchinView(self):
        
        calls = [call("1"),call("2"),call("3")]
        
        mockEvent.EventObject.Name = "1"
        self.CSWController.onStichclick(mockEvent)
        
        mockEvent.EventObject.Name = "2"
        self.CSWController.onStichclick(mockEvent)
        
        mockEvent.EventObject.Name = "3"
        self.CSWController.onStichclick(mockEvent)

        CSWiew.updateStich.assert_has_calls(calls)
        
    def test_StitchRightClickClearsStitchinView(self):
        
        calls = [call("1"),call("2"),call("3")]
        
        mockEvent.EventObject.Name = "1"
        self.CSWController.onStichRightClick(mockEvent)
        
        mockEvent.EventObject.Name = "2"
        self.CSWController.onStichRightClick(mockEvent)
        
        mockEvent.EventObject.Name = "3"
        self.CSWController.onStichRightClick(mockEvent)

        CSWiew.clearStich.assert_has_calls(calls)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()