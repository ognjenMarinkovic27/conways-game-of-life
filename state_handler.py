class StateHandler:

    def __init__(self):
        pass

    def addCell(self, x_y, oldNeighborMap, oldCells):
        x, y = x_y
        neighborMap = oldNeighborMap.copy()
        cells = oldCells.copy()
        cells.add((x, y))
        neighborMap[(x, y)] = 0        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(i==0 and j==0):
                    continue
                if((x+i, y+j) in cells):
                    neighborMap[(x, y)]+=1
                if((x+i, y+j) not in neighborMap):
                    neighborMap[(x+i, y+j)]=0
                neighborMap[(x+i, y+j)]+=1

        return (neighborMap, cells)

    def removeCell(self, x_y, oldNeighborMap, oldCells):
        x, y = x_y
        neighborMap = oldNeighborMap.copy()
        cells = oldCells.copy()

        for i in range(-1, 2):
            for j in range(-1, 2):
                if(i==0 and j==0):
                    continue
                neighborMap[(x+i, y+j)]-=1
        
        cells.remove((x, y))

        return (neighborMap, cells)

    def nextState(self, grid):
        neighborMap = grid.getNeighborMap()
        cells = grid.getCells()
        newNeighborMap = neighborMap.copy()
        newCells = cells.copy()

        emptyCells = set([])
        for pos in newNeighborMap:
            if(newNeighborMap[pos] == 0):
                emptyCells.add(pos)
        for emptyCell in emptyCells:
            del newNeighborMap[emptyCell]

        for pos in neighborMap:
            if pos in cells:
                if(neighborMap[pos] < 2 or neighborMap[pos] > 3):
                    newNeighborMap, newCells = self.removeCell(pos, newNeighborMap, newCells)
            else:
                if(neighborMap[pos] == 3):
                    newNeighborMap, newCells = self.addCell(pos, newNeighborMap, newCells)
        
        return (newNeighborMap, newCells)
        