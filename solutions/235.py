# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentBest = root

        # Binary search p and q to check whether they exist, and return True if they are both in 
        # node's subtree
        def bothAreDescendants(node):
            for shouldBeInSubtree in (p, q):
                cursor = node
                while cursor is not shouldBeInSubtree:
                    if cursor is None:
                        return False
                    elif cursor.val > shouldBeInSubtree.val:
                        cursor = cursor.left
                    elif cursor.val < shouldBeInSubtree.val:
                        cursor = cursor.right
            return True

        # Built a depth-first-traversal array of the contents of the tree using a queue
        allNodes = []
        queue = [root]
        while queue:
            allNodes.append(current := queue.pop())
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Iterate from the bottom level to try to find the lowest node that contains both p 
        # and q
        for node in reversed(allNodes):
            if bothAreDescendants(node):
                return node
