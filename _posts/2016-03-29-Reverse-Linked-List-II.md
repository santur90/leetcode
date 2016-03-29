---
layout: post
title: Reverse Linked List II 
category: Python
tag: [leetcode]
---
解题思路：

就我目前学习到的，有用指向指针的指针的，有插入，有逆转的。但是所有方法的核心，都其实是一个算法，就是利用3个指针修改区间内的节点的next值，且要保证已修改的链表是可以被找到的，即可以连入原链表中。

假设有一个链表有1,2,3,4,5,6，6个节点。m=2，n=5。

我们添加一个dummy节点，方便操作第一个节点。

![sha](http://images.cnitblog.com/i/546654/201404/072244468407048.jpg)
首先让pre指向第m个节点前面那个，cur指向第m个节点，p1指向m的下一个节点，因为p1有可能是NULL，所以当p1不是NULL的时候，p2指向p1的下一个节点。

上图画出了这几个指针指向情况的开始状态和我们希望的终止状态。

在最终状态下，再通过其中方框中的两步就可以我们需要的链表了。

 

而cur，p1，p2三个指针在区间内向前移动并且将p1的next指向cur的过程则包含在一个for循环内部。如下：
![](http://images.cnitblog.com/i/546654/201404/072249466684683.jpg)

```python
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next
        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next
```



