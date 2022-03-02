import tweepy

auth = tweepy.OAuth1UserHandler(
   "LE7rHjXrnLHq37OOoCgrVgWsm", "vJlMBC9g40A2OQwWBJXlnPXS4F2g8UygwSuCqXzPFMiRSdxSK6", "1462026884124917760-PVpPJj0J4kI1V9brqsGBFFdAbMPEHC", "j44ajIeprpKkYKZg0AYPAxjttIrRMlI1WyitKI9F15Sfx"
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



# Get the User object for twitter...
user = api.get_user(screen_name='twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)