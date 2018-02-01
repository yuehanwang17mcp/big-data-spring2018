# Introduction to Python

## Starting out

### Activate your virtual environment

Recall that last week, we installed the `virtualenv` package using `pip`. Consult those directions again if, for whatever reason, you don't have `virtualenv` installed or you haven't created a `bdvs` virtual environment. To activate our virtual environment, we simply need to run a single command in Terminal or Git Bash:

```sh
. ~/.venvs/bdvs/bin/activate
```

Once you've executed this command, you should see `(bdvs)` at the front of the line in Terminal. This means that you're working in your virtual environment!

### Start Atom from the Terminal

Now that we're within our virtual environment, we need to start Atom from the command line. It's important that you follow this step! Otherwise, Atom and Hydrogen will be working with your system Python installation instead of the environment we're curating.

Change directory to your local clone of the class repo and launch Atom. This can be done like so:

```sh
cd /path/to/local/clone/big-data-spring2018
atom ./
```

When Atom launches, you should see the repo's directory tree on the left side of the screen.

<!--
First, create an environment that is running Python 3. We can name this anything, but name it **python3** so we can remember easily what it is.

```sh
	conda create --name python3 python=3.6
```

Now we want to work in this environment. Activate **python3** using the following.

```sh
	source activate python3
```

Then launch a Jupyter notebook.

```sh
	jupyter notebook
``` -->

Todays agenda:

+ What is Python?
+ Libraries
+ Datatypes
+ Data Structures
+ Collections
+ Loops
+ Flow Control

## What is Python?

