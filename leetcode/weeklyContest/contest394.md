# [contest394](https://leetcode.cn/contest/weekly-contest-394/ranking/)
![myrank](./assets/contest394_rank.png)
## t1

```java
class Solution {
    public int numberOfSpecialChars(String word) {
        int[] cnt = new int[26];
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int temp = ch - 'a';
            if (temp >= 0 && temp < 26) {
                cnt[temp] |= 1;
            } else {
                temp = ch - 'A';
                cnt[temp] |= 2;
            }
        }
        int ans = 0;
        for (int i = 0; i < cnt.length; i++) {
            ans += cnt[i] == 3 ? 1 : 0;
        }
        return ans;
    }
}

```


## t2

```java
class Solution {
    public int numberOfSpecialChars(String word) {
        int[] lowerLastCnt = new int[26];
        Arrays.fill(lowerLastCnt, -1);
        int[] upperFirstCnt = new int[26];
        Arrays.fill(upperFirstCnt, -1);
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int temp = ch - 'a';
            if (temp >= 0 && temp < 26) {
                lowerLastCnt[temp] = i;
            }
            temp = ch - 'A';
            if (temp >= 0 && temp < 26 && upperFirstCnt[temp] == -1) {
                upperFirstCnt[temp] = i;
            }
        }
        int ans = 0;
        for (int i = 0; i < lowerLastCnt.length; i++) {
            if (lowerLastCnt[i] >= 0 && upperFirstCnt[i] >= 0 && upperFirstCnt[i] > lowerLastCnt[i]) ans++;
        }
        return ans;
    }
}

```

## t3

```java
class Solution {
    public int minimumOperations(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int max = n * m + 10;
        int[][] dp = new int[2][10];
        for (int i = 0; i < m; i++) {
            int[] nowChangeCnt = getChangeCnt(grid, i);
            int before = (i + 1) & 1;
            int now = i & 1;
            for (int j = 0; j < 10; j++) {
                dp[now][j] = max;
                for (int k = 0; k < 10; k++) {
                    if (j == k) continue;
                    dp[now][j] = Math.min(dp[before][k], dp[now][j]);
                }
                dp[now][j] += nowChangeCnt[j];
            }
        }
        
        return Arrays.stream(dp[(m - 1) &  1]).min().getAsInt();
    }
    
    private int[] getChangeCnt(int[][] grid, int ind) {
        int[] ans = new int[10];
        int[] cnt = new int[10];
        for (int i = 0; i < grid.length; i++) {
            cnt[grid[i][ind]]++;
        }
        for (int i = 0; i < cnt.length; i++) {
            ans[i] = grid.length - cnt[i];
        }
        return ans;
    }
}


```

## t4
```java

```