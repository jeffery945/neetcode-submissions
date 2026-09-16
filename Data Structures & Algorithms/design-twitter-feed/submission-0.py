class Twitter:

    def __init__(self):
        self.count = 0 # used for recording timestamp
        self.followMap = defaultdict(set) #follower -> followee
        self.tweetMap = defaultdict(list) #followee -> list of [count, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 #smaller means newer

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.followMap[userId].add(userId) # because returned posts should include user's tweets
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # for every followeeId that userId follow, if they are in the tweetMap
                ind = len(self.tweetMap[followeeId]) - 1 # get the last index of the tweet
                count, tweetId = self.tweetMap[followeeId][ind]
                heapq.heappush(minheap, [count, tweetId, followeeId, ind - 1]) # use count to sort which one is the newest tweet
        
        while minheap and len(res) < 10:
            count, tweetId, followeeId, ind = heapq.heappop(minheap)
            res.append(tweetId)

            if ind >= 0:
                count, tweetId = self.tweetMap[followeeId][ind]
                heapq.heappush(minheap, [count, tweetId, followeeId, ind - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
