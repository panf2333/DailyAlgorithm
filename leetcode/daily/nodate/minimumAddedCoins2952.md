[problem](https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/description/?envType=daily-question&envId=2024-03-30)

We have a area [0, r) available now. Then we can enumerate the coins.  
If we add them to the area we can get a new area [coins[i], r + coins[i])

1. If r &lt; coins[i] means we need to fill the [r, coins[i]) so, we need to add some element to the array.
Beacuse of the problem is to extend the area. So the best element to be added is the 'r'.
There are two suitations:
   1. When you add x > r like: r + 1 to the array, it is same as coins[i], we can get the new [r + 1, r + r + 1).
<font color="red">***We can't get 'r' from this too. We need to add another element to get our goal.***</font>

   2. when you add x <= r, you can get [x, r + x), the x bigger the r + x bigger. <font color="red">***So we choice the x=r. if the [r, r+r)  2\*r &lt; coins[i] too, we can repeat this process.***</font>


2. if r &gt;= coins[i] we can just extend the area to [0, r + coins[i])

Finally, we might add all coins but still not get target. So we need to just extend r += r and calculate this time.




```java
// java
    public int minimumAddedCoins(int[] coins, int target) {
        Arrays.sort(coins);
        long r = 1L;
        int ans = 0;
        // 枚举coins[i] 加入 之前的范围是[0, r)
        // [coins[i], r + coins[i])
        for (int i = 0; i < coins.length && r <= target; i++) {
            while (coins[i] > r) {
                // [r, coins[i])
                // 到不了就把r加入[0+r, r+r)
                r += r;
                ans++;
            }
            //此时[0, r) 没有把coins[i]放入,放入后会更大
            r += coins[i];
        }

        while (r <= target) {
            r += r;
            ans++;
        }
        return ans;
    }

```


```python
# python
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        r = 1
        ans = 0
        coins = sorted(coins)
        for i, coin in enumerate(coins) :
            if r > target:
                break
            while r < coin:
                r += r
                ans += 1
            r += coin
        
        while r <= target:
            r += r
            ans += 1
        
        return ans
```


```typeScript
// typeScript
function minimumAddedCoins(coins: number[], target: number): number {
    let r = 1;
    let ans = 0;
    // we need to set the comparator otherwise will sort by letter order
    coins = coins.sort((a: number, b: number):number => a - b); 
    for (let i = 0; i < coins.length && r <= target; i++) {
        while (r < coins[i]) {
            r += r;
            ans++;
        }
        r += coins[i];
        
    }

    while (r <= target) {
        r += r;
        ans++;
    }

    return ans;
};
```
