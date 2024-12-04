import six

class Cell:
    DIRECTIONS = {'L': (0,-1), 'LT': (-1,-1), 'T': (-1,0), 'RT': (-1,1), 'R': (0,1),
                  'RB': (1,1), 'B': (1, 0), 'LB': (1, -1)}
    def __init__(self, data, rowIndx, colIndx, parent):
        self.data = data
        self.rowIndx = rowIndx
        self.colIndx = colIndx
        self.parent = parent
        self.neighbors = {}
        self.obj = None
        self.visited = False
        
    def fetchNeighbors(self, matchingFn=None):
        self.neighbors = {}
        for cellDir, (rIndx, cIndx) in six.iteritems(self.DIRECTIONS):
            cell = self.parent.cellAt(self.rowIndx + rIndx, self.colIndx + cIndx)
            if cell:
                if matchingFn:
                    if matchingFn(cell):
                        self.neighbors[cellDir] = cell
                else:
                    self.neighbors[cellDir] = cell
                            
    def store(self, data, storeFn=None):
        if storeFn:
            self.obj = storeFn(self)
        else:
            self.obj = data

    def printData(self):
        return self.data

class Matrix:
    NULL = object()
    CELL_TYPE = Cell
    
    def __init__(self, data):
        self.rows,self.cols = len(data), len(data[0])
        self.data = [Matrix.NULL] * self.cols * self.rows
        self.load(data)
        
    def load(self, data):        
        for rIndx in range(self.rows):
            for cIndx in range(self.cols):
                self.data[(rIndx * self.cols) + cIndx] = self.CELL_TYPE(data[rIndx][cIndx], rIndx, cIndx, self)

    def resetVisit(self):
        for cell in self.data:
            cell.visited = False
        
    def resetStore(self):
        for cell in self.data:
            cell.obj = None
            
    def cellAt(self, rIndx, cIndx):
        if (0 > rIndx) or (rIndx >= self.rows) or (0 > cIndx) or (cIndx >= self.cols):
            return None
        else:
            return self.data[(rIndx * self.cols) + cIndx]
            
    def fetchNeighbors(self, matchingFn=None):
        [cell.fetchNeighbors(matchingFn) for cell in self.data]
        
    def store(self, data, storeFn=None):
        self.resetVisit()
        self.resetStore()
        [cell.store(data, storeFn) for cell in self.data]
        
    def print(self, first_NRows=None, first_NCols=None, printFn=None):
        self.resetVisit()
        firstNRows = first_NRows or 10
        firstNCols = first_NCols or 10
        for rIndx in range(self.rows):
            for cIndx in range(self.cols):
                if firstNCols and cIndx > (firstNCols - 1) and (self.cols - firstNCols):
                    print("=> {} cols more.".format(self.cols - firstNCols), end=' ')
                    break
                if printFn:
                    print(printFn(self.data[(rIndx * self.cols) + cIndx]), end=' ')
                else:
                    print(self.data[(rIndx * self.cols) + cIndx].printData(), end=' ') 
            if firstNRows and rIndx > (firstNRows - 2) and (self.rows - firstNRows):
                print(".\n.\n.\n{} rows more.".format(self.rows - firstNRows), end=' ')
                break  
            print("\n")
            
class IndexedCell(Cell):
    INDEX_COUNT = 0
    
    def __init__(self, *args, **kwargs):
        super(IndexedCell, self).__init__(*args, **kwargs)
        self.index = IndexedCell.INDEX_COUNT
        IndexedCell.INDEX_COUNT += 1
            
    def printData(self):
        return (self.index, self.data)
        
class IndexedMatrix(Matrix):
    CELL_TYPE = IndexedCell
    def __init__(self, *args, **kwargs):
        IndexedCell.INDEX_COUNT = 0
        super(IndexedMatrix, self).__init__(*args, **kwargs)
        
print([item for item in dir() if not item.startswith("__")])
