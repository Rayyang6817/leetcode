class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        #哈希的特性是唯一性 在python中set/dict都有唯一性的特性
        #下列方式很簡單 就是跑迴圈讓他跑進去hash檢查是否有重複 如果有重複則回傳ture
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
        