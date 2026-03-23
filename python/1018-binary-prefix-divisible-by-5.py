class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for i in nums:
            x = (x << 1 | i)
            res.append(x % 5 == 0)
        return res
