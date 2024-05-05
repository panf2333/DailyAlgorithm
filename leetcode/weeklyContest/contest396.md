# [contest396](https://leetcode.cn/contest/weekly-contest-396/ranking/)
![myrank](./assets/contest396_rank.png)
## t1

```python
class Solution:
    def isValid(self, word: str) -> bool:
        vaild = {'a','e','i','o','u','A','E','I','O','U'}
        if len(word) < 3:
            return False
        vaildCnt = 0;
        letterCnt = 0;
        for ch in word:
            if ch in vaild:
                vaildCnt += 1
            elif ch.isalpha():
                letterCnt += 1
            elif ch.isdigit():
                pass
            else:
                return False
        return vaildCnt > 0 and letterCnt > 0

```


## t2

```java
class Solution {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        Map<String, Integer> map = new HashMap();
        int max = 0;
        for (int i = 0; i < word.length(); i += k) {
            String now = word.substring(i, i + k);
            int cnt = map.getOrDefault(now, 0) + 1;
            map.put(now, cnt);
            max = Math.max(max, cnt);
        }
        return word.length() / k - max;
    }
}

```

## t3

```java
class Solution {
    public int minAnagramLength(String s) {
        //1 100000 2 50000 3 33333 4 25000 ... 10 10000 100 1000
        // 1e5 / 1 + 1e5 / 2....
        int n = s.length();
        int[][] cnt = new int[n + 1][26];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 26; j++) {
                cnt[i + 1][j] = cnt[i][j];
            }
            cnt[i + 1][s.charAt(i) - 'a']++;
        }

        for (int i = 1; i <= n; i++) {
            if (n % i != 0) continue;
            int times = n / i;
            boolean vaild = true;
            for (int j = 0; j < 26 && vaild; j++) {
                if (cnt[n][j] % times != 0) {
                    vaild = false;
                }
            }
            if (!vaild) continue;
            for (int j = 2; j <= times && vaild; j++) {
                for (int k = 0; k < 26 && vaild; k++) {
                    vaild = (cnt[j * i][k] == cnt[i][k] * j);
                }
            }
            if (vaild) return i;
        }
        return n;
    }
}

```

## t4
```java

```