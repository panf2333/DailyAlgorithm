# [contest391](https://leetcode.cn/contest/weekly-contest-391/ranking/)

## t1

```java
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int temp = x;
        int sum = 0;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return x % sum == 0 ? sum : -1;
    }
```


## t2

```java
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        int emptyBottles = ans;
        while (emptyBottles >= numExchange) {
            emptyBottles -= numExchange;
            emptyBottles++;
            ans++;
            numExchange++;
        }
        return ans;
    }
```

## t3

```java
    public long countAlternatingSubarrays(int[] nums) {
        long ans = 0L;
        int left = 0;
        int right = 0;
        int len = nums.length;
        int pre = -1;
        while (right < len) {
            if (nums[right] != pre) {
                pre = nums[right];
                right++;
            }
            else {
                while (left < right) {
                    ans += right - left;
                    left++;
                }
                pre = -1;
            }
        }
        while (left < right) {
            ans += right - left;
            left++;
        }
        return ans;
    }

```