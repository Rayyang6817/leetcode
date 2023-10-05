#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):

    #如果要用hash 就要用dict 不能用set來解這道題目
    #因為需要兩個值 第一個是他index的位置 再來就是要知道兩個數值是不是能跟target match
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hash_map : #7帶入會找到 9-7 = 2 會發現他在hash 所以要回傳現在的index
                return [hash_map[diff], i]
            hash_map[n] = i   #這時候會像 {2,0} 第一個是數值 第二個是index存在dict內 繼續回圏
        return None















    # hash_dict = {}  #創造一個dict來放 value : index 

    # for i, n in enumerate(nums):
    #     diff = target - n
    #     if diff in hash_dict: #這裡是找dict內的key 所以就是找value 
    #         return [hash_dict[diff], i] 
    #     hash_dict[n] = i
    # return None