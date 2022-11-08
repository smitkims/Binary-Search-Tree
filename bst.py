
import sys
from typing import List, Any, Tuple


class Node:
    def __init__(self, val: Any):
        self.data = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data: Any) -> bool:
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node: Node, data: Any) -> Node:
        if node is None:
            node = Node(data)
        else:
            if node.data == data:
                return node
            elif node.data < data:
                node.right = self._insert_value(node.right, data)
            else:
                node.left = self._insert_value(node.left, data)
        return node

    def find(self, key: Any) -> bool:
        return self._find_value(self.root, key)

    def _find_value(self, root: Node, key: Any) -> bool:
        if root is None:
            return False

        if root.data < key:
            return self._find_value(root.right, key)

        if root.data > key:
            return self._find_value(root.left, key)

        return True

        raise NotImplementedError("Implement your _find_value function")

    def delete(self, key: Any):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node: Node, key: Any) -> Tuple[Node, bool]:
        deleted = False
        # doesn't exist
        if node is None:
            return node, deleted

        else:
            # key is smaller
            if node.data > key:
                node.left, deleted = self._delete_value(node.left, key)

            # key is larger
            elif node.data < key:
                node.right, deleted = self._delete_value(node.right, key)

            # key is the same as the node value -- this node should be deleted
            else:
                # node has one left child
                if node.right is None:
                    temp = node.left
                    node = None
                    deleted = True
                    return temp, deleted

                # node has one right child
                elif node.left is None:
                    temp = node.right
                    node = None
                    deleted = True
                    return temp, deleted

                # node has two children
                # get the smallest in the right subtree
                temp = node.right
                while(temp.left is not None):
                    temp = temp.left

                node.data = temp.data
                node.right, deleted = self._delete_value(node.right, temp.data)
                deleted = True
                return node, deleted

        return node, deleted

    def in_order_traverse(self) -> List[Any]:
        return self._in_order_traverse(self.root)

    def _in_order_traverse(self, node: Node) -> List[Any]:
        result = []
        if node:
            result = self._in_order_traverse(node.left)
            result.append(node.data)
            result = result + self._in_order_traverse(node.right)
        return result


# For debugging purposes
if __name__ == '__main__':
    sys.stdout = sys.__stdout__
    array = [20, 30, 40, 70, 50, 80, 14, 18, 90, 46]

    bst = BinarySearchTree()

    # Insert
    for x in array:
        bst.insert(x)

    # Find
    print(bst.find(20))  # True
    print(bst.find(21))  # False

    # Delete
    print(bst.delete(50))  # True
    print(bst.delete(40))  # True
    print(bst.delete(19))  # False

    print(bst.in_order_traverse())  # [14, 18, 20, 30, 46, 70, 80, 90]
