from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def depth_limited_search(node, depth, visited):
    if not node:
        return
    visited.append(node.val)
    if depth > 0:
        depth_limited_search(node.left, depth - 1, visited)
        depth_limited_search(node.right, depth - 1, visited)

def get_tree_height(root):
    if not root:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

def iddfs(root):
    if not root:
        return {}
    height = get_tree_height(root)
    passes = {}
    for limit in range(height):
        visited = []
        depth_limited_search(root, limit, visited)
        passes[limit] = visited
    return passes

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    print("DFS Order:  ", dfs(root))
    print("BFS Order:  ", bfs(root))
    print("\nIDDFS passes by depth limit:")
    for limit, order in iddfs(root).items():
        print(f"  Limit {limit}: {order}")