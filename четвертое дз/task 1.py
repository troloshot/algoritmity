class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        counter = []
        for c1, c2 in costs:
            counter.append([c2 - c1,c1,c2])
        counter.sort()
        res = 0
        for i in range(len(counter)):
            if i < len(counter) // 2:
                res += counter[i][2]
            else:
                res += counter[i][1]
        return res