# LeetCode

My LeetCode practice in Python. Started this repo back in 2020 in Java, rebooted
it in Python in 2025 — the old Java solutions are still under `src/main/java/`
if anyone's curious.

Each problem lives in its own folder under `src/main/python/`: the solution, a
short README with the link and a couple notes about how I thought about it, and
pytest tests for the ones I've cleaned up. Whenever I notice a pattern repeats
across problems I jot it down in [docs/PATTERNS.md](docs/PATTERNS.md) — that's
turned into a decent "what shape is this problem" cheatsheet for myself.

![Solved](https://img.shields.io/badge/Solved-56-blue) ![Easy](https://img.shields.io/badge/Easy-17-brightgreen) ![Medium](https://img.shields.io/badge/Medium-38-yellow) ![Hard](https://img.shields.io/badge/Hard-1-red)

| Total  | Easy | Medium | Hard |
|:------:|:----:|:------:|:----:|
| **56** |  17  |   38   |  1   |

## Solutions

### Array (6)

|    # | Title                                                                                                                                                   | Difficulty |                                  Solution                                   |
|-----:|---------------------------------------------------------------------------------------------------------------------------------------------------------|:----------:|:---------------------------------------------------------------------------:|
| 2016 | [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)                         |  🟢 Easy   |    [📁](src/main/python/2016_MaximumDifferenceBetweenIncreasingElements)    |
|   11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                                                                   | 🟡 Medium  |               [📁](src/main/python/11_ContainerWithMostWater)               |
|   16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/)                                                                                             | 🟡 Medium  |                    [📁](src/main/python/16_3SumClosest)                     |
|  128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)                                                             | 🟡 Medium  |            [📁](src/main/python/128_LongestConsecutiveSequence)             |
|  238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)                                                             | 🟡 Medium  |             [📁](src/main/python/238_ProductOfArrayExceptSelf)              |
| 1769 | [Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) | 🟡 Medium  | [📁](src/main/python/1769_MinimumNumberOfOperationsToMoveAllBallsToEachBox) |

### String (1)

|    # | Title                                                                                                         | Difficulty |                         Solution                          |
|-----:|---------------------------------------------------------------------------------------------------------------|:----------:|:---------------------------------------------------------:|
| 2138 | [Divide a String Into Groups of Size K](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/) |  🟢 Easy   | [📁](src/main/python/2138_DivideAStringIntoGroupsOfSizeK) |

### Linked List (4)

|    # | Title                                                                                                 | Difficulty |                        Solution                        |
|-----:|-------------------------------------------------------------------------------------------------------|:----------:|:------------------------------------------------------:|
|  206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                             |  🟢 Easy   |      [📁](src/main/python/206_ReverseLinkedList)       |
|    2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                     | 🟡 Medium  |         [📁](src/main/python/2_AddTwoNumbers)          |
|  146 | [LRU Cache](https://leetcode.com/problems/lru-cache/)                                                 | 🟡 Medium  |           [📁](src/main/python/146_LRUCache)           |
| 2130 | [Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) | 🟡 Medium  | [📁](src/main/python/2130_MaximumTwinSumOfALinkedList) |

### Tree (11)

|    # | Title                                                                                               | Difficulty |                       Solution                        |
|-----:|-----------------------------------------------------------------------------------------------------|:----------:|:-----------------------------------------------------:|
|  104 | [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)         |  🟢 Easy   |  [📁](src/main/python/104_MaximumDepthOfBinaryTree)   |
|  226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)                             |  🟢 Easy   |      [📁](src/main/python/226_InvertBinaryTree)       |
|  700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)     |  🟢 Easy   |  [📁](src/main/python/700_SearchInABinarySearchTree)  |
|  872 | [Leaf Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)                             |  🟢 Easy   |      [📁](src/main/python/872_LeafSimilarTrees)       |
|  938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)                                 |  🟢 Easy   |        [📁](src/main/python/938_RangeSumOfBST)        |
|  437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/)                                         | 🟡 Medium  |         [📁](src/main/python/437_PathSumIII)          |
|  654 | [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)                           | 🟡 Medium  |      [📁](src/main/python/654_MaximumBinaryTree)      |
|  701 | [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | 🟡 Medium  | [📁](src/main/python/701_InsertIntoABinarySearchTree) |
|  814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)                           | 🟡 Medium  |      [📁](src/main/python/814_BinaryTreePruning)      |
| 1302 | [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)                             | 🟡 Medium  |      [📁](src/main/python/1302_DeepestLeavesSum)      |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)   | 🟡 Medium  | [📁](src/main/python/1448_CountGoodNodesInBinaryTree) |

### Stack (10)

