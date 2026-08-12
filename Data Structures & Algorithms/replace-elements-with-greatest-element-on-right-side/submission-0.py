class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            max_val = max(arr[i + 1:])
            arr[i] = max_val
        
        arr[-1] = -1
        return arr

        
