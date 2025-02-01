class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_even = True if nums[0] % 2 == 0 else False
        for num in nums[1::]:
            if is_even and num % 2 == 0:
                return False
            elif not is_even and num % 2 == 1:
                return False
            else:
                is_even = not is_even
        return True
