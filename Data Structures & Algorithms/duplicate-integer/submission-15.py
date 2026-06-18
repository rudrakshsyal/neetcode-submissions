# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums = sorted(nums)
#         for i in range(0, len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False




