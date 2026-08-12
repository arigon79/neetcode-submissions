class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force
        maxSeq = -float('inf')
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                maxSeq = max(maxSeq, product)

        return maxSeq
                
        