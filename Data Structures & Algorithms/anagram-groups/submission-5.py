class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = defaultdict(list)

        for s in strs:
            sorted_arr = ''.join(sorted(s))
            tracker[sorted_arr].append(s)

        for val in tracker.values():
            res.append(val)

        return res