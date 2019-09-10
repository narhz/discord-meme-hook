import praw

from config import CLIENT_SECRET, CLIENT_ID, USER_AGENT


class Redditbot():
    def __init__(self):
        self.reddit = praw.Reddit(client_id=CLIENT_ID,
                                  client_secret=CLIENT_SECRET,
                                  user_agent=USER_AGENT)

    def get_posts(self, sub, score_threshold):
        posts = []
        for submission in self.reddit.subreddit(sub).hot(limit=20):
            if submission.stickied:
                pass
            elif submission.score < score_threshold:
                pass
            elif submission.is_self:
                pass
            else:
                posts.append(submission.url)
        return posts


if __name__ == '__main__':
    Redditbot()
