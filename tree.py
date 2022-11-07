from collections import deque
import math
import typing

class TreeNode:
    def __init__(self, val: int = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode):
    if not root:
        return
    
    stack = deque([root])
    while stack:
        while root:
            root = root.left
            stack.append(root)
        
        
        node = stack.pop()
        if node:
            print(f"Node val in inorder arrangement: {node.val}")
            root = node.right
            stack.append(root)


def level_order_traversal(root: typing.Optional[TreeNode]):
    """
       2
    3    4
  5  6  7  8
  queue = [5,6,7,8]
  res = [2,3,4,5,6,7,8]
    """
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr:
            res.append(curr.val)
            queue.extend([curr.left, curr.right])
    return res
    

def validate_bst(root: typing.Optional[TreeNode]):
    queue = deque([(root, math.inf, -math.inf)])
    while queue:
        node, max_val, min_val = queue.popleft()
        if node:
            if node.val >= max_val or node.val <= min_val:
                return False
            queue.append((node.right, max_val, node.val))
            queue.append((node.left, node.val, min_val))
    return True