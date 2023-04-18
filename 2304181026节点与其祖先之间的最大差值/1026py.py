class Solution:
    def diff(self,root,maxval,minval):
        curres=max(abs(maxval-root.val),abs(minval-root.val))
        newmaxval=max(root.val,maxval)
        newminval=min(root.val,minval)
        if root.left:
            curres=max(curres,self.diff(root.left,newmaxval,newminval))
        if root.right:
            curres=max(curres,self.diff(root.right,newmaxval,newminval))
        return curres
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.diff(root,root.val,root.val)
