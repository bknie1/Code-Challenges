# LeetCode
Problems and solutions.

#### Interview Flags:
  - *'A': Amazon*
  - *'F': Facebook*
  - *'G': Google*
  - *'L': LinkedIn*

## Table of Contents

  
* [Array Partition I](#array-partition-i)
* [Big Countries](#big-countries)
* [Binary Tree Merge](#binary-tree-merge)
* [Find the Median of Two Sorted Arrays](#median-of-two-sorted) ***- G***
* [Hamming Distance](#hamming-distance)
* [Judge Route Circle](#judge-route-circle) ***- G***
* [Two Sum](#two-sum)
* [Valid Parentheses](#valid-parentheses) ***- G***

## Google Preparation

<a name="array-partition-i"></a>
## Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

**Example 1:**
```
Input: [1,4,3,2]
Output: 4
```
**Explanation:** n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

**Note:**
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

**Personal Clarification:**
You have to capture the min value from each pair and find the min sum. Above, the minimum values are 1 from the first pair and 3 from the second pair. We don't bother considering the other two because we know there is no way their sum would be higher; especially if we consider sorting the values first.

<a name="big-countries"></a>
## Big Countries

There is a table World:

A country is big if it has an area of bigger than 3 million (3000000) square km or a population of more than 25 million (25000000).

Write a SQL solution to output big countries' **name**, **population** and **area**.

<a name="median-of-two-sorted"></a>
## Find the Median of Two Sorted Arrays ***- G***
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
```
nums1 = [1, 3]
nums2 = [2]
```
The median is 2.0

# Example 2:
```
nums1 = [1, 2]
nums2 = [3, 4]
```
The median is (2 + 3)/2 = 2.5

<a name="hamming-distance"></a>
## Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers x and y, calculate the Hamming distance.

**Example:**

Input: x = 1, y = 4
```
1   (0 0 0 1)

4   (0 1 0 0)
```
Two bits differ. Therefore, the Output/Hamming distance is 2.

<a name="binary-tree-merge"></a>
## Binary Tree Merge
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

```
Input:
[1,3,2,5]
[2,1,3,null,4,null,7]

Output:
[3,4,5,5,4,null,7]
```

<a name="judge-route-circle"></a>
## Judge Route Circle ***- G***

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

**Example 1:**
```
Input: "UD"
Output: true
```
**Example 2:**
```
Input: "LL"
Output: false
```

<a name="two-sum"></a>
## Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**

  ```python
  nums = [2, 7, 11, 15]
  target = 9
  ```
  *nums[0] + nums[1] = 2 + 7 = 9*
  ```python
  return [0, 1]
  ```

<a name="valid-parentheses"></a>
## Valid Parentheses ***- G***

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
