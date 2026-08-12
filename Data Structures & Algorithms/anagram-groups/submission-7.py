class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            tracker[sorted_str].append(s)
            
        for key in tracker.values():
            res.append(key)

        return res