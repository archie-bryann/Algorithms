import sys

class Node:
    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.parent = None  # pointer to parent node in tree


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    # returns true if the value exists in the tree
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        return False

    # returns the node with the specified input value
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            _num_children = 0
            if n.left_child is not None:
                _num_children += 1
            if n.right_child is not None:
                _num_children += 1
            return _num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases base on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:
            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            # get the single child node
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with it's child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two pointers)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    # We have binary tree & binary search trees (left nodes having lesser values & right nodes having greater values)
    # Run through of test-case at bottom of page:
    # {5}, min, max
    # left children (value must be lesser than maximum)
    # {2}, min, 5
    # right children (value must be greater than min.)
    # {10}, 2, max
    # {15}, 10, max
    def validate_bst(self, root, min=-sys.maxsize, max=sys.maxsize):
        if root is None:
            return True
        if min < root.value < max and \
                self.validate_bst(root.left_child, min, root.value) and \
                self.validate_bst(root.right_child, root.value, max):
            return True
        else:
            return False


def fill_tree(_tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        _tree.insert(cur_elem)
    return _tree


tree = BinarySearchTree()
# tree = fill_tree(tree)

tree.insert(5)
tree.insert(10)
tree.insert(2)
tree.print_tree()
print(tree.search(5))


# Test case for validate_bst
root = Node(5)
l = Node(2)
r = Node(10)
rr = Node(15)

r.right_child = rr
# r.left_child = rr  # makes a binary tree
root.left_child = l
root.right_child = r

print(tree.validate_bst(root))
