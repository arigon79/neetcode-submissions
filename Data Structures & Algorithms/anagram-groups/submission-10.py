class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = {}
        # Time: O(n* nlogn)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sublist:
                sublist[sorted_s].append(s)
            else:
                sublist[sorted_s] = [s]
        res = []
        for sub in sublist.values():
            res.append(sub)
        return res
