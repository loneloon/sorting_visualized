import random


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        output = []

        if self.left:
            output.append(self.left)

        output.append(self.value)

        if self.right:
            output.append(self.right)

        return output.__str__()


class Tree:
    def __init__(self, array):
        self.root = None

        for i in array:
            self.root = self.insert(self.root, i)

    def insert(self, root, value):
        temp = root

        if temp is None:
            temp = Node(value)
        elif value >= temp.value:
            temp.right = self.insert(temp.right, value)
        elif value < temp.value:
            temp.left = self.insert(temp.left, value)

        return temp


min_length = 30
max_length = 30
max_val = 100

input_array = list(random.randint(1, max_val) for i in range(random.randint(min_length, max_length)))

print(input_array)

test_tree = Tree(input_array)
print(test_tree.root)

