
# EXTRA SUPPLEMENT | Web Scraping Using Beautiful Soup

***


### Web Scraping using Beautiful Soup

Let's scrape some data using a fun library called Beautiful Soup. We'll create a CSV dataset of the a table on 311 reported Rodent Incidents around Boston.

The website we are going to scrape is here.

[Rat Incidents in Greater Boston](http://duspviz.mit.edu/_assets/data/sample.html)

Let's get started!

#### Importing Modules

First import modules. **import requests** imports the requests module, and **import bs4** imports the Beautiful Soup library.


```python
import requests
import bs4

# If you don't have Beautiful Soup, install with 'conda install beautifulsoup'
```

#### Testing out Requests

Requests will allow us to load a webpage into python so that we can parse it and manipulate it. Test this by running the following. I am using a really simple page from the Beautiful Soup documentation to explain what is happening here. Enter the following commands in terminal, and hit enter after entering each to run each of them.


```python
response = requests.get('http://duspviz.mit.edu/_assets/data/sample.html')
print(response.text) # Print the output
```

This allowed us to access all of the content from the source code of the webpage with Python, which we can now parse and extract data. It even printed to our console. Pretty cool!

#### Testing out Beautiful Soup

Our next big step is to test out Beautiful Soup. Let's talk about what this is...

### What is Beautiful Soup?

Beautiful Soup is a Python library for parsing data out of HTML and XML files (aka webpages). It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. The major concept with Beautiful Soup is that it allows you to access elements of your page by following the CSS structures, such as grabbing all links, all headers, specific classes, or more. It is a powerful library. Once we grab elements, Python makes it easy to write the elements or relevant components of the elements into other files, such as a CSV, that can be stored in a database or opened in other software.

The sample webpage we are using contains data on 'rodent incidents' in the greater Boston area. Let's use this file to explore the tree, and extract some data.

#### iv. Make the Soup

First, we have to turn the website code into a Python object. We have already imported the Beautiful Soup library, so we can start calling some of the methods in the libary. Replace **print response.text** with the following. This turns the text into an Python object named **soup**.

An important note: You need to specify the specific parser that Beautiful Soup uses to parse your text. This is done in the second argument of the BeautifulSoup function. The default is the built in Python parser, which we can call using **html.parser**

You an also use **lxml** or **html5lib**. This is nicely described in the [documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). For our purposes, using the default is fine.

Using the Beautiful Soup **prettify()** function, we can print the page to see the code printed in a readable and legible manner.


```python
soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup.prettify()) # Print the output using the 'prettify' function
```

At any point, if you need a reference, visit the [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) for the official descriptions of functions. Prettify is a handy one to see our document in a clean fashion.

#### Navigating the Data Structure

With our data from the webpage nicely laid out, Beautiful Soup allows us to now navigate the data structure. We called our Beautiful Soup object **soup**, so we can run the Beautiful Soup functions on this object. Let's explore some ways to do this, try entering some of the following into your terminal.


```python
# Access the title element
soup.title
```


```python
# Access the content of the title element
soup.title.string
```


```python
# Access data in the first 'p' tag
soup.p
```


```python
# Access data in the first 'a' tag
soup.a
```


```python
# Retrieve all links in the document (note it returns an array)
soup.find_all('a')
```


```python
# Retrieve elements by class equal to link using the attributes argument
soup.findAll(attrs={'class' : 'link'})
```


```python
# Retrieve a specific link by ID
soup.find(id="link3")
```


```python
# Access Data in the table (note it returns an array)
soup.find_all('td')
```

#### Working with Arrays

The easiest way to access elements and then either write them to file or manipulate them is to save them as objects themselves. Note that our data is organzed into cities and numbers. Let's save these to arrays, which are the easiest way to work with the data.

The following gives us an array, we can work with the elements.


```python
data = soup.findAll(attrs={'class':'city'})
print(data[0].string)
print(data[1].string)
print(data[2].string)
print(data[3].string)
```

You never want to repeat code like this, so turn this into a loop:


```python
data = soup.findAll(attrs={'class':'city'})
for i in data:
    print(i.string)
```

This array only gives us cities though, let's get all of the data elements that have either class **city** or class **number**.


```python
data = soup.findAll(attrs={'class':['city','number']})
print(data)
```

We have all of our data that was nested in these tags saved to a Python array. Access the elements of the array by using data[x], where x is location in the array. In Python, arrays start at 0, so place 1 in a Python array is actually called by using a 0, and place 8 would be called by a 7.


```python
print(data[0])
print(data[1])
```

Right now, we get the whole element with those commands. To get just the content, use the following.


```python
print(data[0].string)
print(data[1].string)
```

In the next part, we'll create a script file and run it!

### Create and execute Script File (.py)

Open up **starter_script.py** in Sublime Text and we are going to write some code in that file. **.py** signifies that the file is a python program. Using this method, you can make independently standing python files that can be run. It is located in the scripts folder for the week. Starter script contains all the code below, and is a sample you can use for scraping pages.

For the first lines in the file, lets import modules. **import requests** imports the requests module, and **import bs4** imports the Beautiful Soup library, then, based on what we did above, load the page, turn it into a parseable 'soup', then find the proper elements. Let's put a print at the end so we can see our work as it runs.


```python
import requests
import bs4

# load and get the website
response = requests.get('http://duspviz.mit.edu/_assets/data/sample.html')

# create the soup
soup = bs4.BeautifulSoup(response.text, "html.parser")

# find all the tags with class city or number
data = soup.findAll(attrs={'class':['city','number']})

# print 'data' to console
print(data)
```

Run this by saving your file into your directory as **starter_script.py**, and then in terminal, typing **python starter_script.py**. This will execute our program.

You should see an array with our data elements nested within tags. This is what we want!

### Write data to a file using a simple loop

Python makes opening a file and writing to it very easy. Let's take this simple dataset and write it to a file that saves in our current working directory. An important note, whatever the working directory is when you start Python will be the root for where your files are read from and written to.

Python also has nice iteration features that allow us to iterate through arrays, lists, and other files. In this following example, manually create a comma-separated document with our data using file writing operations and a while loop.

In pseudo-code:

1. Open up a file to write in and append data.

2. Set up parameters for the while loop

3. Write headers

4. Run while loop that will write elements of the array to file

5. When complete, close the file

Once done, open the file on your machine and see your data. Enter the following code, note what each line is doing.


```python
f = open('rat_data.txt','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array
l = len(data)-1 # length of array minus one

f.write("City, Number\n") #write headers

while p < l: # while place is less than length
    f.write(data[p].string + ", ") # write city and add comma
    p = p + 1 # increment
    f.write(data[p].string + "\n") # write number and line break
    p = p + 1 # increment

f.close() # close file
```

Save and run the file. You'll see rat_data.txt appear where you designate.

Open **rat_data.txt** in Sublime Text. It's a CSV with the data from the page!

---

```sh
City, Number
Cambridge, 400
Boston, 900
Somerville, 300
Brookline, 600
```

---

Further reading on File Reading and Writing and Iteration in Python can be found at the following links.

[Python File Reading and Writing Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

We created this CSV manually to illustrate some basic Python. Python has modules and features that support CSV as well that are very useful and handy. These are best if you are reading in a CSV, allowing you to access the elements of the CSV. You can read more about the built in CSV module [here](https://docs.python.org/3/library/csv.html).

You've got your feet wet, over the next weeks, there will be much more to come on Python and data scraping!

***

## Additional Reading and Resources

#### Conda Command Line Cheatsheet -
http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf

#### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

#### Python Documentation -
https://docs.python.org/3/library/index.html

#### Beautiful Soup Tutorials -
http://www.crummy.com/software/BeautifulSoup/bs4/doc/
