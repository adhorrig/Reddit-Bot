import praw
import time

r = praw.Reddit(user_agent = "Automated replies to misspellings")
print("Logging in...")
r.login("YOUR_USERNAME", "YOUR_PASSWORD", disable_warning=True)

words_to_match = ['definately', 'defiantly', 'definantly', 'definetly', 'definatley']
cache = []

def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("test")
	print("Grabbing comments...")
	comments = subreddit.get_comments(limit=35)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			print("Match found! Comment ID: " +comment.id)
			comment.reply('Did you mean to spell "definitely?"')
			print("Reply succesful!")
			cache.append(comment.id)
		print("Comments loop finished.")
			
while True:
    try:
	run_bot()
    except praw.errors.RateLimitExceeded:
        print 'Rate limit exceeded. Please wait.'
    time.sleep(10)
