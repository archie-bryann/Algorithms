# https://www.youtube.com/watch?v=Sbciimd09h4
# Ways of doing depth-first search: Pre-order, In-order, Post-order
# Way of implementing: Recursion or Stacks

# Reference to Binary Search Tree (print_tree)
# This is depth-first search (recursion)

# inorder traversal
# get values in sorted order
def _print_tree(self, cur_node):
    if cur_node is not None:
        self._print_tree(cur_node.left_child)
        print(str(cur_node.value)) # inorder traversal
        self._print_tree(cur_node.right_child)

# pre-order traversal
# save tree structure
def _print_tree(self, cur_node):
    if cur_node is not None:
        print(str(cur_node.value)) # pre-order traversal
        self._print_tree(cur_node.left_child)
        self._print_tree(cur_node.right_child)

# post-order traversal
# clean-up or solve bottom-up problems like height or diameter.
# invert or reflect
def _print_tree(self, cur_node):
    if cur_node is not None:
        self._print_tree(cur_node.left_child)
        self._print_tree(cur_node.right_child)
        print(str(cur_node.value)) # post-order traversal