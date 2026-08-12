class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        res = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in tracker:
                tracker[sorted_str].append(s)
            else:
                tracker[sorted_str] = [s]

        for vals in tracker.values():
            res.append(vals)
        
        return res