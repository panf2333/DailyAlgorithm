from collections import defaultdict
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: list[list[int]]) -> list[int]:
        memo = defaultdict(list)
        n = len(grid)
        m = len(grid[0])

        for i, row in enumerate(grid):
            num: int = 0
            base: int = 1
            for val in row:
                if val == 1:
                    num |= base
                base <<= 1
            memo[num].append(i)
        
        if (len(memo[0]) > 0):
            return sorted(memo[0])
        uplimit = (1 << m) - 1
        print(uplimit)
        print(memo)
        for i in range(1, 1 << m):
            if len(memo[i]) == 0:
                continue
            target = uplimit ^ i
            sub = target
            while sub:
                # 处理 sub 的逻辑
                if len(memo[sub]) == 0:
                    sub = (sub - 1) & target
                    continue
                # ans = [memo[i][0], memo[sub][0]]
                # ans.sort()
                # return ans
                return sorted([memo[i][0], memo[sub][0]])
        return []
            
# 1001

a = Solution()
# grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
# grid = [[0,0],[1,1],[1,0],[1,0]]
grid = [[0,0,0,1],[0,1,1,0]]
print(a.goodSubsetofBinaryMatrix(grid))
