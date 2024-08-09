
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# class Solution:

def hasDuplicate(self, nums: List[int]) -> bool:
    
    map = set()
    for n in nums:
        if n in map:
            return True
        else:
            map.add(n)    
    return False

    
# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
def isAnagram(self, s: str, t: str) -> bool:
    #Get Count of each strings chars and compare

    #check if lengths are equal
    if len(s) != len(s):
        return False
    #check if they're both empty strings
    if (s == "") & (t == ""):
        return True

    #dictionary{t:5}
    #make dictionary_s dictionary_t
    dictionary_s = {}
    dictionary_t = {}
    #loop through s
    for letter in s:
        if dictionary_s.get(letter):
            dictionary_s[letter]+= 1
    #if letter in dictionary, add one to count
    #if letter not in dictionary, add to dictionary with count of 1
        else:
            dictionary_s[letter] = 1
    #loop through t
    for letter in t:
        if dictionary_t.get(letter):
            dictionary_t[letter] += 1
        else:
            dictionary_t[letter] = 1
    #if letter in dictionary, add one to count
    #if letter not in dictionary, add to dictionary with count of 1
    #check if dictionaries are equal
    if dictionary_s == dictionary_t:
        return True
    return False

# neetcode method
def isAnagram(self, s: str, t: str) -> bool:
    # check lengths
    if len(s) != len(t):
        return False
    
    # initialize dictionaries
    countS, countT = {}, {}

    # loop through string s
    for i in range(len(s)):
        # the letter = 1 + the value in the dictionary (0 is default)
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

    
# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
# O(N^2)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)

    return answer

# neetcode method OnePass approach O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # dictionary that will hold the value: index
    dictionary_nums = {}
    for i in range(len(nums)):
        #{0:3, 1:4, 2:5}
        # {3:0, 4:1, 5:2, ...}
        # 
        dictionary_nums[nums[i]] = i
        
    
    for i in range(len(nums)):
        # if difference is in the dictionary (7-3) = 4 (if 4 is in dictionary we good)
        if (target - nums[i]) in dictionary_nums:
            return [i, dictionary_nums[target-nums[i]]]
    return
