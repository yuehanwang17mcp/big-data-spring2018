
# Problem Set 4: Networks

### Mapping Social Activism Groups in Pennsylvania

In this problem set we are going to be working with social data to visualize a network of activism groups. The data is provided by the DUSP CoLab Mapping Resistance project, and contains 41 grassroots social activism and civic justice groups in Pennsylvania. The dataset we provide contains the number of Twitter followers for each of the groups, along with a list of ids of each follower. Our goal is to get a better picture of the social connectivity of these groups, and figure out which of the groups share Twitter followers, and of the ones that share followers, how many are the same.

The data was scraped from Twitter using the REST API, not too unlike what we did last week. It is provided to you in JSON (JavaScript Object Notation) format in the **jsons** folder in your materials.

We will give you the functions we used to aggregate and create the network datasets, your job is to build the network using NetworkX.

First, we will read in the data. While **NetworkX** has a number of built-in functions to import data, and directly construct a network, our data doesn't follow their requirements. We will select it through **pandas**, and then we will build the network procedurally using Python functions.

The steps we take look like the following:

1. Load the list of social justice groups
2. Create nodes
3. Create edges
4. Construct the NetworkX drawing


```python
# Import some libraries to work with
from os import listdir
from os.path import isfile, join
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This allows plots to appear on the IPython notebook.
%matplotlib inline 
```

### Load the Social Justice Groups

We have a spreadsheet of collected social justice organizations in Pennsylvania, 41 of them to be exact. We also have a folder of JSON datasets that contain the Twitter followers for each. From this, we can work towards building a network. To start, let's load our spreadsheet of organizations and create a list of the twitter names so we can build a function that will automatically load the JSONS. There is a CSV named `social_justice_orgs_pa.csv` that contains the names of each of the organizations, their twitter handles, and a bunch of other information.

Load this CSV, and create a Python list of twitter handles we can loop through.


```python
df = pd.read_csv('social_justice_orgs_pa.csv')
df
```

Create a list of groups from the Twitter handles. We can loop through this collect our data (already done!) and then to load our files for processing


```python
groups = df['twitter_name'].tolist()
groups
```

### Create the Data for our Network Nodes

Next, let's create the data for our nodes, the groups themselves. We want to create a list where each item in the list contains the name of the group (the Twitter handle), and the number of followers. We can use the number of followers as the weight in our network.

**Take a look at the data**

Open the **jsons** folder and see our collection of JSONs. Each one of these files contains a JSON dataset with a property named **name** that is the name of the groups Twitter handle, and a property named **ids** that is a list of all of the ids of users that follow that account.

**Loop through and grab the data**

To do this, I've created a function called **create_nodes** that loops through our list, finding files with the matching name, then pulls out the **name** and a count of the ids (number of followers). For example, below, run it and see that **1lovemovement1** has 391 Twitter followers.


```python
def create_nodes(g):
    nodes = []
    for i in g:
        node_data = open('jsons/'+ i + 'tweets.json')
        node_data_json = json.load(node_data)
        node_element = [node_data_json['name'], len(node_data_json['ids'])]
        nodes.append(node_element)
    return nodes

nodes = create_nodes(groups)
nodes
```

We can use this list for our nodes.

### Create the Data for our Network Edges

Now, let's process the data files to create our edge data. This is a bit more complex because we have to some matching betweem accounts. We want each edge in the network to have a connection if there are common followers, and then for the weight of that connection to be the number of common followers.

To do this, I've create a function that loads each file, grabs the list of ids, then for each id, loads each file again and checks to see if there are matches between the datasets. Its a loop nested within a loop. To find the matches, we are using something call [set](https://docs.python.org/3/tutorial/datastructures.html#sets). Within the inner loop, it will populate a new array with the names of each of the groups, and the number of common followers.

The function, in the end, will look as follows, and our output will be an array with each element representing a pair of Twitter handles, and a number representing the number of common followers.


```python
# create edges by opening the datasets, then finding matches and saving the number of common followers
def create_edges(g):
    network_edges = []
    for i in g:
        group_1 = open('jsons/'+ i + 'tweets.json')
        group_1_json = json.load(group_1)
        group_1_followers = group_1_json['ids']
        for j in g:
            group_2 = open('jsons/'+ j + 'tweets.json')
            group_2_json = json.load(group_2)
            group_2_followers = group_2_json['ids']
            common_followers = len(set(group_1_followers) & set(group_2_followers))
            node1 = group_1_json['name']
            node2 = group_2_json['name']
            edge = str(common_followers)
            zipped = ([node1, node2], edge)
            network_edges.append(zipped)        
    return network_edges

# Create a variable
edges = create_edges(groups)

edges
```

#### Clean the Data

This data is messy, it contains bidirectional duplications, and zero values represent no common followers (no edge!) so we need to do some cleaning to get it ready.

I've written up a function here that reads in our messy edge array, sorts them to find duplicates by testing equality, then finds zero values and finds nodes, and creates and returns an array with all of these scrubbed out.


```python
# Check for bidirectional duplicates and remove them
def sort_the_edges(network_edges):
    sorted_list = []
    edges_no_duplicates = []
    edges_no_zeros = []
    edges_no_nodes = []
    for i in network_edges:
        sorted_i = sorted(i[0])
        node1 = sorted_i[0]
        node2 = sorted_i[1]
        edge = i[1]
        zipped = [node1, node2, int(edge)]
        sorted_list.append(zipped)
    for i in sorted_list:
        if i not in edges_no_duplicates:
            edges_no_duplicates.append(i)
    for i in edges_no_duplicates:
        if i[2] != 0:
            edges_no_zeros.append(i)
    for i in edges_no_zeros:
        if i[0] != i[1]:
            edges_no_nodes.append(i)
    return(edges_no_nodes)

edges_cleaned = sort_the_edges(edges)
edges_cleaned
```

Just to check, we should have 669 edges in our dataset!


```python
len(edges_cleaned)
```

## Create the Network and Visualize it

We now have two datasets, **nodes** and **edges_cleaned**, that we can use to create our network and visualize the connections between the groups. Your job is to now implement NetworkX and create the network to examine the connections between the groups.

#### Deliverable

Using the methods discussed in the in class exercise, submit a Jupyter Notebook with the following:

1. Drawn Network Graph of the nodes and edges of the Social Justice Groups
2. A histogram of the Degree Distribution, with the number of Social Justice groups and the Number of First Degree Connections.


```python
# Your code here

```
