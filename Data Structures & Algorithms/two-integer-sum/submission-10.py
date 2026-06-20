# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == target - nums[j]:
#                     return [i,j]

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        seen = {} # value -> index ; seen = {10:0}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], index]
            seen[val] = index
