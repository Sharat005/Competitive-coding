class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        t = "balloon"
        wordCount = {}
        
        for c in text:
            if c in wordCount:
                wordCount[c] += 1
            else:
                wordCount[c] = 1
                
        #print(wordCount)
        
        count = 0
        i = 0
        while True:
            if t[i] in wordCount and wordCount[t[i]] > 0:
                wordCount[t[i]] -= 1
            else:
                break
            
            if i == len(t) - 1:
                i = 0
                count += 1
            i += 1
        return count      