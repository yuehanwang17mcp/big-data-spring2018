# step 1

# importing the libraries and tweeter keys
import matplotlib.pyplot as plt
import pandas as pd
import tweepy
import jsonpickle
import os
os.chdir('C:/Users/yueha/BigData/big-data-spring2018/week-04')
from twitter_keys import api_key, api_secret

# authenticate and create a tweepy API Object
def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api
api = auth(api_key, api_secret)

# input search terms, scraping 2000 tweets
latlng = '42.359416,-71.093993'
radius = '5mi'
geocode_query = latlng + ',' + radius
file_name = 'C:/Users/yueha/BigData/big-data-spring2018/week-04/data/ps_tweets.json'
t_max = 2000

def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets

# parse the data collected
def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

ps3_tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

# step 2

# clean locations
bos_list = ps3_tweets[ps3_tweets['location'].str.contains("Boston")]['location']
ps3_tweets['location'].replace(bos_list, 'Boston, MA', inplace = True)

bos_list2 = ps3_tweets[ps3_tweets['location'].str.contains("boston")]['location']
ps3_tweets['location'].replace(bos_list2, 'Boston, MA', inplace = True)

bos_list3 = ps3_tweets[ps3_tweets['location'].str.contains("BOSTON")]['location']
ps3_tweets['location'].replace(bos_list3, 'Boston, MA', inplace = True)

bos_list4 = ps3_tweets[ps3_tweets['location'].str.contains("BOS")]['location']
ps3_tweets['location'].replace(bos_list4, 'Boston, MA', inplace = True)

bos_list5 = ps3_tweets[ps3_tweets['location'].str.contains("Bos")]['location']
ps3_tweets['location'].replace(bos_list5, 'Boston, MA', inplace = True)

cam_list = ps3_tweets[ps3_tweets['location'].str.contains("Cambridge")]['location']
ps3_tweets['location'].replace(cam_list, 'Cambridge, MA', inplace = True)

print(ps3_tweets['location'].unique())

# clean duplicates
ps3_tweets[ps3_tweets.duplicated(subset = 'content', keep = False)]
ps3_tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)

ps3_tweets.to_csv('ps3_twitterdata.csv', sep=',', encoding='utf-8')

# group by user location
loc_tweets = ps3_tweets[ps3_tweets['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets
df_count_tweets.columns
df_count_tweets.columns = ['count']
df_count_tweets

df_count_tweets.sort_index()

# plot pie chart of user-provided locaions
colors = ["#5faf4c","#7969de","#b5b246","#697dc6",
          "#cc54bc","#4bad89","#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]
plt.pie(df_count_tweets['count'], labels=df_count_tweets.index.get_values(), shadow=False, colors=colors, radius=10)
plt.axis('equal')
plt.tight_layout()
plt.show()

# step 3

# create a scatterplot showing tweets that are geolocated
tweets_geo = ps3_tweets[ps3_tweets['lon'].notnull() & ps3_tweets['lat'].notnull()]
len(tweets_geo)
len(ps3_tweets)
plt.scatter(tweets_geo['lon'], tweets_geo['lat'], s = 25)
plt.show()

# step 4

# pick search term "flood" and collect 2000 tweets
latlng = '42.359416,-71.093993'
radius = '5mi'
geocode_query = latlng + ',' + radius
file_name = 'C:/Users/yueha/BigData/big-data-spring2018/week-04/data/ps_tweets.json'
t_max = 2000

def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets

# parse the data collected
def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

flood_tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

# step 5

# clean locations
bos_list = flood_tweets[flood_tweets['location'].str.contains("Boston")]['location']
flood_tweets['location'].replace(bos_list, 'Boston, MA', inplace = True)

bos_list2 = flood_tweets[flood_tweets['location'].str.contains("boston")]['location']
flood_tweets['location'].replace(bos_list2, 'Boston, MA', inplace = True)

bos_list3 = flood_tweets[flood_tweets['location'].str.contains("BOSTON")]['location']
flood_tweets['location'].replace(bos_list3, 'Boston, MA', inplace = True)

bos_list4 = flood_tweets[flood_tweets['location'].str.contains("BOS")]['location']
flood_tweets['location'].replace(bos_list4, 'Boston, MA', inplace = True)

bos_list5 = flood_tweets[flood_tweets['location'].str.contains("Bos")]['location']
flood_tweets['location'].replace(bos_list5, 'Boston, MA', inplace = True)

cam_list = flood_tweets[flood_tweets['location'].str.contains("Cambridge")]['location']
flood_tweets['location'].replace(cam_list, 'Cambridge, MA', inplace = True)

print(flood_tweets['location'].unique())

# clean duplicates
flood_tweets[flood_tweets.duplicated(subset = 'content', keep = False)]
flood_tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)

flood_tweets.to_csv('flood_twitterdata.csv', sep=',', encoding='utf-8')

# group by user location
loc_tweets = flood_tweets[flood_tweets['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets
df_count_tweets.columns
df_count_tweets.columns = ['count']
df_count_tweets

# step 6

# create a scatterplot showing tweets that are geolocated
flood_tweets_geo = flood_tweets[flood_tweets['lon'].notnull() & flood_tweets['lat'].notnull()]
len(flood_tweets_geo)
len(flood_tweets)
plt.scatter(flood_tweets_geo['lon'], tweets_geo['lat'], s = 25)
plt.show()

# step 7

# export scraped twitter dataset with search term "flood"
flood_tweets.to_csv('flood_twitter_data.csv', sep=',', encoding='utf-8')

# export scraped twitter dataset without search term
ps3_tweets.to_csv('ps3_twitter_data.csv', sep=',', encoding='utf-8')
