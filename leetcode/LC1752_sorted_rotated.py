class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        if nums == nums_sort:
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if nums_sort == nums[i + 1::] + nums[0:i + 1]:
                    return True
        return False
