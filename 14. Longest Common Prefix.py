# Longtest Common Prefix
# 
# 
# Input: A list of words (strings) 
# Output: A string of common prefixes 



      # initialize the result 
      #iterate through every index of the first string
        #iterate through every single string 
          #check if every single string at index i is the same
          #check if i is inbounds 
            # if not equal return the result
        # add characters common to all strings to our result




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

      res = ""

      for i in range(len(strs[0])):
        for s in strs:
          if i == len(s) or s[i] != strs[0][i]:
            return res
        res += strs[0][i]

      return res


