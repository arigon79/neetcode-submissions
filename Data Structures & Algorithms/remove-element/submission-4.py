class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Time complexity: O(n)
        # Space complexity: O(1)
        i = 0
        while True:
            n = len(nums)
            if i == n:
                break
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
        