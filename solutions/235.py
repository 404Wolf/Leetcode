# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentBest = root

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

        bestSoFar = root
        allNodes = []
        queue = [root]
        while queue:
            allNodes.append(current := queue.pop())
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        for node in allNodes:
            print(node.val, bothAreDescendants(node))
            if bothAreDescendants(node):
                bestSoFar = node

        return bestSoFar
