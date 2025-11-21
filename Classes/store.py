from value import Value

class Store:
    def __init__(self, nCells: int, storeMap: dict[int,Value]):
        self.nCells = nCells
        self.storeMap = storeMap
    
    class StoreError(Exception):
        def __init__(self, message="Could not find value in env"):
            super().__init__(message)
            self.message = message
            
        def __repr__(self) -> str:
            return f"StoreError({self.message!r})"
            
        def __str__(self):
            return f"StoreError: {self.message}"
    
    def createNewCells(self, v: Value):
        nMap = self.storeMap | {self.nCells: v}
        nStore = Store(self.nCells + 1, nMap)
        return (nStore, self.nCells)
    
    def lookupCellValue(self, j: int):
        if (j in self.storeMap.keys()):
            return self.storeMap[j]
        else:
            raise Store.StoreError(f"{j} is not a valid key in store")
        
    def assignToCell(self, j: int, v: Value):
        if (j in self.storeMap.keys()):
            nMap = self.storeMap | {self.nCells: v}
            return Store(self.nCells, nMap)
        else:
            raise Store.StoreError(f"Illegal assignment to nonexistant location {j}")
         
        