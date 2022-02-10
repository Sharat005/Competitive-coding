class Solution:
    def isHappy(self, n: int) -> bool:
        
        def jump(num):
            sum = 0
            while(num > 0):
                curr = num % 10
                sum += (curr**2)
                num = num // 10
            
            return sum
        
        slow, fast = n, jump(n)
        while(slow != 1 and fast != 1):
            slow = jump(slow)
            fast = jump(jump(fast))
            if(slow == fast):
                return False
            
        return True