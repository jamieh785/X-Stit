'''
Created on 16 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock, call

import Views
from controllers import CrossStitchWorkConttoller
from Models import CrossStitch

#Define Test wide veriables
MWView = Mock(spec=Views.MainWindowView)

ViewFactory = Mock(spec=Views.ViewsFactory)
CSWiew = Mock(spec=Views.CrossStitchWorkView)

mockEvent = Mock()
mockEventObject = Mock()

mockCrossStitch = Mock(spec=CrossStitch)

ViewFactory.createView = MagicMock(return_value=CSWiew)


class CrossStichWorkControllerTest(unittest.TestCase):

    def setUp(self):
        mockCrossStitch.rows = 10
        mockCrossStitch.coloumns = 10
        self.CSWController = CrossStitchWorkConttoller(ViewFactory,MWView,mockCrossStitch)
        mockEvent.EventObject = mockEventObject
        

    def tearDown(self):
        ViewFactory.reset_mock()
        CSWiew.reset_mock()
        mockEvent.reset_mock()
        mockEventObject.reset_mock()
        mockCrossStitch.reset_mock()
        del self.CSWController

    def test_UsesViewFactorytoCreateView(self):
        ViewFactory.createView.assert_called_once_with("CrossStitchWorkView",self.CSWController,MWView,mockCrossStitch.rows,mockCrossStitch.coloumns)
        self.assertEqual(self.CSWController.view, CSWiew)
        
    def test_ShowViewFunctionShowsView(self):
        self.CSWController.showView()
        CSWiew.show.assert_called_once()

    def test_StitchClickUpdatesStitchinView(self):
        
        viewCalls = [call("1,1"),call("2,3"),call("5,4")]
        stitchCalls = [call(1,1),call(2,3),call(5,4)]
        
        mockEvent.EventObject.Name = "1,1"
        self.CSWController.onStichclick(mockEvent)
        
        mockEvent.EventObject.Name = "2,3"
        self.CSWController.onStichclick(mockEvent)
        
        mockEvent.EventObject.Name = "5,4"
        self.CSWController.onStichclick(mockEvent)

        CSWiew.updateStich.assert_has_calls(viewCalls)
        mockCrossStitch.updateStitch.assert_has_calls(stitchCalls)
        
    def test_StitchRightClickClearsStitchinView(self):
        
        viewCalls = [call("1,1"),call("2,3"),call("5,4")]
        stitchCalls = [call(1,1),call(2,3),call(5,4)]
        
        mockEvent.EventObject.Name = "1,1"
        self.CSWController.onStichRightClick(mockEvent)
        
        mockEvent.EventObject.Name = "2,3"
        self.CSWController.onStichRightClick(mockEvent)
        
        mockEvent.EventObject.Name = "5,4"
        self.CSWController.onStichRightClick(mockEvent)

        CSWiew.clearStich.assert_has_calls(viewCalls)
        mockCrossStitch.clearStitch.assert_has_calls(stitchCalls)

    
    def test_NewCrossStictchViewCreatesNewCrossStitch(self):
        self.assertEqual(self.CSWController.crossStitch, mockCrossStitch)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()