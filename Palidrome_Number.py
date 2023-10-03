class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
           return False

        reversed_num = 0
        temp = x

        #假設題目是121  你要先取下最後一位 你要怎做?
        while temp != 0: #只要temp 不是0則一直執行此迴圈 意義是temp不是0就代表你還有沒做完的數字
            #處理個位數 /10的餘數會抓到個位數
            digit = temp % 10 
            #重新組成一個新的數字
            reversed_num = reversed_num * 10 + digit
            #將temp的數字最後一位取代掉 因為已經處理過了!
            temp = temp // 10 
            #while 條件符合則跳出迴圈 return reversed_num ==  x 這裡是一個判斷式 如果一樣則回傳Ture反之則回傳False
 
        return reversed_num == x 
    
x = 121

testans = Solution()

test = testans.isPalindrome(x)

print(test)