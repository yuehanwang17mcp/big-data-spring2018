# Big Data And Society: Lab 2

## To-Do

+ Add section on exporting data to more familiar formats (csv,etc)

## Introduction to Pandas

`Pandas` is a library for Python for data manipulation and analysis. Pandas expands the data processing capacities of Python and adds a number of classes for easily importing data; in particular, it adds numerical tables, from various formats into their DataFrame object. A `DataFrame` is Panda’s basic object that allows multidimensional data processing and indexing. `DataFrames` can be easily and efficiently queried without the need of cumbersome syntax and convoluted loops. `DataFrames` can be merged with other data, they can be sliced, and they can be reshaped; in a way, we can think of Pandas as a big data combination of Excel and SQL.

## Resources

Pandas employs a number of functional and declarative programming idioms making it a bit different from regular Python syntax. However, it is very close to functionality to `NumPy` in that objects are treated as vectors. In this exercise, `NumPy` is generally used for math functions.

You may want to reference a [cheatsheet](https://drive.google.com/folderview?id=0ByIrJAE4KMTtaGhRcXkxNHhmY2M&usp=sharing) to ease the learning curve and learn about some of its functionality:

## Importing the library
First we need to import the libraries we'll be using for this workshop; we'll also use the `as` option to allow us to invoke the library with fewer keystrokes.

```python
import pandas as pd
import numpy as np
```

## Pandas and Data Frames

You can think of a dataframe as a manipulable, multidimensional Python array. They are based on `numpy` arrays, can hold structured data, and you can perform functions on them to manage data, such as query, select, join, group. Let's set up a really simple dataframe.

```python
# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Joey', 'Jeremy', 'Jenny']

# View dataframe
df
```

Say we want to add a column. Easy! Use the `assign` method.

```python
# Assign a new column to df called 'age' with a list of ages
df.assign(age = [28, 33, 27])
```

Data in this table can be manipulated, queried, sorted, and munged.

## Reading Files

This is cool and all... but it's the rare situation where you'd actually load data like this. You can imagine how tedious it would get after typing more than a few rows and variables (not to mention all of the windows you're leaving open for human error).

Pandas provides a number of reader functions that process files and return a pandas object or `DataFrame`. Multiple different file types can be read, like `csv`, `txt`, `xls`, and `json`. The `read_table()` function parses the tabular data contained in the files and returns a formatted and indexed `DataFrame`. A number of additional arguments can be specified, allowing us to specify the separator used in delimited text files, which column to use as an index, etc.

Additional documentation can be found on the API:
http://pandas.pydata.org/pandas-docs/stable/index.html

To start us off, lets look at a results file by precinct from the 2016 general election. This is an extract of results by precinct for Centre County, Pennsylvania.

```python
# We are reading a CSV with election data
df = pd.read_table('data/centrecounty_precinct_results_nov2016.txt', sep=',')

# We can print the first 5 rows of the df
df.head()
```

Notice we have a table! A spreadsheet! And it indexed the rows. Pandas (borrowing from R) calls it a DataFrame. Lets see the types of the columns.

`df`, in Python context, is an instance of the `pd.DataFrame` class, created by calling the `pd.read_table` function, which calls the DataFrame constructor inside of it. `df` is a dataframe object.

## DataFrame Methods

The df object, for example, has methods, or functions belonging to it, which allow it to do things. For example `df.head()` is a method that shows the first 5 rows of the dataframe. `df.dtypes` returns the data types of each of the columns.

Additional documentation can be found here: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
In general, the API is the best resource: http://pandas.pydata.org/pandas-docs/stable/api.html


```python
df.dtypes
```

The shape of the object is:

```python
df.shape
```

3526 rows times 16 columns. A spredsheet is a matrix. `df.shape` returns a tuple, so we can access members of this **tuple** like we do with a list:

```python
df.shape[0], df.shape[1]
```

```python
df.shape[0]
```

These are the column names:


```python
df.columns
```

Notice that `df.columns` returns a `Pandas.Series` object. This object is built on top of the Python **lists**, and has similar methods and attributes.

Access an individual column.


```python
df.Contest
```

We can use the unique() function to find the unique values in each column. Let's find the unique values in the Contest column

```python
df.Contest.unique()
```

Now lets get multiple columns:

```python
df_multipleColumns = df[['Contest','PrecNo', 'Count']]
df_multipleColumns.head()
```

## Querying

Pandas `DataFrames` have built-in methods for performing queries in a SQL style. They can be diced, sorted, etc it. We can apply any of this queries to parts of the `df`, and based on this query select subsets of the whole `df`. Let's do some filtering and querying.

The output of this is a series.

```python
df['PrecNo'] == 1
```

To print out the table with only the rows we want, we can apply what is called a filter. The above is a series. Let's take a look again at **Precinct 1**. We can use the `df` mask to get a filtered dataframe: we use the mask to "index" into the dataframe to get the rows we want.


```python
df_precinct1 = df[df['PrecNo'] == 1]
```

```python
df_precinct1.head()
```

We can query based on multiple conditions, by using a `&` condition. All we need to do is add `()` brackets around each condition. The query uses a boolean AND. Each condition ceates a mask of trues and falses.

```python
df[(df['PrecNo'] < 8) & (df['PrecNo'] > 5)]
```

Because this dataset contains all of the different contests in the November generals, we can use a query to pull out just the presidential election. Here we use [df.loc](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html) to select by label and find only those listings for the presidential election.


```python
df_pres = df.loc[df['Contest'] == 'PRESIDENTIAL ELECTORS']
df_pres
```

Now that we are looking just at the votes for the presidential election, we can find, for example, which rows show votes for Hillary Clinton.

```python
df_clinton = df_pres.loc[df_pres['Candidate'] == 'HILLARY CLINTON,  PRESIDENT']
df_clinton.head()
```

```python
df_pres['Candidate'].unique()
```


Since these rows are the ones that have voted for Clinton, we can perform operations to locate which rows (ie which precincts) had more than 50% of the vote go to Clinton.

This gives us a `Pandas.Series` of `True`s and `False`s. We call this a mask.


```python
df_clinton.PctCnt > 50
```

We can summarize the Count field for the rows that represent Clinton.

```python
df_clinton.Count.sum()
```

Say we want to summary for all of the candidates, lets go back to the **df_pres** table we made and group by the candidate, then sum the count.

```python
df_pres.groupby('Candidate').Count.sum()
```

We can group by with multiple columns. This will allow us to look at the results from each precinct.

```python
df_pres.groupby(['PrecNo','Candidate']).Count.sum()
```

Or directly, in Pandas, which works since `df_pres` is a pandas Series. Pandas series have a number of built-in methods like `.max()`, `.min()`, and `.mean()`!

```python
df_clinton['Count'].max()
```

You can save these as variables. And cast them to strings.

```python
# create min, max, and mean
max_clinton = df_clinton['Count'].max()
min_clinton = df_clinton['Count'].min()
mean_clinton = df_clinton['Count'].mean()

# print out some results
print("Highest precinct vote total for Clinton: " + str(max_clinton))
print("Lowest precinct vote total for Clinton: " + str(min_clinton))
print("Mean precinct vote total for Clinton: " + str(mean_clinton))
```

This isn't super useful though, so we can get the whole row of the max and min values of the percentage vote, use the following query.


```python
df_clinton.loc[df['PctCnt'] == df_clinton['PctCnt'].max()]
```

Here, Clinton took 77% of the vote!

```python
df_clinton.loc[df['PctCnt'] == df_clinton['PctCnt'].min()]
```

In this precinct, Clinton took only 17% of the votes.

#### Exercise

Calculate the minimum value, and maximum value of the `Count` column to find the precincts with the highest and lowest turnouts by percentage. Hint, you'll want to filter by `Contest`. [This](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.min.html#pandas.Series.min) documentation might be useful.


```python
# Your code here

```

#### Exercise:
Get the average actual number of people that turned out to vote by precinct across the whole dataset. [Documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.subtract.html#pandas.Series.subtract)


```python
# Your code here

```

## Cleaning

One of the most common tasks while working with big data is data cleaning. Datasets will be inherently heterogeneous and unstructured. The lack of structure can cause functions to throw errors. We can clean data sets through various methods; if the discrepancies follow a structured pattern, it is possible to use built-in functions, or write our own functions. However, if the errors cannot be structured, we might have to do it manually!

For this example, we first check the datatypes:

```python
df.dtypes
```

```python
df.shape
```

A common cause of errors is having Null or 'None' values. This usually means data was missing.


```python
df[df['PrecNo'].isnull()]
```

We had some incomplete data! We can get rid of it with the `.notnull()` function.


```python
df = df[df['PrecNo'].notnull()]
df.shape
```

We removed those 6 rows. Important note, this is working in memory! We are not actually changing the table, do to so, you can export your output to a CSV.

## Split-apply-combine (Joins!)

With Pandas we can split the data into groups based on some criteria. We can then apply a function to each group independently, and finally combine the results into a new data structure.

![Joins](http://i.imgur.com/yjNkiwL.png)

#### Group Registered Voter Data and Compare Numbers

In this next section, let's look at registered voter data, and do some grouping, joins, and comparisons.



```python
# Import the file
# Note: It's a big one! You can work with large files in Pandas with ease.
# However, you might need to set the low memory option to False.
df_voters = pd.read_table('data/CENTRE_FVE_20170123.csv', sep=',', low_memory=False)
df_voters
```

```python
# Get the row count
df_voters.shape
```

```python
# change column datatype to int for Field 27
df_voters['27'].unique()
```

Our table is 123443 rows long, by 153 columns. For a data dictionary, see the data folder. Looking at our metadata, our precinct code is held in Field 27.


```python
# Group the edges by their source
grouped = df_voters.groupby('27')
summed = grouped['27'].count()

# get a series
summed.head()
```

```python
# Convert our series to a dataframe so we can work with it further
df_summed_extract = summed.to_frame()
# df_summed_extract.index = df_summed_extract.index.map(int)
df_summed_extract.head()
```

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.rename.html


```python
# lets rename things so they make more sense
df_summed_extract.columns = ['Count']
df_summed_extract.index.names = ['Precinct']
df_summed_extract
```

Next, lets perform a join. We are going to compare the number of registered voters in the voter registration dataset to the same number in the results dataset. Let's join this table we just made from the voter registration dataset to the results dataset, based on precinct number.

How might we do this?


```python
# Query out the necessary rows
df_resultsRegVoters = df.loc[df['Contest'] == 'REGISTERED VOTERS - TOTAL']

# Create our table with headers and new index for joining
df_summed_resultsRV = df_resultsRegVoters[['PrecNo', 'Count']].astype(int).set_index('PrecNo')
df_summed_resultsRV.columns = ['Count']

# View our table
df_summed_resultsRV.head()
```


```python
# run a join!
df_compare = df_summed_extract.join(df_summed_resultsRV, lsuffix='_Extract', rsuffix='_Results')
df_compare
```


```python
df_compare['difference'] = np.subtract(df_compare['Count_Extract'], df_compare['Count_Results'])
df_compare
```

The numbers are really close, but not quite the same. Why might this be?
