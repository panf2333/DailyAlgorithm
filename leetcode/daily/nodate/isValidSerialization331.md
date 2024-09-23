# [331isValidSerialization](https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/?envType=daily-question&envId=2024-03-31)


<image src="https://assets.leetcode.cn/medals/2024/gif/03.gif">


> tips: 
> 1. preorder traversal is parent node -> left child tree -> right child tree
> 2. null node have to have consecutive with 2 '#'

We can use a data structure named stack to simulate the tree traversal.   

If this node isn't a null node means that it has two children. So we can put a number 0 to record it's children traversal suitation.


If this node is a leaf node, it also have 2 childern. It will have 2 consecutive '#'.

When the child tree is traversal completed, we pop this node from the stack. And if it's not the root node, We need to increase the parent node's value. This mean the node has one complete subtree.

When this node's both 2 subtrees traversal complete. The value equals 2. We need to pop this node and to increase it's parent too.

We can repeat this process, until the string is end or stack is empty.

only string is end and stack is empty, this string is vaild.

Time complex: O(n)  
> We traversal the string once.       
Space complex: O(n) 
>we use a stack to store the element. Actually the space is the deep of the tree.


```java
    // 一个叶子节点是两个连续的# 就可以返回父节点
    // 我们可以记录每一个节点是否已经遍历了左子树和右子树。通过一个cnt计数
    // 0 是都没遍历完， 1是左子树遍历了， 2是右子树遍历了。 当得到2时说明该子树已经遍历完成了
    // 我们就继续找他的节点，并将其的cnt++
    public boolean isValidSerialization(String preorder) {
        Stack<Integer> stack = new Stack();
        String[] strs = preorder.split(",");
        int i = 0;
        for (; i < strs.length; i++) {
            if (!strs[i].equals("#")) stack.push(0);
            else {
                while (!stack.isEmpty() && stack.peek() == 1) stack.pop();
                // 这个空节点# 没有对应的父节点 那就跳出看是否满足i == len - 1
                // 最后一个节点，可以把栈清空
                if (stack.isEmpty()) return i == strs.length - 1;
                // 不是1,又在里面其实只可能是0 可以直接push(1)
                stack.push(stack.pop() + 1);
            }
        }
        return false;
    }
```

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        strs = preorder.split(',')
        for i, s in enumerate(strs):
            if s != '#':
                stack.append(0)
            else:
                while len(stack) > 0 and stack[-1] == 1:
                    stack.pop()
                if len(stack) == 0:
                    return i == len(strs) - 1
                stack.pop() 
                stack.append(1)
        
        return False

```


```typeScript
function isValidSerialization(preorder: string): boolean {
    let strs: string[] = preorder.split(",");
    let stack: number[] = [];
    for (let i = 0; i < strs.length; i++) {
        if (strs[i] !== "#") {
            stack.push(0);
            continue;
        }

        while (stack.length > 0 && stack[stack.length - 1] === 1) stack.pop();

        if (stack.length === 0) return i == strs.length - 1;

        stack[stack.length - 1] = 1;
    }
    return false;
};

```