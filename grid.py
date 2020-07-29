from state_handler import StateHandler

class Grid:

    def __init__(self, neighborMap = {}, cells = set([])):
        self.__neighborMap = neighborMap
        self.__cells = cells
        self.__stateHandler = StateHandler()

    def addCell(self, x_y):
        newState = self.__stateHandler.addCell(x_y, self.__neighborMap, self.__cells)
        self.__neighborMap, self.__cells = newState

    def removeCell(self, x_y):
        newState = self.__stateHandler.removeCell(x_y, self.__neighborMap, self.__cells)
        self.__neighborMap, self.__cells = newState

    def nextState(self):
        newState = self.__stateHandler.nextState(self)
        self.__neighborMap, self.__cells = newState
       
    def getNeighborMap(self):
        return self.__neighborMap
 
    def getCells(self):
        return self.__cells

    def isCellLive(self, x_y):
        return x_y in self.__cells
    