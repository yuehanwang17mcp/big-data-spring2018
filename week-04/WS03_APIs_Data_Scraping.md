# Workshop 3: APIs and Data Scraping: Getting Twitter Data

Code is adapted from Bhaskar Karambelkar's excellent [blog post](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)\

## Set up a Twitter Application

This week we are going to use the `tweepy` library to scrape data from the Twitter REST API and make some plots! To access data through the Twitter API, you need keys associated with an App linked to your Twitter account. Your uniquer API keys should be kept secret!

There are a couple of ways to get Twitter data; the REST API is just one of them. The others are to set up a Streamer (which streams real time tweets), or to access the Firehose (this means everything!). If you're curious, you can read [this article](https://brightplanet.com/2013/06/twitter-firehose-vs-twitter-api-whats-the-difference-and-why-should-you-care/) to compare these methods.

Follow these steps to get your keys:

+ Create a Twitter account if you do not already have one.
+ Go to [Twitter Application Management](https://apps.twitter.com/) and log in with your Twitter credentials.
+ Click "Create New App" in the upper right corner.
+ Fill out the form. Give it a name like 'data_getter_yourname' and a description. The form will ask for a website---good thing we made one of these a few week ago! Use your GitHub Pages site as the URL. Leave the Callback URL field blank. Agree to the terms and click "Create your Twitter application".
+ In the next page, click on the "Keys and Access Tokens" tab, and copy your "Consumer Key (API Key)" and "Consumer Key (API Secret)".

## Create a Python script to store your Twitter keys

We need to create a Python file (`.py`) that will contain our Twitter keys. Open your text editor, and in the materials for the week, paste these keys into a new file called `twitter-keys.py`. You need to define two string variables, one for each key. Your code should look like this:

```python
# In the file you should define two variables (these must be strings!)
api_key = "your twitter key"
api_secret = "your twitter secret"
```

Using this method, we can then import the keys from a separate Python script; we can also specify that this file should not make its way to Github using a `.gitignore` file.

## Create a `.gitignore` file

You've hopefully picked up on the fact that it's **never** a good idea to include these keys in a publicly accessible script or webpage, including GitHub. One way to keep them private is importing the keys as a variable from a separate, untracked file. We can make sure to avoid accidentally pushing the file (say, with a lazy `git add .`) by including it in a `.gitignore` file.

Create a new file in the root directory of your forked repo. Save this file as `.gitignore`. Add the following lines to this file:

```sh
week-04/**/twitter_keys.py
```

Terminal bonus: if you want to do all of this in one step (create a `.gitignore` file to which you add a line), you can do so using the `echo` command as follows:

```sh
echo "week-04/**/twitter_keys.py" > .gitignore
```

This is telling git that it should ignore changes to files called `twitter_keys.py` in any subdirectory of the week-04 directory. We're safe! This file will go untracked by GitHub and we can be sure that we won't accidentally push it to our public GitHub repo.

## Importing Libraries and Twitter Keys

We will be using `tweepy`, a Python library that provides wrappers around Twitter's API. Like other Python packages we've used up until this point, we can install `tweepy` from the command line using `pip`.

```sh
# pip install twython
pip install tweepy
```

Create a new python script file (maybe `twitter_scrape.py`) and load the following libraries, including `tweepy`:

```python
# Import libraries
import json
import jsonpickle
import tweepy
from datetime import datetime
```

In addition to using `import` to load Python libraries, we also can use it to import variables from local `.py` scripts. This is very useful here---we can import the `api_key` and `api_secret` variables from our untracked `twitter_keys.py` file.

```python
# Imports the keys from the python file
from twitter_keys import api_key, api_secret

# Our keys are now stored as global variables.
print(api_key)
print(api_secret)
```

## Authenticate and create your `tweepy` object

We now need to construct `tweepy` objects that will store authentication credentials and call the API. We'll do this using the Application Only Auth method (`tweepy.AppAuthHandler()`).

Many scripts and tutorials you'll find on Github and elsewhere use the Access Token Authentication method (`tweepy.OAuthHandler()`). Without getting TOO into the weeds, OAuth performs user authentication, while AppAuth performs app authentication. The first allows you to perform account-related tasks through the API (posting statuses, etc.), while the second allows you to make more requests---this means more Tweets for us. Because it allows us to gather more Tweets, we are going to use `AppAuthHandler()`.

We first create a `tweepy` `AppAuthHandler` instance and pass it our API keys. We then pass this instance to a Tweepy API object which simplifies the process of accessing the [API endpoints](https://dev.twitter.com/overview/documentation).

```python
# Create an instance of the tweepy AppAuthHandler object
# Set this up using your Twitter Keys, imported from twitter_keys.py
auth = tweepy.AppAuthHandler(api_key, api_secret)

# Pass our authentication handler to the API object
# wait_on_rate_limit is a helpful tweepy feature that will automate the process of waiting when we've hit the Twitter API's rate limits.
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Print error and exit if there is an authentication error
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
```

After running the above code, you will have access to the Twitter API via our `api` tweey object. For reference, check out the [`tweepy` documentation](http://docs.tweepy.org/en/v3.5.0/api.html).

## Query the Twitter API to get Tweets at a Location

Now that we've authenticated and stored an API object, let's use it to perform a search and get some tweets! We will do this by constructing two functions: the first will repeatedly submit a query to Twitter's [search API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets), which will return a JSON-formatted list of Tweets. The second will parse these Tweets for storage in a Python dictionary object. This is a fairly representative workflow, regardless of what API you're working with; you'll need to query the API and parse the results of the query.

The Twitter API has rate limits that constrain how quickly we can download data. This is to try to lighten the load on their servers (and, of course, to encourage you to pay them for a premium service). We are using the Search API with Application Authentication; this will limit us to 450 requests in 15 minutes, with each request returning a maximum of 100 Tweets, yielding a theoretical maximum of 45,000 per 15 minute window. Read about the [Rate Limits](https://developer.twitter.com/en/docs/basics/rate-limits.html) here. If you exceed this limit, Twitter might lock you out.

First, we're going to define a number of global variables that we will pass to our search function, allowing us to search for specific words in specific locations.

```python
search_term = '' # leave blank to query by location
lat_lng = '42.359416,-71.093993' # Eric's office (ish)
distance = '1mi' # specify search distance
geocode_query = lat_lng + ',' + distance
```

These should be fairly intuitive; the `latlng` pair is concatenated with `distance`, separated by a comma, because this is the format specified by the `tweepy` reference.

```python
# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
# sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
# max_id = -1

def get_tweets(geo, search_term = '', tweet_per_query = 100, tweet_max = 150, since_id = None, max_id = -1):
    tweet_count = 0
    all_tweets = {}
    while tweet_count < tweet_max:
        try:
            if (max_id <= 0):
                if (not since_id):
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo)
                else:
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, since_id = since_id)
            else:
                if (not since_id):
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, max_id = str(max_id - 1))
                else:
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, max_id = str(max_id - 1), since_id = since_id)
            if (not new_tweets):
                print("No more tweets found")
                break
            for tweet in new_tweets:
                all_tweets[tweet.id_str] = parse_tweet(tweet)
            max_id = new_tweets[-1].id
            tweet_count += len(new_tweets)
        except tweepy.TweepError as e:
          # Just exit if any error
          print("Error : " + str(e))
          break
    print (f"Downloaded {tweet_count} tweets.")
    return all_tweets
```

## Parse the Tweets and return a Python Dictionary

Let's define a second function to parse the JSON

The returned object is a Python `dict` that we can easily parse into another dictionary to later store as a JSON.

```python
def parse_tweet(tweet):
    properties = {}
    if tweet.coordinates != None:
        properties['lat'] = tweet.coordinates['coordinates'][0]
        properties['lon'] = tweet.coordinates['coordinates'][1]
    else:
        properties['lat'] = None
        properties['lon'] = None
    properties['location'] = tweet.user.location
    properties['id'] = tweet.id_str
    properties['content'] = tweet.text
    properties['user'] = tweet.user.screen_name
    properties['user_id'] = tweet.user.id_str
    properties['raw_source'] = str(tweet)
    properties['time'] = str(tweet.created_at)
    return properties
```

## Run the `get_tweets` function

We're now ready to

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
