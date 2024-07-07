# [contest405](https://leetcode.cn/contest/weekly-contest-405/ranking/)
![myrank](./assets/contest405_rank.jpg)
## t1

```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            ans += (s[(i + k) % n])
        return ans
```


## t2

```python
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def dfs(s: str):
            if len(s) == n:
                ans.append(s)
                return
            dfs(s+'1')
            if s[-1] == '1':
                dfs(s+'0')
        dfs('0')
        dfs('1')
        return ans
```

## t3

```python
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = [[[0, 0] for i in range(m + 1)] for i in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                memo[i + 1][j + 1][0] = memo[i + 1][j][0] + memo[i][j + 1][0] - memo[i][j][0]
                memo[i + 1][j + 1][1] = memo[i + 1][j][1] + memo[i][j + 1][1] - memo[i][j][1]
                if grid[i][j] == 'X':
                    memo[i + 1][j + 1][0] += 1
                elif grid[i][j] == 'Y':
                    memo[i + 1][j + 1][1] += 1
                if memo[i + 1][j + 1][0] >= 1 and memo[i + 1][j + 1][0] == memo[i + 1][j + 1][1]:
                    ans += 1
                    
        # print(memo)
        return ans

```

## t4
```python
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = Trie()
        for i in range(len(words)):
            trie.insert(words[i], costs[i])
        
        heap = []
        dp = [0] + [inf] * len(target)
        for node in trie.search(target):
            heap.append(node.depth - 1)
            dp[node.depth] = node.cost
        heapq.heapify(heap)
        while len(heap) > 0:
            now = heapq.heappop(heap)
            if now == len(target) - 1:
                break
            for node in trie.search(target[now + 1:]):
                nodeind = now + node.depth
                if dp[nodeind + 1] == inf:
                    heapq.heappush(heap, nodeind)
                dp[nodeind + 1] = min(dp[now + 1] + node.cost, dp[nodeind + 1])
        return dp[len(target)] if dp[len(target)] != inf else -1
        
            
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.cost = -1
        self.depth = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, cost):
        current_node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
        current_node.depth = len(word)
        current_node.cost = cost if current_node.cost == -1 else min(current_node.cost, cost)

    def search(self, word) -> list[TrieNode]:
        current_node = self.root
        nodes = []
        for char in word:
            if char not in current_node.children:
                return nodes
            current_node = current_node.children[char]
            if current_node.is_end_of_word:
                nodes.append(current_node)
        return nodes


```