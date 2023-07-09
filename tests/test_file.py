from pprint import pprint

from status.main import TreeStore


class TestTreeStore:
    items = [
            {'id': 1, 'parent': 'root'},
            {'id': 2, 'parent': 1, 'type': 'test'},
            {'id': 3, 'parent': 1, 'type': 'test'},
            {'id': 4, 'parent': 2, 'type': 'test'},
            {'id': 5, 'parent': 2, 'type': 'test'},
            {'id': 6, 'parent': 2, 'type': 'test'},
            {'id': 7, 'parent': 4, 'type': None},
            {'id': 8, 'parent': 4, 'type': None}
    ]

    def test_getAll(self):
        expected = [
            {'id': 1, 'parent': 'root'},
            {'id': 2, 'parent': 1, 'type': 'test'},
            {'id': 3, 'parent': 1, 'type': 'test'},
            {'id': 4, 'parent': 2, 'type': 'test'},
            {'id': 5, 'parent': 2, 'type': 'test'},
            {'id': 6, 'parent': 2, 'type': 'test'},
            {'id': 7, 'parent': 4, 'type': None},
            {'id': 8, 'parent': 4, 'type': None},
        ]

        assert TreeStore(self.items).getAll() == expected

    def test_getItem(self):
        expected = {'id': 7, 'parent': 4, 'type': None}
        assert TreeStore(self.items).getItem(7) == expected

    def test_getChildren(self):
        expected = [
            {'id': 7, 'parent': 4, 'type': None},
            {'id': 8, 'parent': 4, 'type': None},
        ]
        assert TreeStore(self.items).getChildren(4) == expected
        assert TreeStore(self.items).getChildren(5) == []

    def test_getAllParents(self):
        expected = [
            {'id': 4, 'parent': 2, 'type': 'test'},
            {'id': 2, 'parent': 1, 'type': 'test'},
            {'id': 1, 'parent': 'root'},
        ]
        assert TreeStore(self.items).getAllParents(7) == expected


if __name__ == '__main__':
    items = [
        {'id': 1, 'parent': 'root'},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 3, 'parent': 1, 'type': 'test'},
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 5, 'parent': 2, 'type': 'test'},
        {'id': 6, 'parent': 2, 'type': 'test'},
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None}
    ]

    ts = TreeStore(items)
    pprint(ts.getAll())
    # [{'id': 1, 'parent': 'root'}, {'id': 2, 'parent': 1, 'type': 'test'},
    # {'id': 3, 'parent': 1, 'type': 'test'}, {'id': 4, 'parent': 2, 'type': 'test'},
    # {'id': 5, 'parent': 2, 'type': 'test'}, {'id': 6, 'parent': 2, 'type': 'test'},
    # {'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]

    print(ts.getItem(7))  # {'id': 7, 'parent': 4, 'type': None}

    print(ts.getChildren(4))
    # [{'id': 7, 'parent': 4, 'type': None},
    # {'id': 8, 'parent': 4, 'type': None}]

    print(ts.getChildren(5))  # []

    print(ts.getAllParents(7))
    # [{'id': 4, 'parent': 2, 'type': 'test'},
    # {'id': 2, 'parent': 1, 'type': 'test'},
    # {'id': 1, 'parent': 'root'}]
