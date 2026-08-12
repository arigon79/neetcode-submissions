class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n)
        prev = {0:1}
        curSum, res = 0, 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prev.get(diff, 0)
            prev[curSum] = 1 + prev.get(curSum, 0)
        return res

        
                

