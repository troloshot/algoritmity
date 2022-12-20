class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        res = []
        while stack:
            sort = stack.pop()
            if sort.left:
                stack.append(sort.left)
                res.append((sort.left).val)
            if sort.right:
                stack.append(sort.right)
                res.append((sort.right).val)
        min_values = 10 ** 6
        res.append(root.val)
        res.sort()
        for i in range(len(res)):
            if min_values > abs(res[i - 1] - res[i]):
                min_values = abs(res[i - 1] - res[i])
        return min_values