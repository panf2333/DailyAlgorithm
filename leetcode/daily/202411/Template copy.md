# [3239. Minimum Number of Flips to Make Binary Grid Palindromic I](https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/)

## Problem Explanation
We iterate the row and column separately and count each row and each column flip numbers.

The number of row flips is the number of grid[i][left] != grid[i][right] (right = len(grid[i]) - 1 - left).

The number of column flips is the number of grid[left][i] != grid[right][i] (right = len(grid) - 1 - left).
### Time complex:
O(2nm)

### Space complex:

## Code

### python
```python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        cnt1 = 0
        for row in grid:
            n = len(row)
            left, right = 0, n - 1
            while left < right:
                if row[left] != row[right]:
                    cnt1 += 1
                left += 1
                right -= 1
        
        cnt2 = 0
        n = len(grid[0])
        for i in range(n):
            l, r = 0, len(grid) - 1
            while l < r:
                if grid[l][i] != grid[r][i]:
                    cnt2 += 1
                l += 1
                r -= 1
        return min(cnt1, cnt2)




```

### TypeScript
```TypeScript


```

### Go
```go
```