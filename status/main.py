from collections import defaultdict


class TreeStore:
    def __init__(self, items) -> None:
        self.items = {item['id']: item for item in items}
        self.children = defaultdict(list)
        self.parents = {}
        for item in items:
            if (parent_id := item['parent']) is not None:
                self.children[parent_id].append(item)
            self.parents[item['id']] = parent_id

    def getAll(self) -> list:
        return list(self.items.values())

    def getItem(self, item_id) -> dict:
        return self.items.get(item_id)

    def getChildren(self, parent_id) -> list:
        return self.children.get(parent_id, [])

    def getAllParents(self, item_id) -> list:
        parent_id = self.parents.get(item_id)
        parents = []
        while parent_id is not None:
            parent = self.items.get(parent_id)
            if parent is not None:
                parents.append(parent)
                parent_id = parent['parent']
            else:
                break
        return parents
