# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution (object):
    def twoSum(self, nums, target): 
        for i in range(len(nums)): #定義一個迴圈依照nums的長度 若長度是4則會從0~3走遍
            for j in range(i + 1, len(nums)):#對於每個i，j將從i的下一個位置開始，到nums的最後一個位置。
                if nums[i] + nums[j] == target:#如果有碰到i位置的數字+j位置的數字 
                    return [i, j]#如果等於目標數字則return i跟j的位置
                
        return [] #如果都沒找到則回傳一個空的列表
    
nums = [2,7,11,15]
target = 9

testans = Solution()

test = testans.twoSum(nums,target)

print(test)
