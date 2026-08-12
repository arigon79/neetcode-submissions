class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        
        for i in nums:
            if i in my_hash:
                return True
            
            my_hash[i] = 1
        
        return False