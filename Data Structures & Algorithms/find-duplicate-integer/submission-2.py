class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Time: O(n)
        # Space: O(1)
        while True:
            print(f"Before: slow: {slow}, fast: {fast}")
            slow = nums[slow]
            fast = nums[nums[fast]] 
            print(f"After: slow: {slow}, fast: {fast}")
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            print(f"Before: slow: {slow}, slow2: {slow2}")
            slow = nums[slow]
            slow2 = nums[slow2]
            print(f"After: slow: {slow}, slow2: {slow2}")
            if slow == slow2:
                return slow
        
        
        
