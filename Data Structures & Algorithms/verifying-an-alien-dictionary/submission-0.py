class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            words1 = words[i]
            words2 = words[i + 1]

            for j in range(len(words1)):
                if j == len(words2):
                    return False
                
                if words1[j] != words2[j]:
                    if order_index[words2[j]] < order_index[words1[j]]:
                        return False
                    break
            
        return True
