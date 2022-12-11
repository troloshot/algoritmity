class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        stack = [root]
        res = []
        while len(stack) > 0:
            values = []
            res1 = []
            for score in stack:
                if score:
                    values.append(score.val)
                if score.left:
                    res1.append(score.left)
                if score.right:
                    res1.append(score.right)

            if len(values) > 0:
                res.append(sum(values) * 1.0 / len(values))
            res = res1

        return res
