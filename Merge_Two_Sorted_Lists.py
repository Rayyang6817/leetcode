# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp = dummy = ListNode(None)
        
        while (list1 != None) and (list2 != None):
            if list1.val < list2.val :
                #如果list1的數字比較小
                #則tmp後面接list1的第0個數字
                tmp.next = list1
                #然後指針要指向下個數字
                list1 = list1.next
            else :
                tmp.next = list2
                list2 = list2.next

            tmp = tmp.next

                #如果還有就直接接
        tmp.next = list1 or list2
        #為什麼要回傳dummy由於tmp與dummy當初指向同一個記憶體位置
        #但tmp會因為迴圈的關係一直移動所以只要dummy的下個節點就是節點的起點也就是list1or2的開頭
        return dummy.next