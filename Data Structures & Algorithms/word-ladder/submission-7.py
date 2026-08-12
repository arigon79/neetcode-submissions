class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)  # ← replaces manual dict + if/else
        wordList.append(beginWord)           # ← removed the `if` guard (visit set handles duplicates)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)    # ← simplified, no if/else needed
        
        visit = set([beginWord])             # ← was set(beginWord) which iterates characters
        q = deque([beginWord])               # ← was deque(beginWord) which iterates characters
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0   