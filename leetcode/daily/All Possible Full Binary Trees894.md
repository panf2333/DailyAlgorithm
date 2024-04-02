# [894 All Possible Full Binary Trees](https://leetcode.cn/problems/all-possible-full-binary-trees/description/?envType=daily-question&envId=2024-04-02)


## Problem Explanation
We assume the label is from 1 to n.
A full binary tree must have odd node. Because 1 partent node match with 0 or 2 children nodes.
1 root + 2 child. The child can be this child's parent.So 1 + num(left) + num(right) = odd + odd + odd = odd

If the n mode 2 equals 0, we just return the empty list.

If the n is 1, we just return the root node.

Then we enumerate the n with i, this left subtree has i - 1 nodes, the right subtree has n - i nodes.

We process this issue recursively. And use an array to record the result to avoid the duplicate calculation.

We can get allPossibleFBTs(left) list and  allPossibleFBTs(right) list.

Then we should to combine them to the tree. And add them to the result. This has len(left subtree) * len(right subtree) kinds of situations. 


### Time complex:
~~O(n^2)~~   
~~In the allPossibleFBT function we enumerate state times. The state is less than or equals n.
Because of we record the result. So the state number is n. The most call times is n; 
The outermost layer is O(n^2).
Then we need to construct the tree. Each left subtree can combine with the right subtree.~~

The tree number times.


### Space complex:
O(n)
All the ansList is the part of result. So we can ingore them. We recursive n layer. So is O(n);

```java
    List<TreeNode>[] memo;
    int n;
    // 设编号为1...n
    // 枚举[2, n - 1] 为根节点， 因为1为根节点的话就没有左孩子，就不是完全二叉树，n同理       O(n)
    // 一个函数入参是区间返回的是子树的可能性列表。
    // 如果节点只有一个那么就是该节点为叶子节点不可能有其他结果
    // 如果子树有偶数个节点有就不可能存在返回空列表
        // 1 个父节点， 0个2个孩子节点，一开始是一个根节点。  1+1*2... 第二层中的任意个有2个节点才会有后续 1+1*2+[1,2]*2...+[1,k]*2 必然是奇数
    // 然后两个循环分别构造左子树情况 * 右子树情况 的节点并返回 
    public List<TreeNode> allPossibleFBT(int n) {
        List<TreeNode> ans = new LinkedList();
        if (n % 2 == 0) return ans;
        
        if (n == 1) {
            ans.add(new TreeNode(0));
            return ans;
        }
        this.n = n;
        memo = new LinkedList[n + 5];

        return allPossibleFBTs(n);
    }

    private List<TreeNode> allPossibleFBTs(int state) {
        if (memo[state] != null) {
            return memo[state];
        }
        List<TreeNode> ansList = new LinkedList();
        if (state == 1) {
            ansList.add(new TreeNode(0));
            return memo[state] = ansList;
        }

        for (int i = 2; i < state; i++) {
            if ((i - 1) % 2 == 0) continue;
            List<TreeNode> leftTrees = allPossibleFBTs(i - 1);
            List<TreeNode> rightTrees = allPossibleFBTs(state - i);
            for (TreeNode left : leftTrees) {
                for (TreeNode right : rightTrees) {
                    TreeNode root = new TreeNode(0);
                    root.left = left;
                    root.right = right;
                    ansList.add(root);
                }
            }
        }
        return memo[state] = ansList;
    }
```