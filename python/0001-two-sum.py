class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_num = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in required_num:
                return [required_num[complement], i]
            required_num[nums[i]] = i
