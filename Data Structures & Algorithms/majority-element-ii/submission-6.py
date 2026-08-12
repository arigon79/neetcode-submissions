class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        count = Counter(nums)
        majority = math.floor(len(nums)/3)
        res = []
        for c in count:
            if count[c] > majority:
                res.append(c)
        return res