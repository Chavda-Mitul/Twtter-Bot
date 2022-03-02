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

for tweet in statuses:
    print(str(tweet.id) + '    ' + tweet.text)

