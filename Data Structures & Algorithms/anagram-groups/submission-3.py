class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in tracker:
                tracker[sorted_str] = [s]
            else:
                tracker[sorted_str].append(s)
        
        for val in tracker.values():
            res.append(val)

        return res