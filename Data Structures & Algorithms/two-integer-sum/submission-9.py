class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        my_hash = {}

        for key, val in enumerate(nums):
            if target - val in my_hash:
                res.append(my_hash.get(target - val))
                res.append(key)
            else:
                my_hash[val] = key

        return res