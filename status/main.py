class TreeStore:

    def getAll(self) -> list:
        pass

    def getItem(self, item_id, default=None) -> dict:
        pass

    def getChildren(self, parent_id) -> list:
        pass

    def getAllParents(self, item_id) -> list:
        pass
