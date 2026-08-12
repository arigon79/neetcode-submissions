class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        for element in nums:
            if element in my_hash:
                return True
            my_hash[element] = 1

        return False
         