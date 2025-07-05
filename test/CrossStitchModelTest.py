'''
Created on 29 Jun 2025

@author: metily
'''
import unittest

from Models import CrossStitch

class Test(unittest.TestCase):

        
    def test_CreateViewWithCorrectRowsColoumns(self):
        crossStitch = CrossStitch(10,10)
        

        for x in range(10):
            for y in range(10):
                self.assertEqual(crossStitch.getStitch(x,y), None)
 

    def test_updateAllStitcheswithRGBValue(self):
        crossStitch = CrossStitch(10,10)
        
        for y in range(10):
            for x in range(10):
                crossStitch.updateStitch(x,y)
                
        for y in range(10):
            for x in range(10):
                self.assertEqual(crossStitch.getStitch(x,y), (255,255,255))
                
    def test_updateSelectedSticheswithRGBValue(self):
        crossStitch = CrossStitch(10,10)
        crossStitch.updateStitch(1,1)
        crossStitch.updateStitch(2,3)
        crossStitch.updateStitch(5,4)
        
        for y in range(10):
            for x in range(10):
                if (x == 1 and y == 1) or (x == 2 and y == 3) or (x == 5 and y == 4):
                    self.assertEqual(crossStitch.getStitch(x,y), (255,255,255))
                else:
                    self.assertEqual(crossStitch.getStitch(x,y), None)

    def test_CLearAllStitches(self):
        crossStitch = CrossStitch(10,10)
        
        for y in range(10):
            for x in range(10):
                crossStitch.updateStitch(x,y)
            
        for y in range(10):
            for x in range(10):
                crossStitch.clearStitch(x,y)
                
        for y in range(10):
            for x in range(10):
                self.assertEqual(crossStitch.getStitch(x,y), None)
                
    def test_ClearSelectedStiches(self):
        crossStitch = CrossStitch(10,10)
        
        for y in range(10):
            for x in range(10):
                crossStitch.updateStitch(x,y)
                
        crossStitch.clearStitch(1,1)
        crossStitch.clearStitch(2,3)
        crossStitch.clearStitch(5,4)       
                
        for y in range(10):
            for x in range(10):
                if (x == 1 and y == 1) or (x == 2 and y == 3) or (x == 5 and y == 4):
                    self.assertEqual(crossStitch.getStitch(x,y), None)
                else:
                    self.assertEqual(crossStitch.getStitch(x,y), (255,255,255))
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_CreateViewWithRowsColoumns']
    unittest.main()