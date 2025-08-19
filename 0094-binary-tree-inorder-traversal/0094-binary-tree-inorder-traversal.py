# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        k=[]
        self.helper(root,k)
        return k
        


    def helper(self,root,k):
        if root is None:
            return None

        self.helper(root.left,k)
        k.append(root.val)
        self.helper(root.right,k)

        