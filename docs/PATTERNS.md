# Algorithmic Patterns Cheat Sheet

A condensed map from "what does the problem look like" → "what tool to reach for".
Each entry links to a representative problem solved in this repo.

## 🪟 Sliding window

**When:** find a contiguous subarray/substring that satisfies some constraint
(max sum of size-k window, longest substring without repeats, ...).

**Idea:** maintain a window `[l, r]` and a running aggregate (sum / counter /
set). Expand on `r`, shrink on `l` while the constraint is violated.

- [643. Maximum Average Subarray I](../src/main/python/643_MaximumAverageSubarrayI/)
- [209. Minimum Size Subarray Sum](../src/main/python/209_MinimumSizeSubarraySum/)
- [424. Longest Repeating Character Replacement](../src/main/python/424_LongestRepeatingCharacterReplacement/)

## 👯 Two pointers

**When:** sorted array / palindrome / "pair sums to target" / partitioning.

**Idea:** two indices moving toward each other (or in the same direction) with
a clear invariant (`left ≤ right`, `nums[left] + nums[right] vs target`).

- [125. Valid Palindrome](../src/main/python/125_ValidPalindrome/)
- [167. Two Sum II](../src/main/python/167_TwoSum2InputArrayIsSorted/)
- [11. Container With Most Water](../src/main/python/11_ContainerWithMostWater/)
- [42. Trapping Rain Water](../src/main/python/42_TrappingRainWater/)

## 🥞 Monotonic stack

**When:** "next greater / next smaller", or expression-style problems where
order matters and you need to defer decisions.

**Idea:** push indices/values; pop while the top breaks monotonicity, doing
work on each pop.

- [739. Daily Temperatures](../src/main/python/739_DailyTemperatures/)
- [735. Asteroid Collision](../src/main/python/735_AsteroidCollision/)
- [20. Valid Parentheses](../src/main/python/20_ValidParentheses/)
- [150. Evaluate Reverse Polish Notation](../src/main/python/150_EvaluateReversePolishNotation/)

## 🗺 Hash map / set

**When:** "have I seen this before?", complement lookups, frequency counts,
deduplication.

**Idea:** trade memory for `O(1)` lookups.

- [128. Longest Consecutive Sequence](../src/main/python/128_LongestConsecutiveSequence/)
- [347. Top K Frequent Elements](../src/main/python/347_TopKFrequentElements/)
- [146. LRU Cache](../src/main/python/146_LRUCache/) (hash + doubly linked list)
- [36. Valid Sudoku](../src/main/python/36_ValidSudoku/)

## 🔍 Binary search

**When:** sorted (or monotonically-conditioned) input, "find the smallest X
such that P(X) is true".

**Idea:** invariant on `lo` and `hi`; each iteration discards half.

- [74. Search a 2D Matrix](../src/main/python/74_SearchA2DMatrix/)
- [153. Find Minimum in Rotated Sorted Array](../src/main/python/153_FindMinimumInRotatedSortedArray/)
- [374. Guess Number Higher or Lower](../src/main/python/374_GuessNumberHigherOrLower/)

## 🌲 Tree DFS / BFS

**When:** anything on a binary tree.

**Idea:** recursion that returns "what the parent needs to know"; or a queue
for level-order.

- [104. Maximum Depth of Binary Tree](../src/main/python/104_MaximumDepthOfBinaryTree/)
- [437. Path Sum III](../src/main/python/437_PathSumIII/) (DFS + prefix-sum hash)
- [1448. Count Good Nodes in Binary Tree](../src/main/python/1448_CountGoodNodesInBinaryTree/)
- [1302. Deepest Leaves Sum](../src/main/python/1302_DeepestLeavesSum/)

## 🎯 Dynamic programming

**When:** count / optimize over sequences with overlapping subproblems.

**Idea:** define the state, derive the transition, pick top-down (memo) or
bottom-up.

- [121. Best Time to Buy and Sell Stock](../src/main/python/121_BestTimeToBuyAndSellStock/)
- [53. Maximum Subarray](../src/main/python/53_MaximumSubarray/) (Kadane)
- [139. Word Break](../src/main/python/139_WordBreak/)

## 🍴 Greedy

**When:** local optimum implies global optimum. Often interval problems or
"farthest-reachable" reasoning.

- [55. Jump Game](../src/main/python/55_JumpGame/)

## 🎒 Backtracking

**When:** generate all valid configurations (combinations, permutations,
subset-sum-style enumerations).

**Idea:** recursion + "do / recurse / undo".

- [22. Generate Parentheses](../src/main/python/22_GenerateParentheses/)
- [17. Letter Combinations of a Phone Number](../src/main/python/17_LetterCombinationsOfAPhoneNumber/)

## 🔁 Linked list manipulation

**When:** in-place pointer rewiring, fast/slow pointers.

- [206. Reverse Linked List](../src/main/python/206_ReverseLinkedList/)
- [2. Add Two Numbers](../src/main/python/2_AddTwoNumbers/)
- [2130. Maximum Twin Sum of a Linked List](../src/main/python/2130_MaximumTwinSumOfALinkedList/)
