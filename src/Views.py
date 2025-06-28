'''
Created on 14 Jun 2025

@author: metily
'''

import sys, inspect

class ViewsFactory():
    '''
    Factory class to hold View classes for the controllers to use when needed
    '''
    def __init__(self,views={}):
        #self.__views = views
        defualtViews = self.createDefualtViews()
        
        #Check supplied views for any implemented views
        for view in defualtViews.keys():
            if view in views:
                defualtViews[view] = views[view]
                
        self.__views = defualtViews
    
    def createView(self,view,*args):
        return self.__views[view](*args)
    
    def createDefualtViews(self):
        defualtViews = {}
        viewClasses = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for view in viewClasses:
            defualtViews[view[0]] = view[1]
        #Remove ViewFactory as its not a View
        defualtViews.pop("ViewsFactory")
        return defualtViews
        
class MainWindowView():
    '''
    Base Class for Main Window Window View
    '''
    def __init__(self, controller, parentView):
        pass
    
    def show(self):
        pass
    
    def exit(self):
        pass

class CrossStitchWorkView():
    '''
    Base Class for Cross Stitch work area
    '''
    def __init__(self, controller,parentView):
        pass
    
    def show(self):
        pass
    
    def updateStich(self):
        pass
    
    def clearStich(self):
        pass