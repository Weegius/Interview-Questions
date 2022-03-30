"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

# initialize the result 
#iterate through every index of the first string
  #iterate through every single string 
    #check if every single string at index i is the same
      #check if i is inbounds 
      # if not equal return the result
# add characters common to all strings to our result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        return res