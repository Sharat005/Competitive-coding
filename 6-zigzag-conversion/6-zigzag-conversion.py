class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # if(len(s) > 1000 or numRows > 1000):
        #     return None
        output = [""]* (min(numRows, len(s)))
                
        down = False
        row = 0
        
        if(numRows is 1):
            return s
        
        for c in range(len(s)):
            output[row] += s[c]
            if(row == 0 or row == numRows - 1):
                down = not down
            if(down):
                row += 1
            else:
                row -= 1
                
        s1 = "".join(output)
        
        return s1
