import tweepy

consumer_key = 'GeMrovno2LIPb9iZo1pY2qpeT'
consumer_secret = 'rEJsCzR4HXx4z0Y0Lk1bGl0xtPBYVXHDrfvFoAxmwPDFC7yjVs'
access_token = '1462026884124917760-cqEHC7rYhgGaylJ76zmZtWGaDLjYS0'
access_token_secret = '66Y8OGwp3za6OFqqinTRy7wgKjTYK6HGy386QR9JiRicj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# api.update_status('Tweeter bot reporting live test 1') #this will tweet the given tweet.


statuses = api.home_timeline()
# print(statuses)
# for tweet in statuses:
#     print(str(tweet.id) + '    ' + tweet.text + '   ' +tweet. )


# print(get_home_timeline())


print("_____________________________________________________________________________________")
_user = api.get_user(screen_name = "Mitul_Chavda_")
print("User details:")
print(_user.name)
print(_user.description)
print(_user.location)

print("Last 20 Followers:")
for follower in _user.followers():
    print(follower.name)
print("_____________________________________________________________________________________")


# tweet = api.get_user(screen_name="Mitul_Chavda_")
# print("Most recent tweet: " + tweet.status.text)

# api.update_profile(description="Bot that will reweet and like") # this will update the bio


# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)




# for tweet in tweepy.Cursor(api.search, q='#python', rpp=100).items(100):
#     print(f"{tweet.user.name} said: {tweet.text}")
#     pass

