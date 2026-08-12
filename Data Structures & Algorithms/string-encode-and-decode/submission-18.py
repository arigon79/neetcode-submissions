class Solution:

    def encode(self, strs: List[str]) -> str:
        res  = ''

        for s in strs:
            n = str(len(s))
            res += n + '#' + s
        
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
        

            n = int(s[i: j])
            j += 1
            res.append(s[j: j + n])
            i = j + n
        
        return res
            
            

        
