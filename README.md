# LeetCode
Problems and solutions.

## Table of Contents
* [Big Countries](#big-countries)
* [Binary Tree Merge](#binary-tree-merge)
* [Hamming Distance](#hamming-distance)
* [Judge Route Circle](#judge-route-circle)
* [Two Sum](#two-sum)


<a name="big-countries"></a>
## Big Countries
There is a table World:

A country is big if it has an area of bigger than 3 million (3000000) square km or a population of more than 25 million (25000000).

Write a SQL solution to output big countries' **name**, **population** and **area**.

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
## Judge Route Circle

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
