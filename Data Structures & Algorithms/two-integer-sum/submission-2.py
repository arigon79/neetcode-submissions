class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(0, n):
            for j in range(i, n):
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result

        return result