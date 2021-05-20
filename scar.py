import praw
import random
import os 

print(os.getenv("Y"))


reddit = praw.Reddit(
    client_id="SJ6V9gtmz55WwA",
    client_secret="VHn6PPJt8iOGe144QHA5xQTuuYGVhw",
    user_agent="Ari.py",
)


url_list = []


hot_posts_memes = reddit.subreddit('dankmemes').hot(limit=40)





for post in hot_posts_memes:
    url_memes = post.url
    
    url_list.append(url_memes)
        # hot_posts_dank = reddit.subreddit('dankmemes').hot(limit=10)
        # for dank in hot_posts_dank:
        #     .url_dank = dank

meme = random.choice(url_list)



url_rare = []

hot_posts_rare = reddit.subreddit('rareinsults').hot(limit=40)

for post_r in hot_posts_rare:
  rare = post_r.url
  url_rare.append(rare)
  


url_c = []

hot_posts_c = reddit.subreddit('cursedcomments').hot(limit=20)

for post_c in hot_posts_c:
  curse = post_c.url
  url_c.append(curse)
  


    
