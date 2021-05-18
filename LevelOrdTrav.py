"""Binary Tree Level Order Traversal
Time Complexity : O(N)
Space Complexity : O(H) H - height of tree = max ssize of satck.

approach -> do dfs . recursion"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # maintain a global list of levels
    def __init__(self):
        self.levels = []
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return self.levels
        #make recursive calls
        self.recursive(root,0) #initially call on root and its level 0 
        return self.levels
    
    def recursive(self,root:TreeNode,level):
        #if we encounter a new level keep adding the nodes in the level in levels list following dfs
        if len(self.levels) == level:
            self.levels.append([])
        self.levels[level].append(root.val)
        
        if root.left:
            self.recursive(root.left, level+1)
        #stack.pop() so it maintains the level when it goes to right child
        if root.right:
            self.recursive(root.right, level+1)