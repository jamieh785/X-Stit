'''
Created on 14 Jun 2025

@author: metily
'''
from abc import abstractmethod, ABC

class MainWindowViewFactory(ABC):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @abstractmethod
    def createView(self):
        ...
        
class MainWindowView():
    '''
    Base Class for Main Window Window View
    '''
    
    def __init__(self):
        pass
    
    def show(self):
        pass