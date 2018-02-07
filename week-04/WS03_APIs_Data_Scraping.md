# Workshop 3: APIs and Data Scraping: Getting Twitter Data


## Express Gratitude to https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./

## Set up a Twitter Application

This week we are going to scrape data from the Twitter API and make some plots! We are going to use the Twitter REST API, which lets us query and retrieve samples of Tweets. To do this, you need API keys that are associated with your account. Your API keys are secret and unique to you and only you, and they gives you access to Twitter data through the API.

There are a couple of ways to get Twitter data, the REST API is just one of them. The others are to set up a Streamer (which streams real time tweets), or to access the Firehose (this means everything!). Read [this article](https://brightplanet.com/2013/06/twitter-firehose-vs-twitter-api-whats-the-difference-and-why-should-you-care/) for a nice comparison between the methods.

The Twitter REST API is best place to start and what we will use in class. Follow the following steps to get your keys.

* Create a twitter account if you do not already have one.
* Go to [https://apps.twitter.com/](https://apps.twitter.com/) and log in with your twitter credentials.
* Click **"Create New App"** in the upper right corner
* Fill out the form, give it a name like `data_getter_yourname` and a description. The form will ask for a website---good thing we made one a few week ago! Use the `github.io` page you created as the URL. Leave the Callback URL field blank. Agree to the terms and click "Create your Twitter application".
* In the next page, click on **Keys and Access Tokens** tab, and copy your "Consumer Key (API Key)" and "Consumer Key (API Secret)".

## Create a Python script to store your Twitter keys

We need a Python file that will contain the Twitter keys. Open your text editor, and in the materials for the week, paste they keys you copied into a new file and save it as `twitter-keys.py`. You need to define two string variables, one for each key. Your code should look like this:

```
# In the file you should define two variables (these must be strings!)
api_key = "your twitter key"
api_secret = "your twitter secret"
```

Using this method, we can then import the keys and use them on a repeated basis, and we can choose not to put this file on Github. Again, make sure your variables store your keys as strings!

## Create a .gitignore file

Here's the thing---it's **never** a good idea to include these keys in a publicly accessible script or webpage. This means that these keys should not find their way to GitHub. One way to keep them private is importing the keys as a variable from a separate, untracked file. We can make sure to avoid accidentally pushing the file by adding its name to a `.gitignore` file.

Create a new file in the root directory of your forked repo. Save this file as .gitignore. Add the following lines to this file:

```sh
week-04/**/twitter_keys.py
```

This is telling git that it should ignore changes to files called `twitter_keys.py` in any subdirectory of the week-04 directory. We're safe! This file will go untracked by GitHub and we can be sure that we won't accidentally push it to our public GitHub repo.

## Importing the Libraries and Twitter Keys

We will be using `twython`, a Python library that provides wrappers around Twitter's API. Like other Python packages we've used up until this point, we can install `twython` from the command line using `pip`.

```sh
# pip install twython
pip install tweepy
```

Import the libraries, including `twython`:

```python
# Import libraries
import json
import time
import threading
import tweepy
from datetime import datetime
```

In addition to using `import` to load Python modules, we can use it to import variables from local `.py` scripts. We can therefore import the `api_key` and `api_secret` variables from our `twitter_keys.py` file.

```python
# Imports the keys from the python file
from twitter_keys import api_key, api_secret

# Our keys are now stored as global variables.
print(api_key)
print(api_secret)
```

## Get an OAuth2 token, and create your Twython object

We now need to et up our instance of Twython to work with your account. Doing this requires that we authenticate our Python app using our keys. Twitter uses something called [OAuth](https://dev.twitter.com/oauth) for API authentication. Twitter uses two types of OAuth authentication. OAuth1 provides user authentication to the API and is used to post tweets and issue requests on behalf of users. OAuth 2 provides [application-only authentication](https://dev.twitter.com/oauth/application-only)---it has higher rate limits but it doesn't allow you to post on users' behalf. Because it allows us to gather more Tweets, we are going to use OAuth2.

OAuth 2 requires a Third Access token you must request using the API. This next step will set everything up for us.

We first create a `Twython` object and call it `twitter`; this object simplifies the access to the [Twitter API](https://dev.twitter.com/overview/documentation), and provides methods for accessing the API’s endpoints.

```python
# Create a Twython object called twitter
# Set this up using your Twitter Keys, imported from twitter_keys.py
auth = tweepy.AppAuthHandler(api_key, api_secret)

# Get an OAuth2 access token, save as variable so we can launch our app.
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Print error and exit if there is an authentication error
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
```

For reference, the Twython documentation and all available commands can be found here. [https://twython.readthedocs.io/en/latest/usage/starting_out.html](https://twython.readthedocs.io/en/latest/usage/starting_out.html)

## Query the Twitter API to get Tweets at a Location

<!-- The first function fetches tweets with a given query at a given lat-long. We will be using the search parameters to hit the APIs endpoint. We need to provide the lat/lon of the centroid of the area we want to query, maximum number of tweets to return, and area within the centroid to search for, among others. -->

Next, let's do a search and get some tweets! Specifically, set up a function that will use the **search** API. Read more about the **search** API [here](https://dev.twitter.com/rest/reference/get/search/tweets).

The **Search API** can take many parameters for querying tweets. Twitter has a nice page of what you can use as query parameters here [https://dev.twitter.com/rest/public/search](https://dev.twitter.com/rest/public/search).

The Twitter API has rate limits that limit how quickly you can download data. This is to try to lighten the load on their servers. We are using the Search API with **OAuth2 (Application) Access** - which limits us to **450 in 15 minutes** Read about the [Rate Limits](https://dev.twitter.com/rest/public/rate-limiting) here. This means, in our following steps, always follow the guideline that you will not be able to get more than 450 tweets in 15 minutes, or Twitter might lock your access.


```python
# Input the search term you want to search on (leave blank if you want to query only by location)
search_term = ''
# Setup a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Setup a search distance
distance = '25mi'
geocode_query = latlng + ',' + distance
# Set result type (can be 'recent', 'popular', or 'mixed')
type_of_result = 'recent'
# Set number of results (up to 100, remember you can only get 450 in 15 minutes)
tweet_max = 400
tweet_per_query = 100

file_name = 'tweets.txt'

# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweet_count = 0
all_tweets = {}
print("Downloading max {0} tweets".format(tweet_max))
with open(file_name, 'w') as f:
    while tweet_count < tweet_max:
      try:
        if (max_id <= 0):
          if (not sinceId):
            new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geocode_query)
          else:
            new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geocode_query,
                                    since_id = sinceId)
        else:
          if (not sinceId):
            new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geocode_query,
                                  max_id = str(max_id - 1))
          else:
            new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geocode_query,
                                  max_id = str(max_id - 1), since_id = sinceId)
        if not new_tweets:
          print("No more tweets found")
          break
        for tweet in new_tweets:
          properties = {}
          if tweet.coordinates != None:
            properties['lat'] = tweet.coordinates[0]
            properties['lon'] = tweet.coordinates[1]
          else:
            properties['lat'] = None
            properties['lon'] = None
          properties['location'] = tweet.user.location
          properties['id'] = tweet.id_str
          properties['content'] = tweet.text
          properties['user'] = tweet.user.screen_name
          properties['user_id'] = tweet.user.id_str
          # properties['raw_source'] = tweet
          properties['time'] = str(tweet.created_at)
          all_tweets[tweet.id_str] = properties
          print(tweet)

        tweet_count += len(new_tweets)
        print("Downloaded {0} tweets".format(tweet_count))
        max_id = new_tweets[-1].id

        # Write to GeoJSON
        with open( 'data/tweets.json', 'w' ) as f:
                f.write(json.dumps(all_tweets))

      except tweepy.TweepError as e:
        # Just exit if any error
        print("Error : " + str(e))
        break

# print ("Downloaded {0} tweets, Saved to {1}".format(tweet_count, file_name))
print (f"Downloaded {tweet_count} tweets. Wrote to {file_name}.")
```

## Automate it: Hit the API and Parse the Result

We are going to create a function to help us repeatedly hit the API, and parse the result into a readable JSON that contains the things that we are interested in, and still stores the raw tweet as an additional property. The returned object is a Python `dict` that we can easily parse into another dictionary to later store as a JSON. Raw JSONs returned from the API have a specific structure.

It can be sometimes hard to read a raw JSON. It can be helpful to use online parsers like [this one]( http://jsonparseronline.com/) to look at the structure of a JSON file, and only access what we care about.

Note: Remember we are limited to 450 every 15 minutes.

```python
# Does pretty much what its long name suggests.
def get_tweets( latlong ):
    # Create a dictionary to parse the JSON
    all_tweets = {}

    # We will be hitting the API a number of times within the total time
    total_time = 10

    # Every time we hit the API we subtract time from the total
    remaining_seconds = total_time
    interval = 5

    while remaining_seconds > 0: # loop and run the function while remaining seconds is greater than zero
        added = 0

        # Hit the Twitter API using our function
        new_tweets = get_tweets_by_location(latlong) # we set latlong above!

        # Parse the resulting JSON, and save the rest of the raw content
        for tweet in new_tweets:

            tid = tweet['id']

            # Test that we have are not pulling a duplicate tweet
            if tid not in all_tweets:
                added += 1
                properties = {}
                if tweet['coordinates'] != None:
                    properties['lat'] = tweet['coordinates']['coordinates'][0]
                    properties['lon'] = tweet['coordinates']['coordinates'][1]
                else:
                    properties['lat'] = None
                    properties['lon'] = None
                properties['location'] = tweet['user']['location'] #This will get us the location associated with the profile
                properties['id'] = tid
                properties['content'] = tweet['text']
                properties['user'] = tweet['user']['id']
                properties['raw_source'] = tweet
                properties['data_point'] = 'none'
                properties['time'] = tweet['created_at']
                all_tweets[ tid ] = properties

        print(f"At {total_time - remaining_seconds} seconds, added {added} new tweets, for a total of {len(all_tweets)}")

        # We wait a few seconds and hit the API again
        time.sleep(interval)
        remaining_seconds -= interval

    print(str(len(all_tweets)) + ' Tweets retrieved.')

    # We return the final dictionary to work with in Python
    return all_tweets
```

## Run the Twitter Scraper

We need to call the functions, and save the JSONs into a folder on your local drive. Make sure that you have a folder called `week-04/data`; this is where we'll be saving all the new JSONS.

<!-- We can run the code continuously utilizing some loop, or we can use libraries like [threading](https://docs.python.org/3.6/library/threading.html). -->

```python
# This function executes the the functions over a given period of time
def execute_scrapers():
    # This is the number of times the code will be executed. In this case, just once.
    starting = 1
    while starting > 0:
        # Sometimes the API returns some errors, killing the whole script, so we setup try/except to make sure it keeps running
        try:
            t = get_tweets( latlong )
            # We name every file with the current time
            timestr = time.strftime('%Y%m%d-%H%M%S')
            # We write a new JSON into the target path
            with open(f'data/{timestr}tweets.json', 'w') as f:
                f.write(json.dumps(t))
            # we can use a library like threading to execute the run function continuously.
            threading.Timer(10, get_tweets, args = latlng).start()
            starting -= 1
        except:
            pass

execute_scrapers()
```

## Let's Explore the Data we Saved to our Machine

Let's look through the JSON we created and check out some of the data we just downloaded. First, let's import a couple of additional libraries that will let us interact with our file system, use numpy and pandas, and create plots:

```python
# Import some additional libraries that will allow us to plot and interact with the operating system
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

Next, let's explore our data a bit. This following function will allow us to perform a visual examination of what we downloaded from Twitter. Once we have collected some data, we can parse it, and visualize some of the results. Since some of the data is repeated, we can initialize some lists to check whether or not a tweet already exists, and add it to the list. We can then extract the useful information for our purposes, and store it in another list.

Building on last week, we can do this in Pandas.


```python
# Get the file names from a given directory
file_dir = "data" # Set this to where your JSON saved

# Get only the JSONs we have saved
onlyfiles = [ f for f in listdir(file_dir) if isfile(join(file_dir,f)) and not f.startswith('.')]

# create an empty dataframe with columns for each property
df_tweets = pd.DataFrame(columns = ['tweet_id', 'lat', 'lon', 'content','location','user','raw_source','data_point','time'])

# Loop through all the files
for file in onlyfiles:
    full_dir = join(file_dir,file)
    with open(full_dir) as json_data:
        dict = json.load(json_data) # creates a Python dictionary of our json
        if not isinstance(dict, list):
            for key, val in dict.items():
                df_tweets.loc[key,val] = val

df_tweets
```

## Summarize, Group, and Plot the Dataset

Next let's summarize and group our data, and create some plots.

**A** - First, group by the user location. This is not lat/lon, but rather the information the individual has input on their profile.

When you give people the power to input their own location, you get an assortment of 'creative' responses!

```python
df_tweets.dtypes
```

```python
df_tweets['location'].unique()
```

Now let's do some grouping and sorting. We are using Pandas to do our analysis, much like last week.


```python
grouped_tweets = df_tweets.groupby('location')
count_tweets = grouped_tweets['location'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets.columns = ['Count']
df_count_tweets.index.names = ['Location']
df_count_tweets.sort_index()
```

Let's create a pie chart of these using matplotlib.

```python
# Create a list of colors (from iWantHue)
colors = ["#697dc6","#5faf4c","#7969de","#b5b246",
          "#cc54bc","#4bad89","#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]

# Create a pie chart
plt.pie( df_count_tweets['Count'], labels=df_count_tweets.index.get_values(), shadow=False, colors=colors)

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()
```

There are quite a few duplicates that we can clearly see, you will likely want to clean this data to rectify this.

**B** - Next, let's find how many actually have a location and put them on a scatterplot. To do this, we need to find first the rows where lat and long are not None, and then create the plot from just that subset of the data. Let's give it a go.


```python
# Create a filter from df_tweets filtering only those that have values for lat and lon
df_tweets_with_location = df_tweets[df_tweets.lon.notnull() & df_tweets.lat.notnull()]
df_tweets_with_location
```


```python
# Use a scatter plot to make a quick visualization of the data points
# NOTE: WHEN I DID THIS, I ONLY HAD SIX OUT OF ABOUT 100 TWEETS!
plt.scatter(df_tweets_with_location['lon'],df_tweets_with_location['lat'], s=25)
plt.show()
```

## Clean the Data

**Clean the Locations** - You saw above that we had a bunch of locations that were very similar. Here, we could use [replace](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html). For example, we could replace all the variations of **York, PA** with a singular string using something like the following:


```python
# List of variations of York
variations_of_york = ['York, PA','York PA','York, Pennsylvania','York, Pa','41 W Market Street York, Pa','york P.a. ','York, Pa.']

df_tweets['location'].replace(variations_of_york, 'York, PA')
```

**Remove Duplicates** - Make sure that we don't get tweets plotted more than once. How would you make sure to only plot unique tweets? We can maybe use [drop_duplicates](http://chrisalbon.com/python/pandas_delete_duplicates.html)

## Exporting your Data to CSV

Exporting your dataset is easy, you can use **to_csv()**. This [Stack Exchange](http://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file) page will help you.


```python
df_tweets.to_csv('twitter_data.csv', sep=',', encoding='utf-8')
```

### Problem Set 3 - Extend What You Have Learned

Now that you know how to scrape data from Twitter, let's extend the exercise a little so you can show us what you know. This time you will set up the scraper to get data around MIT and scrape data for 20 minutes. Then you will visualize it with  and visualize. Think about what you would need to change to do that.

Once you have the new JSON file of Boston tweets you should a pie chart and scatterplot of your collected tweets. When you are creating your dataset, you should get at least two different attributes returned by the Twitter API (we got many of them above, so base it off of that example). Atleast one of them should be the tweet id. Make sure you remove and duplicate tweets (if any). Expanding on the above, then save the data to a CSV.

Make sure you get your own Twitter Key.

#### Deliverables

**1** - Using the Twitter REST API, collect Tweets from Boston for 30 min. Note how you set the time in the above example (in the **run_all()** function), it was in seconds. How would you do that here?

**2** - Create a Pie Chart showing a summary of tweets by user location. Please clean up the data so that multiple variations of the same location name are replaced with one variation.

**3** - Create a Scatterplot showing all of the tweets that had a latitude and longitude.

**4** - Pick a search term, such as *Trump* or *#Trump* and collect 15 minutes of tweets on it. Use the same lat/lon for Boston as you used above.

**5** - Export the entirety of your scraped Twitter datasets (one with a search term, one without) to two CSV files. We will be checking this CSV file for duplicates. So clean your file.  

### What to Give Us on Stellar

1 - Create a new Jupyter notebook that contains your scraper code. You can copy much of this one, but customize it. Submit the new Jupyter notebook, which includes your pie chart and scatterplot.

2 - Your final CSV files.
