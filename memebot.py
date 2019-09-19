from dhooks import Webhook

import os
from time import sleep

from config import HOOK

from pickles import write_pickle, load_pickle, append_pickle
from reddit import Redditbot


def run():
    hook = Webhook(HOOK)

    if not os.path.exists('old_urls.pkl'):
        write_pickle([], 'old_urls.pkl')
    while True:
        post_urls = Redditbot().get_posts('dankmemes', 10000)

        for url in post_urls:
            if url in load_pickle('old_urls.pkl'):
                pass
            else:
                hook.send(url)
                append_pickle(url, 'old_urls.pkl')
                sleep(600)


if __name__ == '__main__':
    run()
