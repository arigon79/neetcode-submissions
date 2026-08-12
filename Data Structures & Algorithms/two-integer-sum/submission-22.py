class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        arr = [[v, i] for i, v in enumerate(nums)]
        arr.sort()

        l, r = 0, len(arr) - 1
        while l < r:
            s = arr[l][0] + arr[r][0]
            if s == target:
                if arr[l][1] > arr[r][1]:
                    return [arr[r][1], arr[l][1]]
                else:
                    return [arr[l][1], arr[r][1]]
            elif s > target:
                r -= 1
            else:
                l += 1
        return []