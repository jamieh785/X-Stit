'''
Created on 12 Jun 2025

@author: metily
'''
import unittest
import threading
import XStit

appThread = threading.Thread(target=XStit.wxRun)

class WStitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        appThread.start()
        
    @classmethod
    def tearDownClass(cls):
        print("Tests complete, please close window")
        appThread.join()

    def test1_MainScreen(self):
        
        print("Do you see Main Screen")
        self.assertEqual(input().lower(),'y')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()