[Python](https://www.python.org/) is a very, very popular high-level programming language. It emphasizes legibility over highly complex structure. Python provides simple data structures that allow for easy data manipulation. Python's simplicity and legibility has led to a large and devoted user community who have created numerous libraries that vastly extend the basic capacities of the language.

Python is an "interpreted" language. This means that every Python command that is executed is actually translated to lower-level programming languages. Lower-level, compiled programming languages (for example, C++) are very fast and powerful, but writing programs in these languages can be difficult.

There are two main versions of Python, these are Python 2 and Python 3. Python 3 is newer, and remove bugs and idiosyncrasies of Python 2; however Python 2 is still heavily used. While the fundamentals of the two versions are the same, there are some differences (mostly syntactical) between the two. These differences are substantial enough that, unfortunately, Python 3 is NOT backwards compatible, so always double check which version of Python a given script is written in. In this class, we are using Python 3.

There are a number of great Python tutorials available on the web, some can be found here:

+ [Python Docs Tutorials](https://docs.python.org/3/tutorial/)
+ [Python Docs Guide to Tutorials](http://docs.python-guide.org/en/latest/intro/learning/)
+ [Learn Python the Hard Way](https://learncodethehardway.org/python/)
+ [Learn More Python the Hard Way](https://learncodethehardway.org/more-python/)

There are also some excellent Python textbooks and cookbooks. Yes, dear reader, books are still very useful! I recommend the following:

+ Guttag, John. *Introduction to Computation and Programming Using Python*. Cambridge: MIT Press, 2017.
+ McKinney, Wes. 2017. *Python for Data Analysis*. 2nd ed. Boston: O’Reilly Media.


<!-- ## 2. Jupyter Notebooks:

![IPython](images/ipython.png "IPython")

<p>
A Jupyter Notebook (formerly called iPython) is a tool for interactively writing and executing Python code. It allows the programmer to easily write and test code by allowing snippets of code and their results to be displayed side-by-side. Each snippet of code is called a "cell". It promotes the ease of documentation by allowing some cells to contain text, html code, images, or even Latex. Jupyter is particularly useful for Big Data computation, as it allows for parallel processing.
</p>
<p>Here is some Latex:</p>
$$e^x = \int e^x dx$$
<p>Here is some HTML:</p>
<table>
    <tr>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>3</td>
        <td>4</td>
    </tr>
</table> -->

## Python Libraries

Python is a dynamically typed language. A language has dynamic typing when variable types are not predefined like in a compiled language; the type of a value is evaluated when the code is run, based on how you are attempting to use it.

Dynamic typing and a number of other language specific characteristics, like readability and reusability, make it a very popular programming language with a large user community. However, Python on itself only provides a basic number of modules and functionality. In order to extend Python’s functionality, the active community has created a very large number of libraries. A library is a built-in or external module that can be imported into our current code to add functionality. Libraries usually take advantage of Object-Oriented-Programming, defining Python objects in additional scripts that can then be instantiated in our current code.

Loading libraries into our current context can be expensive; for that reason, Python requires us to explicitly load the libraries that we want to use:

```python
import math
```

We can be more specific and import only specific classes or functions of the library:

```python
from math import pi
```

We can also change the name of the library when it gets imported. This allows you to invoke libraries using shorter names. Libraries often have conventional abbreviations; for example, you'll often see the `pandas` library (which we'll be using a lot in the class!) imported as `import pandas as pd`.

```python
import matplotlib as plt
import pandas as pd
```

```python
# Import Libraries for use later in script
import math
import matplotlib
import numpy as np

# If you get an error message stating that "No module named ... ", quit Python using quit()
# After quiting, install the missing library using pip. For example, in the terminal, to
# get matplotlib, type 'conda install matplotlib'
```

## Comments

Comments allow you to include text in you code that is not executed. This makes them exceptionally useful for documenting your code. Documenting your code becomes imperative when you share it. Other coders won't know what was going on in your brain! You probably will have a hard time remembering after a while, too so... do yourself and others a favor. It is always good practice to comment your code with future users (again, including you in two months) in mind. We can have single- or multi-line comments.

Single-line comments start with the hash character, `#` , and extend to the end of the line. A comment may appear at the start of a line or following whitespace or code.

Multiline comments are known as docstrings. They start with “”” and end with “””.

```python
# Firstly, this is a single-line comment.

"""
This is a
multiline
comment
"""

print("Comments worked!")
```

## Python Data Structures

A data structure is a way of organizing data in the computer memory. Data structures can implement one or more particular data types (ADT).  Some data structures can be built based on a basic type or basic building block. Most languages allow more complicated composite types to be recursively constructed starting from basic types.

### Variables

Variables allow us to store results, text, functions or data that we can retrieve later by invoking their name. They give our code persistence. Unlike many other programming languages, you don’t have to explicitly define a variable name or its datatype beforehand; you can create variables on the fly! Variables can also be continuously redefined. Python emphasizes legibility. You should as well! Good naming practices clearly refer to the data you are storing.

```python
# We can define variables without having to declare their type. We can name it whatever we want.
x = 4.0
print(x)
print(x*2)
# A text (or string) variable
text = "This is the text we're storing!"
print(text)
# you can change the value of x as often as you want.
x = 3
print(x)
x = x+2
print(x)
# the following retrieves the value stored in x, adds 2 to it,
# and stores the result in x.
x+=2
print(x)
x-=10
print(x)
division=5/6
print(division)
print(type(division))
```

### Numeric Types and Their Methods

Python implements four distinct numeric types: plain integers, long integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of plain integers.

Variables can be defined based on constructing a numeric data type. Every time we define a variable with a number, we are constructing an instance of the datatype. Different datatypes have different constructors; to construct a numeric data type, you only need to type it! In general, numeric types (and data types) have methods and properties. Properties allow you to access specific data of a given object, and methods allow you to do operations with them.


```python
# Integers (int) are a numerical data-type.
print(1+2)
print(type(1+2))
```

```python
# Floats are another numeric type that allows for fractions.
print(1.0+.5)
print(3.0-2.0)
print(6*5.0)
print(7.0/2)
print(type(1.0+5))
```

### Strings

Strings are sets of characters. We can create them by enclosing characters in quotes. Python treats single quotes the same as double quotes.

Strings can be thought of as lists of characters - we'll get into lists a bit more later. For now, know that we can access substrings by specifying ranges in the list or characters. They also have a number of methods or operations that we can perform with them.

```python
# A string is sequence of characters.
print("Hello World.")

# Let's store a string in a variable called "s".
# Note that using ' and " to define strings are interchangeable.
s = 'This is a string.'
print(s)

# We can access individual characters or substrings. What do you notice about the output from the second print function?
print(s[2])
print(s[2:6])

# You can add strings together
string = s + " Another string."
print(string)
string+=" A third string."
print(string)
```

### Formatting strings: `f` strings and `str.format()`

Imagine though, that you're interested in including a value stored in a variable in your string. For example, you'd like to print a message to console that includes both the result of an operation and a description of that result. Python now has an simple syntax that accomplishes exactly this, known as the f string. It looks something like this:

```python
result1 = 2.017e-3
print(f"The result of the operation is {result1}!")
result2 = 12.023e-3
print(f"The result of operation one is {result1} and the result of operation two is {result2}!")
```

This simple syntax is a new addition to Python - it only became available in Python 3.6. In prior versions, the same result can be obtained using the `str.format() `method as follows:

```python
finding1 = 17
print("We find that the value is {}!".format(finding))
finding2 = 13
print("We find that the first value is {} and the second value is {}!".format(finding1, finding2))
```

The `str.format()` method places the variables in curly brackets in the order in which they're passed to the method.


### Booleans
Booleans are binary datatypes that are used to indicate the truth or falsehood of a statement. Epistemologically, computers are incredibly simplistic. They understand two values: `True` and `False` (or 1 and 0). Despite the highly reductive computational treatment of truth they imply, Booleans are exceedingly useful.

```python
# booleans, can hold only two
# possible values: True or False.
is_true = True
print(is_true)
```

```python
# There are several operators that act on booleans, which can be thought of as constructing Venn diagrams.
# Let x and y be variables storing booleans.
# "Not x" switches the value of x. If x is True, then "not x" is False.
# "x and y" returns True if x and y are True.
# "x or y" returns True if x or y are True.
# Again: Venn diagrams.
x = True
y = False
print(x)
print(not x)
print(x and y)
print(x and not y)
print(x or y)
print(not x or y)
```

```python
# There are functions to make comparisons between valuables and produce bools.
# '==' tests for equality
print(1 == 2)
print(1 == 1)
# '!=' tests for inequality
print(1 != 2)
# comparison functions also apply to strings
print("abcd" == "abcd")
# Pointers and their values can be compared.
x = 1
y = 2
# compare values of pointers
print(x == y)
# set x and y to be the same pointer
x = y
print(x)
print(y)
# check if x and y are THE SAME using the 'is' function.
print(x is y)
```

### Lists

Lists are a data structure designed for easy storage and access to data. They are initialized using by using `[ ]` to enclose a comma separated sequence of values. These values can be anything. Lists can either contain a series of the same type of values, or a heterogeneous mix of types.  We can access individual elements of a list, a subset of elements, or the whole list. Lists are mutable: we can modify their elements.

Python deals with multiple data structures in a similar manner. For example lists, dictionaries, files, and and iterators work similarly. It's important to note that Python is 0-indexed. This means that the first element in a list is not accessed with `list[1]`. Rather, it is accessed with `list[0]`. This is the case with most programming languages, with some notable exceptions. `R` for example, is 1-indexed.

```python
L1 = [] # an empty list
x = 5
L2 = [1,2.0,'a',"abcd",True,x] # a list containing different values
# lists can be built dynamically (aka on the fly) using "append" and
# "extend".
L1.append(1)
L1.append(2)
print(L1)
L3 = ['a','b','c']
L1.extend(L3)
L1.append(L3)
print(L1)
# Whoa! What's the difference between extend and append?

# Values stored in lists are accessible by their index in the list.
# Lists maintain the ordering in which values were stored in them.
# We use "[i]" to retrieve the i-th element in a list.
# Note that the first element in a list in Python has index 0.
L = ['a','b','c','d','e']
print(L[0])
print(L[1])
# We can access from the ends of lists as well.
print(L[-1])
print(L[-2])
# We can access chunks of a list to produce sub-lists.
print(L[:2])
print(L[2:4])
#print [1,2]+['a','b']
# There is a useful function for producing sequences of numbers.
print(range(10))
print(range(2,10))
print(range(4,10,2))
# The length of a list can be calculated using "len()"
print(len(range(10)))
```

Lists can also be constructed through a functional programming idiom called list comprehension.


```python
alist=[1,2,3,4,5]
asquaredlist=[i*i for i in alist]
asquaredlist
```

### Dictionaries

Dictionaries, called "dicts" for short, allow you to store values by providing identifying keys and values. They always have key/value pairs. Dicts are initialized using `{ }`. Placing a comma-separated list of `key:value` pairs within the braces adds initial `key:value` pairs to the dictionary. Dictionaries are indexed by keys instead of numeric indices.

It is best to think of a dictionary as an unordered set of `key:value` pairs, with the requirement that the keys are unique (within one dictionary).

The `keys()` method of a dictionary object returns a list of all the keys used in the dictionary, in an arbitrary order. To check whether a single key is in the dictionary, use the `in` keyword.

```python
D = {} # an empty dict
D2 = {'key1':1,'key2':"moose",4:5}
print(D2)
# Key-value pairs can also be defined like this
D2[6] = False
print(D2)
# values can be retrieved using their keys.
print(D2['key2'])
print(D2[6])

# can be used in conditionals
if not D2[6]: # evaluates to false
    print("Dicts are fun.")
else:
    print("Dicts are not that fun.")

# The keys and values of dicts can be accessed as lists.
print("keys: "+str(list(D2.keys())))
print("values: "+str(list(D2.values())))
```

```python
adict={'one':1, 'two': 2, 'three': 3}
print(adict)
print(adict['one'])
print([i for i in adict])

print([(k,v) for k,v in adict.items()])

playlist = (list(adict.values()))
print(playlist[1])
print(list(adict.keys()))
```

The keys do not have to be strings. You can use dictionary comprehensions as well:


```python
mydict={k:v for (k,v) in zip(range(5), range(5))}
mydict
```

You can construct them nicely using the function `dict`.

```python
dict(a=1, b=2)
```


#### Dictionaries and JSON

A **JSON** (JavaScript Object Notation) is a lightweight data-interchange format that is quite standard across the web. It is highly readable and easy for machines to parse and generate. It is very similar to a Python dictionary. However, a dictionary is a python object, while a JSON is a set of characters. We can convert a dictionary into a JSON (or vice versa) very easily with a built-in Python module.

```python
import json

a = {'a': 1, 'b':2}
s = json.dumps(a)
a2 = json.loads(s)

## a is a dictionary
print(a)
## s is a string containing a in JSON encoding
print(s)
## reading back the keys are now in unicode
print(a2)
```

## Flow Control

Python is an imperative programming language. In computer science, imperative programming is a programming paradigm that uses statements that change a program's state. The different states are executed based on a number of rules. We can control the flow of the program through a number of structures. In python there are three main categories of program control flow:

+ Branches
+ Loops
+ List comprehension
+ Function calls

Booleans can be used to control the flow of execution of the code. If-statements execute a section of code if a given bool evaluates to True. There is a specific syntax for booleans, including indentations.

### Branches

```python
flag = True
x = 0
if flag:
    x = 1
    print("Flag is True.")
else:
    x = 2
    print("Flag is False.")
print(x)
# We can check for other cases as well. Controlling the execution of code
# like this is referred to as "flow of control".
if x == 0:
    print("A")
elif x == 1:
    print('B')
else:
    print("C")
```

    Flag is True.
    1
    B

### Loops

### List comprehension

### Function calls

## Syntactical Quirks

### No character after functions!

If you've worked in, for example, JavaScript, you may have noticed that the above lines look a little naked. In some languages, you use, for example, `;` after a function call. This is not the case in Python. A line break is sufficient to indicate the end of a line.

### Interpreted indentation

One of the things that makes Python so readable is that it enforces a common

#### Iteration
Loops allow us to automate repetitive tasks. The repeated execution of a set of statements is called iteration. There are a number of way to iterate in Python. We can use **for** loops or **while** loops too. The syntax is like the syntax of if-statements. The **for** loop loops over each of the elements of a list or iterator, assigning the current element to the variable name given. A **while** loop repeats a sequence of statements until some condition becomes false.



```python
X = range(10)
print(X)
```

    range(0, 10)



```python
for x in X:
    print(x)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
for i in X:
    # doubles the list element
    print(X[i]*2)

print(X)
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    range(0, 10)


We can control the execution of a loop through different statements. Python includes statements to exit a loop prematurely. To exit a loop, use the **break** statement. The loop below is a for loop.


```python
for i in range(10):
    print(i)
    if (i > 5):
        break # breaks out of the loop when it gets a number higher than five
```

    0
    1
    2
    3
    4
    5
    6


While loops are also supported. **continue** continues to the next iteration of the loop skipping all the code below, while **break** breaks out of it.


```python
i=0
while i < 10:
    print(i)
    i=i+1
    if i < 5:
        continue
    else:
        break
```

    0
    1
    2
    3
    4


You can iterate through lists.


```python
myList = ["This", "is", "Python"]
for i in myList:
    print(i) # print the value
    print(myList.index(i)) # print the position of the value (index)

```

    This
    0
    is
    1
    Python
    2


Build a list that contains all the courses that you are taking this semester, and print them. Every time you print a course number add the phrase `In Spring 2017, I am taking:`


```python
# Your code here

```

#### 9. Functions
Functions allow a programmer to write reusable code to perform a single action. Functions provide better modularity for your application and a high degree of code reusing. Once a function is defined, it can be called by typing the name of the function and passing the arguments. For example, Python gives you many built-in functions like **print()**.  Functions can just perform an operation, or they can return values.

Functions are defined using the key work **def**.



```python
#consider this example:
# First choose an initial value for x.
x = 0
for i in range(100):
    x+=i
print(x)

# What if we do this for a new initial value for x?
# What if we use a different number instead of 100?
# We don't want to rewrite this for loop every time.
# Let's define a function.
def ForSum(x,y):
    for i in range(y):
        x+=i
    # "return" indicates what values to output
    return x

# Same calculation from above
print(ForSum(0,100))
print(ForSum(10,50)) # Now with new numbers

# Interestingly, pointers can store functions. This means that functions
# can be inputs to other functions.
F = ForSum
print(F(0,100))

def execute(funct,x):
    return funct(x,100)

print(execute(F,10))

# Now, just for fun:
print(F(F(F(10,100),50),1000))
```

    4950
    4950
    1235
    4950
    4960
    505685



```python
def print_words(x="THIS",y="Not Mike"):
    print(x)
    print(y)

x = "Mike"
y = "Something else"

print_words(x)
```

    Mike
    Not Mike


Now, wrap the code you created for the previous section in a function called `course_printer`.


```python
# Your code here:

```

Series and numpy lists behave similarly as well.


#### Vectorization

Numpy arrays are a bit different from regular python lists, and are the bread and butter of data science. Pandas Series are built atop them.

In other words, operations on numpy arrays, and by extension, Pandas Series, are **vectorized**. You can add two numpy lists by just using `+` whereas the result isnt what you might expect for regular python lists. To add regular python lists elementwise, you will need to use a loop:


```python
newlist=[]
for item in alist:
    newlist.append(item+item)
newlist
```




    [2, 4, 6, 8, 10]



**Vectorization** is a powerful idiom, and we will use it a lot in this class. And, for almost all data intensive computing, we will use numpy arrays rather than python lists, as the python numerical stack is based on it.

You have seen this in idea in spreadsheets where you add an entire column to another one.

Two final examples


```python
a=np.array([1,2,3,4,5])
print(type(a))
b=np.array([1,2,3,4,5])

print(a*b)
```

    <class 'numpy.ndarray'>
    [ 1  4  9 16 25]
