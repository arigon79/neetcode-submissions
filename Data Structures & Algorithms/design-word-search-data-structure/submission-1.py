class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.childrens:
                cur.childrens[c] = TrieNode()
            cur = cur.childrens[c]
        
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.childrens.values():
                        if dfs(i + 1, child):
                            return True
                    
                    return False
                    
                else:
                    if c not in cur.childrens:
                        return False
                    cur = cur.childrens[c]
                
            return cur.isEndOfWord

        return dfs(0, self.root)
        
