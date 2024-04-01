# [2810 Faulty Keyboard](https://leetcode.cn/problems/faulty-keyboard/description/?envType=daily-question&envId=2024-04-01)


## Problem Explanation
It's a simple simulation problem. We just traversal this string, and if we encounter the character 'i' . let's reverse the string now exist.

As the example, the 'i' will not append any character to the new string.

In the end, we just return this string.

### Time complex:
O(n ^ 2)
We need to traversal the string each character. So it's n;

And if the character is 'i', we need to reverse the string. The string max length is n.

In the worst suitation, we need to excute n ^ 2 operate.

### Space complex:
O(n)
We just use a array to store the new string.


```java
    public String finalString(String s) {
        char[] chs = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < chs.length; i++) {
            if (chs[i] == 'i') sb.reverse();
            else sb.append(chs[i]);
        }
        return sb.toString();
    }
```

```python
    def finalString(self, s: str) -> str:
        sentence = []
        for character in s:
            if character == 'i':
                sentence = sentence[::-1]
            else:
                sentence.append(character)
        return "".join(sentence)

```

```typeScript
function finalString(s: string): string {
    let ans: string = "";
    for (let i = 0; i < s.length; i++) {
        if (s[i] == 'i') {
            let temp = "";
            for (let character of ans) {
                temp = character + temp;
            }
            ans = temp;
        }
        else ans = ans + s[i];
    }
    return ans;
};

```