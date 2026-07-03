'''class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)  # {userId: [(-timestamp, tweetId)]}
        self.user_follows = defaultdict(set) # {followerId: set(followeeIds)}
    
    def postTweet(self, userId, tweetId):
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
    
    def getNewsFeed(self, userId):
        heap = []
        heap.extend(self.user_tweets[userId][-10:])
        for followeeId in self.user_follows[userId]:
            heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)

        return [tweetId for _, tweetId in heapq.nsmallest(10, heap)]
    
    def follow(self, followerId, followeeId):
        self.user_follows[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        self.user_follows[followerId].discard(followeeId)'''

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)