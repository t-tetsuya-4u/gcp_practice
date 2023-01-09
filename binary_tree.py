class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_search(root_node, search_value):
    while True:
        if root_node.value == search_value:
            return True

        elif root_node.value > search_value:
            if root_node.left is not None:
                root_node = root_node.left
            else:
                return False

        elif root_node.value < search_value:
            if root_node.right is not None:
                root_node = root_node.right
            else:
                return False


# Below are some lines of code that will test the functions defined above.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, True, True, True, False, False, False
# (each on a separate line)

root_node = Node(10)
root_node.left = Node(5)
root_node.right = Node(15)
root_node.left.left = Node(3)
root_node.left.right = Node(7)
root_node.right.left = Node(12)
root_node.right.right = Node(18)

print(binary_tree_search(root_node, 18))
print(binary_tree_search(root_node, 7))
print(binary_tree_search(root_node, 15))
print(binary_tree_search(root_node, 10))
print(binary_tree_search(root_node, 1))
print(binary_tree_search(root_node, 11))
print(binary_tree_search(root_node, 21))