|    # | Title                                                                                                               | Difficulty |                            Solution                            |
|-----:|---------------------------------------------------------------------------------------------------------------------|:----------:|:--------------------------------------------------------------:|
|   20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                                               |  🟢 Easy   |           [📁](src/main/python/20_ValidParentheses)            |
|  150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)                 | 🟡 Medium  |    [📁](src/main/python/150_EvaluateReversePolishNotation)     |
|  155 | [Min Stack](https://leetcode.com/problems/min-stack/)                                                               | 🟡 Medium  |               [📁](src/main/python/155_MinStack)               |
|  394 | [Decode String](https://leetcode.com/problems/decode-string/)                                                       | 🟡 Medium  |             [📁](src/main/python/394_DecodeString)             |
|  735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)                                             | 🟡 Medium  |          [📁](src/main/python/735_AsteroidCollision)           |
|  739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)                                             | 🟡 Medium  |          [📁](src/main/python/739_DailyTemperatures)           |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)   | 🟡 Medium  | [📁](src/main/python/1381_DesignAStackWithIncrementOperation)  |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/)                                     | 🟡 Medium  |        [📁](src/main/python/1472_DesignBrowserHistory)         |
| 2375 | [Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string/) | 🟡 Medium  | [📁](src/main/python/2375_ConstructSmallestNumberFromDIString) |
| 2390 | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)                         | 🟡 Medium  |      [📁](src/main/python/2390_RemovingStarsFromAString)       |

### Hash Table (7)

|   # | Title                                                                             | Difficulty |                    Solution                    |
|----:|-----------------------------------------------------------------------------------|:----------:|:----------------------------------------------:|
|   1 | [Two Sum](https://leetcode.com/problems/two-sum/)                                 |  🟢 Easy   |         [📁](src/main/python/1_TwoSum)         |
|  13 | [Roman To Integer](https://leetcode.com/problems/roman-to-integer/)               |  🟢 Easy   |    [📁](src/main/python/13_RomanToInteger)     |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/)               |  🟢 Easy   |   [📁](src/main/python/169_MajorityElement)    |
|  12 | [Integer To Roman](https://leetcode.com/problems/integer-to-roman/)               | 🟡 Medium  |    [📁](src/main/python/12_IntegerToRoman)     |
|  36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)                       | 🟡 Medium  |      [📁](src/main/python/36_ValidSudoku)      |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/)                             | 🟡 Medium  |       [📁](src/main/python/146_LRUCache)       |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium  | [📁](src/main/python/347_TopKFrequentElements) |

### Two Pointers (5)

|   # | Title                                                                                                 | Difficulty |                      Solution                       |
|----:|-------------------------------------------------------------------------------------------------------|:----------:|:---------------------------------------------------:|
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                   |  🟢 Easy   |      [📁](src/main/python/125_ValidPalindrome)      |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)               |  🟢 Easy   |  [📁](src/main/python/643_MaximumAverageSubarrayI)  |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟡 Medium  | [📁](src/main/python/167_TwoSum2InputArrayIsSorted) |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                 | 🟡 Medium  |  [📁](src/main/python/209_MinimumSizeSubarraySum)   |
|  42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                             |  🔴 Hard   |     [📁](src/main/python/42_TrappingRainWater)      |

### Binary Search (3)

|   # | Title                                                                                                       | Difficulty |                         Solution                          |
|----:|-------------------------------------------------------------------------------------------------------------|:----------:|:---------------------------------------------------------:|
| 374 | [Guess Number Higher Or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)                 |  🟢 Easy   |    [📁](src/main/python/374_GuessNumberHigherOrLower)     |
|  74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)                                     | 🟡 Medium  |         [📁](src/main/python/74_SearchA2DMatrix)          |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium  | [📁](src/main/python/153_FindMinimumInRotatedSortedArray) |

### Dynamic Programming (4)

|   # | Title                                                                                                             | Difficulty |                            Solution                            |
|----:|-------------------------------------------------------------------------------------------------------------------|:----------:|:--------------------------------------------------------------:|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)                 |  🟢 Easy   |      [📁](src/main/python/121_BestTimeToBuyAndSellStock)       |
|  53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                               | 🟡 Medium  |            [📁](src/main/python/53_MaximumSubarray)            |
| 139 | [Word Break](https://leetcode.com/problems/word-break/)                                                           | 🟡 Medium  |              [📁](src/main/python/139_WordBreak)               |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟡 Medium  | [📁](src/main/python/424_LongestRepeatingCharacterReplacement) |

### Greedy (1)

|  # | Title                                                 | Difficulty |             Solution              |
|---:|-------------------------------------------------------|:----------:|:---------------------------------:|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 Medium  | [📁](src/main/python/55_JumpGame) |

### Backtracking (2)

|  # | Title                                                                                                         | Difficulty |                         Solution                          |
|---:|---------------------------------------------------------------------------------------------------------------|:----------:|:---------------------------------------------------------:|
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 🟡 Medium  | [📁](src/main/python/17_LetterCombinationsOfAPhoneNumber) |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                                   | 🟡 Medium  |       [📁](src/main/python/22_GenerateParentheses)        |

### Math (3)

|    # | Title                                                                                                                                     | Difficulty |                                Solution                                |
|-----:|-------------------------------------------------------------------------------------------------------------------------------------------|:----------:|:----------------------------------------------------------------------:|
| 2566 | [Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)                         |  🟢 Easy   |     [📁](src/main/python/2566_MaximumDifferenceByRemappingADigit)      |
|    7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                                                         | 🟡 Medium  |                 [📁](src/main/python/7_ReverseInteger)                 |
| 1432 | [Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) | 🟡 Medium  | [📁](src/main/python/1432_MaxDifferenceYouCanGetFromChangingAnInteger) |
