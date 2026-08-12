class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}
        
        for i in strs:
            sorted_str = ''.join(sorted(i))

            if sorted_str not in my_hash:
                my_hash[sorted_str] = [i]
            else:
                my_hash[sorted_str].append(i)
        
        result = []
        
        for value in my_hash.values():
            result.append(value)

        return result