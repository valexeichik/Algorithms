class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def contains_node(self, value):
        return self.__contains_node(self.root, value)

    def __contains_node(self, current_node, value):
        while current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def insert(self, value):
        if value is None:
            return
        new_node = Tree.Node(value)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            parent_node = current_node
            if parent_node.value == value:
                return
            elif parent_node.value > value:
                current_node = parent_node.left
                if current_node is None:
                    parent_node.left = new_node
                    return
            else:
                current_node = parent_node.right
                if current_node is None:
                    parent_node.right = new_node
                    return

    def delete(self, value):
        if self.root is None:
            return

        current = self.root
        parent = self.root
        is_right = False

        while value != current.value:
            parent = current
            if current.value < value:
                is_right = True
                current = current.right
            else:
                is_right = False
                current = current.left

            if current is None:
                return

        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_right:
                parent.right = None
            else:
                parent.left = None
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif is_right:
                parent.right = current.right
            else:
                parent.left = current.right
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif is_right:
                parent.right = current.left
            else:
                parent.left = current.left
        else:
            new_parent = current
            new_node = current
            new_current = current.right

            while new_current is not None:
                new_parent = new_node
                new_node = new_current
                new_current = new_current.left

            if new_node != current.right:
                new_parent.left = new_node.right
                new_node.right = current.right

            new_node.left = current.left
            if current == self.root:
                self.root = new_node

            if is_right:
                parent.right = new_node
            else:
                parent.left = new_node

    def __inorder_traversal(self, node, result):
        if node is None:
            return

        node_stack = []
        current_node = node
        while current_node is not None or len(node_stack) > 0:
            while current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left
            current_node = node_stack.pop()
            result.append(str(current_node.value))
            current_node = current_node.right

    def inorder_traversal(self):
        result = []
        self.__inorder_traversal(self.root, result)
        return result

    def __preorder_traversal(self, node, result):
        if node is None:
            return

        node_stack = [node]
        while len(node_stack) > 0:
            current_node = node_stack.pop()
            result.append(str(current_node.value))

            if current_node.right is not None:
                node_stack.append(current_node.right)
            if current_node.left is not None:
                node_stack.append(current_node.left)

    def preorder_traversal(self):
        result = []
        self.__preorder_traversal(self.root, result)
        return result

    def __postorder_traversal(self, node, result):
        if node is None:
            return

        node_stack1 = []
        node_stack2 = []
        node_stack1.append(node)
        while len(node_stack1) > 0:
            current_node = node_stack1.pop()
            node_stack2.append(current_node)
            if current_node.left is not None:
                node_stack1.append(current_node.left)
            if current_node.right is not None:
                node_stack1.append(current_node.right)
        while len(node_stack2) > 0:
            result.append(str(node_stack2.pop().value))

    def postorder_traversal(self):
        result = []
        self.__postorder_traversal(self.root, result)
        return result


def main():
    with open('input.txt', 'r') as file:
        target = int(file.readline())
        nodes = list(map(int, file.read().split()))

    tree = Tree()
    for node in nodes:
        tree.insert(node)

    tree.delete(target)

    with open('output.txt', 'w') as file:
        file.write('\n'.join(tree.preorder_traversal()))


if __name__ == '__main__':
    main()