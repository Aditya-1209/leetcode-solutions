class Solution:
    def numberOfSteps(self, num: int) -> int:
        s = 0

        while num != 0:
            s += 1
            if num & 1:
                num -= 1
            else:
                num >>= 1
        
        return s
