class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = []

        for n in nums:
            if n in tracker:
                return True

            tracker.append(n)

        return False