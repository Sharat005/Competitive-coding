class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        #two variables one to keep track of 0's to be changed to 1 and another to keep track of 1's to be changed to 0's
        
        flipped_zeroes = s.count('0')
        ones_to_zeroes = 0
        output = flipped_zeroes
        
        for c in s:
            if c == '0':
                flipped_zeroes -= 1
            elif c == '1':
                ones_to_zeroes += 1
            output = min(output, flipped_zeroes+ones_to_zeroes)
            
        return output
                