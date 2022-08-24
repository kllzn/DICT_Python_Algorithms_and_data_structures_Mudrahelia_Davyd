from SSD import SSD


class Node:

    def __init__(self, data: SSD):
        self.data = data    # type: SSD
        self.next = None    # type: [Node, None]

    def has_value(self, value: SSD):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
