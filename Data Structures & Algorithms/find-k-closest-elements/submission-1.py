class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0

        for r in range(len(arr)):
            if (r - l) + 1 > k:
                if abs(arr[l] - x) > abs(arr[r] - x):
                    l += 1
                else:
                    return arr[l: r]           
        return arr[l:]