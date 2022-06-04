class Twitter:

    def __init__(self):
        self.does_follow = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.insert(0, (userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        print(userId, [(uid, tweedId) for uid, tweedId in self.tweets if uid == userId])
        return [tweedId for uid, tweedId in self.tweets if uid == userId or uid in self.does_follow[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.does_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.does_follow[followerId]:
            self.does_follow[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)