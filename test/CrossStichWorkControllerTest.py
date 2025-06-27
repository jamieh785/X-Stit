'''
Created on 16 Jun 2025

@author: metily
'''
import unittest
from unittest.mock import Mock, MagicMock

import Views
from controllers import CrossStitchWorkConttoller

#Define Test wide veriables
MWView = Mock(spec=Views.MainWindowView)

ViewFactory = Mock(spec=Views.ViewsFactory)
CSWiew = Mock(spec=Views.CrossStitchWorkView)
ViewFactory.createView = MagicMock(return_value=CSWiew)


class CrossStichWorkControllerTest(unittest.TestCase):


    def setUp(self):
        self.CSWController = CrossStitchWorkConttoller(ViewFactory,MWView)


    def tearDown(self):
        ViewFactory.reset_mock()
        CSWiew.reset_mock()
        del self.CSWController


    def test_UsesViewFactorytoCreateView(self):
        ViewFactory.createView.assert_called_once_with("CrossStitchWorkView",self.CSWController,MWView)
        self.assertEqual(self.CSWController.view, CSWiew)
        
    def test_ShowViewFunctionShowsView(self):
        self.CSWController.showView()
        CSWiew.show.assert_called_once()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()