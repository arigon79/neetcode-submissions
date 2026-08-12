class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]


        for num in nums:
            subset = []
            for r in res:
                subset.append(r + [num])
            
            res = res + subset
            print(res)

        return res