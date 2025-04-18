from typing import List
from collections import defaultdict
import heapq

class Twitter:
    TWEETS_TO_RETRIVE = 10

    def __init__(self):
        self.timestamp = 0
        # subscribers[userID] -> set of user with userID followees
        self.subscribees: defaultdict[int, set[int]] = defaultdict(set)
        # tweets[userID] -> list of tweets
        self.tweets: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.__get_heap(userId)
        heapq.heapify(heap)

        news_feed = []

        for _ in range(Twitter.TWEETS_TO_RETRIVE):
            if not heap:
                break

            _, tweet_id, followee_id, tweet_ordinal_number = heapq.heappop(heap)
            news_feed.append(tweet_id)

            if tweet_ordinal_number > 0:
                next_tweet_ordinal_number = tweet_ordinal_number - 1
                next_tweet_timestamp, next_tweet_id = self.tweets[followee_id][next_tweet_ordinal_number]
                heapq.heappush(heap, (next_tweet_timestamp, next_tweet_id, followee_id, next_tweet_ordinal_number))

        return news_feed

    def __get_heap(self, userId: int):
        # heap - list of (tweet_timestamp, tweet_id, followeeId, tweet_ordinal_number)
        heap = []
        for followeeId in self.subscribees[userId]:
            if followeeId in self.tweets:
                last_tweet_timestamp, last_tweet_id = self.tweets[followeeId][-1]
                tweet_ordinal_number = len(self.tweets[followeeId]) - 1
                heap.append((last_tweet_timestamp, last_tweet_id, followeeId, tweet_ordinal_number))

        if userId in self.tweets:
            last_tweet_timestamp, last_tweet_id = self.tweets[userId][-1]
            tweet_ordinal_number = len(self.tweets[userId]) - 1
            heap.append((last_tweet_timestamp, last_tweet_id, userId, tweet_ordinal_number))

        return heap

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscribees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.subscribees[followerId]:
            self.subscribees[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)             # User 1 posts a new tweet (id = 5).
    print(twitter.getNewsFeed(1))       # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)                # User 1 follows user 2.
    twitter.postTweet(2, 6)             # User 2 posts a new tweet (id = 6).
    print(twitter.getNewsFeed(1))       # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet
                                        # id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)              # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))       # User 1's news feed should return a list with 1 tweet id -> [5], since user
                                        # 1 is no longer following user 2.
