from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)      # user -> set of followees
        self.tweetMap = defaultdict(list)      # user -> list of [time, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.followMap[userId].add(userId)

        maxHeap = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (-time, tweetId, followeeId, index - 1))

        while maxHeap and len(res) < 10:
            negTime, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                time, nextTweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (-time, nextTweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)