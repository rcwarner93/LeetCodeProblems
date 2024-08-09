from typing import List

# MEDIUM
# Anagram Groups
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.
# ROBERT SOLUTION
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfSublists = []
        # THIS IMPORTANTE
        used = [False] * len(strs) 
        # Loop over each word
        for i in range(len(strs)):
            if used[i]:
                continue
            used[i] = True
            subList = [strs[i]]
            # Loop over every other word other than the one were looking at from i + 1 to end
            for j in range(i+1, len(strs)):
                # Call Helper function to determine if one word is an anagram to another
                if self.isAnagram(strs[i],strs[j]) and not used[j]:
                    subList.append(strs[j])
                    used[j] = True
            listOfSublists.append(subList)
                    
        
        
        # Return list of sublists
        # if returns true add that word as well to same sublist
        return listOfSublists
        

    def isAnagram(self, string1: str, string2: str) -> bool:
        lettersInString1 = {}
        lettersInString2 = {}
        for letter in string1:
            # countS[s[i]] = 1 + countS.get(s[i], 0)
            if letter in lettersInString1:
                lettersInString1[letter] += 1
            else: 
                lettersInString1[letter] = 1
        for letter in string2:
            if letter in lettersInString2:
                lettersInString2[letter] += 1
            else: 
                lettersInString2[letter] = 1
        return lettersInString2 == lettersInString1


# MEDIUM
# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]
# Constraints:
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
# REMU ATTEMPT
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary with counts of each integer
        # {1:1,  2:4, 3:5}
        countsdictionary = {}

        for i in range(len(nums)):
            # checks the integer,adds 1 if the integer is already there
            countsdictionary[nums[i]] = 1 + countsdictionary.get(countsdictionary[nums[i]], 0)

        # for loop for outputting the top k keys
        output = []
        integers = [] # [1,2,3]
        countintegers = [] # [1,4,5]
        for x, y in countsdictionary.items():
            # find the k greatest y's
            return
        
        #find top k countintegers
        for i in range(len(countintegers)):
            #when we get the top k, we need those indexs, then we just append those to the answers array
            return


# NEET CODE SOLUTION
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq = [[] for i in range(4)]
        # this creates
        # freq = [[], [], [], []]
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            # freq = [[1,3,4],[2]]
            

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)

# ChatGPT Answer
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # Step 1: Create a frequency dictionary
        countsdictionary = {}
        
        for num in nums:
            countsdictionary[num] = 1 + countsdictionary.get(num, 0)
        
        # Step 2: Convert the frequency dictionary to a list of tuples (frequency, element)
        freq_list = [(freq, num) for num, freq in countsdictionary.items()]
        
        # Step 3: Sort the list of tuples by frequency in descending order
        freq_list.sort(reverse=True, key=lambda x: x[0])
        
        # Step 4: Extract the top k frequent elements
        top_k = [num for freq, num in freq_list[:k]]
        
        return top_k
        

        