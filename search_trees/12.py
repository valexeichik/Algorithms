import mmap 

class Node:
    def __init__(self, value=None):
        self.value = value
        self.height = -1
        self.depth = -1
        self.max_semipath = -1
        self.children = 0
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)

def set_depth(root):
    if not root:
        return

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        node.depth = depth
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

def find_leaves_and_their_parents(node, leaves):
    if not node:
        return

    stack = [(node, node.parent)]
    while stack:
        current_node, parent = stack.pop()
        if not current_node.left and not current_node.right:
            leaves.append(current_node)
            leaves.append(parent)
        if current_node.right:
            stack.append((current_node.right, current_node))  
        if current_node.left:
            stack.append((current_node.left, current_node))

def find_edges(max_semipath, min_root, root):
    left_branch = []
    right_branch = []

    if not min_root.left:
        left_branch.append(min_root)
    else:
        find_leaves_and_their_parents(min_root.left, left_branch)
    if not min_root.right:
        right_branch.append(min_root)
    else:
        find_leaves_and_their_parents(min_root.right, right_branch)

    min_sum = float('inf')
    stack1 = []
    left_leaves = []
    right_leaves = []

    for l_node in left_branch:

        if l_node.children == 0:
            if l_node.value < root.value:
                left_leaves.append(l_node)
            else:  
                right_leaves.append(l_node)
                
        for r_node in right_branch:
            l1 = l_node.depth - min_root.depth
            l2 = r_node.depth - min_root.depth

            if l_node.children != r_node.children \
                and l1 + l2 == max_semipath:
                if l_node.value + r_node.value < min_sum:
                    min_sum = l_node.value + r_node.value
                    stack1.clear()
                    stack1.append((l_node, r_node, l1, l2))
                elif l_node.value + r_node.value == min_sum:
                    stack1.append((l_node, r_node, l1, l2))
                    
    if min_root == root:
        return min_root, stack1
    
    for node in right_branch:
        if node.children == 0:
            if node.value < root.value:
                left_leaves.append(node)
            else:  
                right_leaves.append(node)
    
    stack2 = []
    if root.height == max_semipath:
        for leaf in left_leaves:
            if leaf.depth == max_semipath and root.value + leaf.value < min_sum:
                min_sum = root.value + leaf.value
                stack2.clear()
                stack2.append((leaf, root, max_semipath, 0))
            elif root.value + leaf.value == min_sum:
                stack2.append((leaf, root, max_semipath, 0))
        
        for leaf in right_leaves:
            if leaf.depth == max_semipath and root.value + leaf.value < min_sum:
                min_sum = root.value + leaf.value
                stack2.clear()
                stack2.append((root, leaf, 0, max_semipath))
            elif root.value + leaf.value == min_sum:
                stack2.append((root, leaf, 0, max_semipath))
                
    if len(stack2) != 0 and root.value < min_root.value:
        return root, stack2
    else:
        return min_root, stack1

def set_height_and_max_semipath(node, params, root):
    if not node:
        return
    else:
        set_height_and_max_semipath(node.left, params, root)
        set_height_and_max_semipath(node.right, params, root)
        if not node.left and not node.right:
            node.height = node.max_semipath = 0
        elif not node.right:
            node.height = node.max_semipath = 1 + node.left.height
            node.children =  1 + node.left.children
        elif not node.left:
            node.height = node.max_semipath = 1 + node.right.height
            node.children =  1 + node.right.children
        else:
            node.height = 1 + max(node.right.height, node.left.height)
            node.max_semipath = 1 + node.left.height + node.right.height
            node.children = 2 + node.left.children + node.right.children

        if node.max_semipath >= params[0]:
            if node.max_semipath > params[0] \
                or ((node.max_semipath == params[0] and (not params[1] or node.value < params[1].value)) and (node != root \
                    or (node == root and node.right and node.left))):
                params[1] = node
            params[0] = node.max_semipath 
        
def define_median(tetra, min_root, max_semipath):
    left_edge, right_edge, l1, l2 = tetra

    if l1 == l2:
        return min_root.value
    
    index = max_semipath // 2
    path_array = [None] * (max_semipath + 1)
    if l1 > l2:
        start, end = 0, max_semipath - l2
        current = min_root
        while path_array[index] is None:
            if current.value > left_edge.value:
                path_array[end] = current.value
                current = current.left
                end -= 1
            else:
                path_array[start] = current.value
                current = current.right
                start += 1
    else:
        start, end = l1, max_semipath
        current = min_root
        while path_array[index] is None:
            if current.value > right_edge.value:
                path_array[end] = current.value
                current = current.left
                end -= 1
            else:
                path_array[start] = current.value
                current = current.right
                start += 1

    return path_array[index]

def find_node_to_delete(max_semipath, min_root, edges):
    median = None
    for tetra in edges:
        node_value = define_median(tetra, min_root, max_semipath)
        if median and node_value != median:
            return None
        else:
            median = node_value
    return median

def insert(root, value):
    new_node = Node(value)

    if root is None:
        root = new_node
        return

    current_node = root
    while True:
        if value == current_node.value:
            return
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
                new_node.parent = current_node
                return
            else:
                current_node = current_node.left
        else:
            if current_node.right is None:
                current_node.right = new_node
                new_node.parent = current_node
                return
            else:
                current_node = current_node.right

def delete(root, value):
    if root is None:
        return None

    current = root
    parent = None
    is_right = False

    while current is not None and value != current.value:
        parent = current
        if current.value < value:
            is_right = True
            current = current.right
        else:
            is_right = False
            current = current.left

    if current is None:
        return root

    if current.left is None and current.right is None:
        if current == root:
            root = None
        elif is_right:
            parent.right = None
        else:
            parent.left = None
    elif current.left is None:
        if current == root:
            root = current.right
        elif is_right:
            parent.right = current.right
        else:
            parent.left = current.right
        current.right.parent = parent
    elif current.right is None:
        if current == root:
            root = current.left
        elif is_right:
            parent.right = current.left
        else:
            parent.left = current.left
        current.left.parent = parent
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
            new_node.right.parent = new_node

        new_node.left = current.left
        new_node.left.parent = new_node

        if current == root:
            root = new_node
        elif is_right:
            parent.right = new_node
        else:
            parent.left = new_node
        new_node.parent = parent

    return root
            
def preorder_traversal(node, result):
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

def main():
    with open('tst.in', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            root = Node(int(mfile.readline()))
            nodes = list(map(int, mfile.read().split()))

    for node in nodes:
        insert(root, node)

    set_depth(root)

    params = [-1, None]
    set_height_and_max_semipath(root, params, root)
    max_semipath, min_root = params
    result = []
    if max_semipath % 2 == 0:
        min_root, edges = find_edges(max_semipath, min_root, root)
        node = find_node_to_delete(max_semipath, min_root, edges)
        if node:
            root = delete(root, node)

    preorder_traversal(root, result)
        
    with open('tst.out', 'w') as file:
        file.write('\n'.join(result))

if __name__ == "__main__":
    main()