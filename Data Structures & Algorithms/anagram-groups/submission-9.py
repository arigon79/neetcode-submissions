class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        # Time complexity: O(m*nlogn)
        # Space complexity: O(m*n)
        for s in strs:
            s_arr = ''.join(sorted(list(s)))
            if s_arr in tracker:
                tracker[s_arr].append(s)
            else:
                tracker[s_arr] = [s]
        
        res = []
        for vals in tracker.values():
            res.append(vals)
        
        return res
        