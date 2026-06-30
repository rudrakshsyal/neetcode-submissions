class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # counter = {1:0}
        # max_count = 0

        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         counter[1] += 1
        #         max_count = max(max_count, counter[1])
        #     else:
        #         counter[1] = 0
            
        # return max_count

        index = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                index += 1
                max_count = max(max_count, index)
            else: 
                index = 0
        
        return max_count
        