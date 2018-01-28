
# Setting up Git and Github (Command Line) 

***

### Collaboration on Coding Projects

Collaboration is key when working with a group on a coding project. Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. In other words, Git is software that keeps careful track of changes to text files (like code scripts and web pages) in order to allow users to preserve edit histories and merge multiple versions.

### What is Github?

Github is a web service that hosts your code and provides easy ways to store, work with, and share your projects. It is designed for collaboration, meaning that once a file is recognized in Github, if you are working on a project with collaborators, it will identify changes between files, and let the users know when they try to upload if the same lines have been changed. If the same lines have been changed, you have to tell it one you want, this is called a **merge conflict**. If a merge conflict is not found, it will automatically update the online version of the repository with your new code.

Working with Github is easy, there are two main ways you can work with Github, via command line, or with a Desktop GUI. The instructions below will show you how to get started on the command line.

### Why do we use Github?

We are using Github because it has been become a popular standard for open source and collaborative coding projects.

### What are some Git and Github specific terms to familiarize with?

Github has a particular, and sometimes peculiar, set of language and terms that are used when working with it and its functionalities. The following are some common terms and what they mean when you hear them. You will grow more familiar with these over time.

#### Repository

A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including scripts, code, data, and documentation), and stores each file's revision history so you can track changes. Repositories can have multiple contributors (known as collaborators) and can be either public or private.

#### Clone

A clone is a copy of a repository in which you are a collaborator that is on your machine, not the remote Github website. With your clone you can edit the files in your preferred editor and use Git to keep track of your changes without having to be online. It is, however, connected to the remote version so that changes can be synced between the two. You can **commit** and **push** your local changes to the remote to keep them synced.

#### Fork

A fork is a personal copy of *another user's* repository that lives on your account. Forks allow you to freely make changes to a project without affecting the original. Forks remain attached to the original, allowing you to submit a pull request to the original's author to update with your changes. You can also keep your fork up to date by pulling in updates from the original. To edit files, you must **clone** your forked repository to your machine, and you can work with it as if it is your own.

#### Fetch

Fetching refers to getting the latest changes from an online repository without merging them in. Once these changes are fetched you can compare them to your local branches (the code residing on your local machine).

#### Pull

Pull refers to when you are fetching in changes in an online repository and merging them into your local version. For instance, if someone has edited the remote file you're both working on, you'll want to pull in those changes to your local copy so that it's up to date.

#### Merge

Merge is the process of taking files from one version of the repository (i.e. the online version) and syncing them with another (i.e. your local version). This is the process of combining two versions and resolving conflicts. If there are conflicts, those are called **merge conflicts**, and must be resolved manually.

#### Merge Conflict

A merge conflict is when two collaborators change the same line of the same file in a repository. These are not a problem, when you collaborate it will happen, however it can be a bit confusing at first. To resolve a merge conflict, the user needs to pick which line is the one that should be saved. Merge conflicts must be resolved in order to successfully **pull** and **push** repositories.

#### Commit

When you change a file, before you **push** to the online version, you need to **commit** the changes. A commit, or "revision", is an individual change to a file (or set of files). It's like when you save a file, except with Git, every time you save it creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep record of what changes were made when and by who. Commits usually contain a commit message which is a brief description of what changes were made.

#### Push

Pushing refers to sending your committed changes to a remote repository such as GitHub.com. For instance, if you change something locally, you'd want to then push those changes so that others may access them.

#### Branch

A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary or master branch allowing you to work freely without disrupting the "live" version. When you've made the changes you want to make, you can merge your branch back into the master branch to publish your changes.

***

Okay, let's get started with Github, set up our computers to talk to the Github website so we can push and pull files, and let's give this a try!

***

## 1. Sign up for a Github account

Sign up for a Github account on the Github site in which you can host projects and maintain repositories.

[Github Homepage](http://www.github.com)

Once signed up, go to your profile page.


## 2. Create, join, or fork repositories in your Github account

To start us off, we need a project (aka repository) to work on. This is the Github way of storing projects. So on the Github site, let’s create a repository. Repositories can be used for many projects, allowing you to collaborate, share, and modify scripts, programs, and websites. Project repositories can be named just about anything, and you should pick something relevant to your project.

For this exercise, we are going to set up a repository that will hold HTML, CSS, and JavaScript for a website. Other projects can range from Python projects, to C projects, to just about any language you can find.

### Create a website using Github Pages

In our website repository, we have keep the HTML, CSS, and JS required for our webpage. A feature of Github is the ability to create a homepage using something called [Github pages](https://pages.github.com/).

To use Github pages, you have to name your repository very specifically. The following steps detail creating a repository and setting up the initial settings.

***

#### i. Click on the Repositories tab on your main profile page.

On your Github profile page, click on the Repositories tab.

#### ii. In the upper right corner, select ‘New’.

Create a new repository.

#### iii. In the Create a new repository window, set up your repository.

Name the repository **username.github.io**, and *replace username with your Github username*. Give the repository a description, make it public, and initialize it with a README. Don’t worry about the license at this point.

#### iv. Click Create.

You now have an empty repository set up in which you can add files and set up a project.

***

Our repository is on the Github webpage in our profile. Now we can **clone** a copy to our local machines so we can edit the files and materials. To do that though, we need to set up Git on our machine. We want to set it up so we can interact with it via command line on our local machine to create, edit, and manage files, which means we need to set up a secure key that Github will recognize is only on your machine.

***

## 3. Setting up Github

### Check to see if Git is installed, if not, we need to install Git

Moving back to our local machine, we need to get git and Github setup so we can work with it.

**If you are using Mac:** Using Terminal, we are going to check for Git, and if it is not found, we will download and install necessary files.

**If you are using Windows:** Git does not work easily from the Windows command prompt. To easily use command line to interact with Github, you need to install Github for desktop where you can use Git Bash. This is a command line interface that allows you to run commands to create repositories, rectify file differences, and push commits.

[Download Github for Desktop](https://desktop.github.com/)

Once downloaded, proceed below, but instead of using Terminal, you use Git Bash.

#### i. Open Terminal/Git Bash

#### ii. Check git installation by entering the following command

***

```sh
git –-version
```

***

if you have Git installed, you will see the version. If you get an error, or you don’t see the version, you need to install Git. Install Git from the downloads page on the main Git project homepage.

https://git-scm.com/

Download Git for your machine. A wizard will lead you through the installation. You can select the defaults for installation. You might need to restart your machine after installation to get it to take effect.

***

## 4. Authenticate with Github using SSH

Because our work is stored online on the Github page, our local machine needs to communicate with the Github servers in order to pull and push project documents. This requires authentication with the Github servers, and Github will ask us to enter our username and password everytime we want to pull or push files. If we are making alot of changes, entering our username and password everytime you push a file to the server can get tedious.

The best solution is to set up your computer to communicate with Github via SSH. SSH is a secure connection in which we provide Github a unique address for our computer that it will recognize and trust, so we can communicate between the two without constantly having to reauthenticate. It will give you instant access to your Github folders.

In order to do this, you need a key that is unique to your instWe need to create an SSH key unique to our local machine that Github can store and recognize. Create an SSH key on your machine by following the instructions at the following link. The steps will lead you through setting up a unique key that allows Github to ‘trust’ your machine. Take the key created on your machine and paste into your account on Github.com. This key allows you to connect to Github via Terminal without entering your Github username and password.

The Github site contains very nice instructions on how to do this. Before you continue the tutorial, set up SSH authentication by following the instructions on the Github help pages at the following address. On this page, please work through the steps one by one to set up your SSH key to work with Github.

1. About SSH
2. Check for existing SSH Keys
3. Generating a new SSH key and adding it to the ssh-agent
4. Adding a new SSH key to your Github account
5. Testing your SSH connection
6. Working with SSH Key passphrases

https://help.github.com/articles/generating-ssh-keys/

***

## 5. Create a Directory for Github Projects

Next we want to setup a Github folder on your computer that can contain local copies of our Github project directories. The easiest way to edit and change code is to work on it on your own machine. You can then sync the repository folders with the Github servers so others can see and use your code modifications, and you can pull changes others have made. Please work through the following steps get your repo set up.

### Create a github folder in your Documents

First, create a **github** directory on your machine. We are going to set up a **github** folder within the Documents folder of our local profile (**documents/github**) using Terminal and some basic command line to complete the task.

#### i. Open Terminal, change your current location to your Documents directory.

Use cd to change directories on your machine to the location you want to store documents.

***

```sh
cd documents
```

***

Note: You can use **pwd** to find out your present working directory)

#### ii. Create a new directory called ‘github’

Make a new folder that will hold our github projects.

***

```sh
mkdir github
```

***

This creates an empty folder called github in our Documents folder. We will use this for storing local copies of our github repositories and as working space when we edit and modify projects.

#### iii. Change the working directory to your new 'github' directory

Change directories to your new github directory.

***

```sh
cd github
```

***

The ‘github’ folder is now your working directory and commands we run will be happening in this directory. We will work locally on our Github repositories in this space.

You saw this require some command line work. For documentation on additional command line commands and shortcuts, the following cheatsheet can be very helpful. Descriptions of the commands we just used, if you are curious, are included.

https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)


## 6. Clone a copy of the repository you want to work on

Create a clone of the website repository on your machine so you can edit code and files. This will allow for pulling, merging, and pushing changes you make to your files.

To access Github commands in the terminal, use the term **git** to begin your statement.

#### i. With your SSH authentication setup, clone your first repo to your local drive using the following.

Replace with your username to get your github.io repository. To do this, you can use **git clone**.

***

```sh
git clone git@github.com:<Github username>/<Github username>.github.io.git
```

[Read more about the git commands available in terminal](https://www.siteground.com/tutorials/git/commands.htm)

***

#### ii. Change your working directory to your cloned repo.

***

```sh
cd <Github username>.github.io
```

***

Take a look in your finder window, you will see a ‘github-username.github.io’ folder is now in your github folder.

***

### 6b. Create a Repository Remotely using Command Line using Git Init

Above, we created a repository on the Github webpage. What if we want to create one from the command line (remotely) in an existing directory and then push that to Github so others can collaborate with us?

The steps to remotely create a repository are detailed by the [Github docs](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).


## 7. Make edits locally in your repository

Going back to your ‘username.github.io’ folder that you have created, you can add, edit, modify, and delete files from this directory. This directory is local, but we will use the command line to sync it with the repo on the Github site. This is where Github shines, you can fully edit documents and files on your machine, then synchronize them with your repositories on the Github site. This is excellent for group work and versioning.

#### i. Install a Text Editor (Sublime Text)

*If you have Sublime Text installed, you can move on to the next step*

When editing code, it is important to use a Text Editor and not a Word Processor. A text editor is a simple program that edits text files. This is distictly different than a Word Processor, such as Microsoft Word. In order to properly format, show colors, and display different fonts, programs such as Microsoft Word add alot of extra code to the source files. We don't want this! Text Editors work purely with the text they are provided, and are used for writing code, scripting, and programming.

The text editor we recommend is called **Sublime Text**. Before moving on, please install it and use it for writing your code.

[Sublime Text 3](https://www.sublimetext.com/3)

#### ii. Edit the Github README

Edit the README to contain your name and some information on your project. This README contains the text that is visible to visitors to the Github repo. Here you can descriptions on what your project is, what it does, and how people that fork a copy can use it.

For example, you could write the date and that this is your Github homepage.

#### iii. Create our website... write some code!

Let's begin our project. Working in the project directory on your machine, you can work with or create almost anything. For example, let’s create a basic HTML document. Open a text document, copy and paste the following code snip. We are going to call this **index.html**.

***

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8"> 
	<title>Hello World</title>
</head>
<body>
	<h1>Hello World</h1>
	<p>I wuz here.</p>
</body>
</html>
```

***

Save the document in the **username.github.io** directory as **index.html**. Now we can start the process of creating a **commit**, and once we have a commit, **push** our code to the Github website.


## 7. Use git status to check the working status and synchronization of documents.

When working on the command line, Git and Github have many commands you can run that you will need to familiarize yourself with.

Having made the changes above and saved them, go back to terminal. Enter:

***

```sh
git status
```

***

This checks the current status of changes. You should see that our **README.md** was modified, and that **index.html** is not yet tracked. However, these files are not yet staged to be committed to the online repository. In order to commit this files to our online repository, we need to stage them first.

## Commiting and Pushing Changes

## 8. Stage your changes, modifications, and additions

When you are done working, stage your changes by using:
***
```sh
git add <filename>
```

***
This puts the files into the Git staging area. You can add multiple files to your staging area at once. If you edit many files on your machine, when you are done, put them each into the staging area and you can sync them with the online repository all at once.

Stage our files using the following syntax:

***

```sh
git add README.md
git add index.html
```

If you want to stage all files, use:

```sh
git add .
```

***

Check the result by typing in git status again to see that the changes are ready to be committed. If you ever need to unstage anything, use the following:

***
```sh
git reset HEAD <filename>
```
***

**Important to note:** files are not staged in their entirety, rather, changes to the files are staged.

## 9. Commit files to our repository

Once you are happy with your edits and you have made all your modifications, we are ready to commit the files and update the repository. We start locally - that is, with the repository stored in our local instance of Git. Remember, Git acts as an intermediary between us and our edits. When we change files on our local machines, Git keeps track of changes, but we need to commit those changes to the local repository so that Git knows we'd like to consider this a checkpoint.

It is best practice to add a comment to your commit that describes the changes you made to the files. For example, for this exercise, we can say we ‘added the index.html document and updated the readme’. This helps others working with your code stay organized and informed on what you did that made this commit worthy.

To commit our files, we use git commit. We add a –m flag for the message we want to include with our commit. In terminal, still in your working directory and with our files staged, use the following.

***
```sh
git commit –m “added index.html and updated readme”
```
***

This commits our changes to the local repository.  You will see a note that files in your master branch were changed and created.
 
## 10. Push files to our online repository

The last step is push the files to the remote repository on the Github website to synchronize them for the rest of our team and any others that want to work with our files. We do this using git push. The syntax for this is **git push origin branchname**. This will push the file to the remote origin and match it to the name of the branch. If the branch doesn’t exist, it will be created. To push our files to Github, use the following:

***

```sh
git push origin master
```

***

You might have to enter your password to authenticate once more upon hitting enter. This will push our master branch to Github and sync our files.

Go online to your Github profile page and check the ‘username.github.io’ repository. You should see your files and modifications! Wash, rinse, and repeat.

## 11. View your Website

Visit your Github site to see your page!

Open a browser and navigate to:

http://yourusername.github.io

Congrats, you have created your first github repo, and a new website in the process!

===


## 12. Working with Branches

Up to this point, we have been working with our ‘master’ branch. The ‘master’ branch is the main branch of our repository, and should always be kept working and clean. If we want to work on a copy that is different than the live ‘master’ branch, we can create a working branch that has a copy of all of the files in the master branch, then try out changes on the working branch so you don’t break code that is in the master branch.

Keep in mind that creating new branches will not create new local file directories. That is, if you make changes to a local file while a non-master branch is checked out, the changes are stored in the local Git repository, but the original local file is unchanged (as it is represented by the master branch in Git).

In Terminal, to create a branch, follow the following steps.

#### i. Create a branch based on the master branch

To create a branch based on the master branch, use the following syntax:

***
```sh
git checkout –b <new branch name> <existing branch name>
```
***

For example, we can use:

***
```sh
git checkout –b test-changes master
```
***

to create a new branch called test-changes of the master branch. (Technically the master part at the end is unnecessary, but always better to be verbose).

#### ii. Show all local branches by using the branch command

Show all branches of the repository using the following command:
***
```sh
git branch
```
***
**Note:**An asterisk will appear next to the current working branch.

#### iii. Switching between branches

Use **git checkout** to switch between branches. Switching back to the master branch would look like:

***
```sh
git checkout master
```
***

#### iv. Merge branches

Merging branches is easy. To merge **test-changes** back into master, change to your master branch using checkout, and then use the merge command.

***
```sh
git checkout master
git merge test-changes
```
***

#### v. Commit and Push a Branch

Branches can be commited to the local repository and synced to the remote repository (on the Github site) using the same **push** process described in the steps used for the master branch above.

#### vi. Delete a Branch

If you ever need to delete a branch if you are done working in a branch and have merged changes, use the –d key of the branch command. For example, to delete test-changes, use:

***
```sh
git branch –d test-changes
```
***

**Branches are a powerful component of working with Github!**

## 14. Resolving Merge Conflicts

Users working in large groups are bound to run into some conflicts when two or more people are working on the same files and changing the same lines of code. There are methods for resolving this, but unfortunately will require some manual checking. In short, conflicts will be flagged in your file when you open it in a text editor. You will have to go through your file and find conflicts, decide which one to accept, and then delete the surrounding conflict markers. This is described in nice detail on the Github help pages at the following address.

https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/

Congrats, this crash course has introduced you to git and Github! Clearly there is much more to learn, including handling issues, which are like tickets individuals can open on your code, then interact with the authors to resolve, and pull requests, where authors can take modified code and merge it into their original projects. See below for additional reading, cheatsheets, and resources.

Github has a DESKTOP APP! This makes things quite a bit easier. If you are comfortable working on the command line, you can stop here, but to learn the Desktop app, check out Part 1B.


## 12. Pulling changes from Github

Often you will need to incorporate changes made by others on the remote repository on your local drive.  In this case, you can log into terminal and use git pull. Git pull will retrieve new work done by other people and merge the local changes with changes made by others. Syntax appears like the following. (syntax looks like the following - **git pull remote branch **)

***
```sh
git pull origin master
```
***

For more on this, read the following at the Github help pages.

https://help.github.com/articles/fetching-a-remote/
***

***


## Additional Reading and Resources

#### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

#### Github Glossary –
https://help.github.com/articles/github-glossary

#### Git on the Command Line - 
http://dont-be-afraid-to-commit.readthedocs.org/en/latest/git/commandlinegit.html

#### Git Branching – Basic Branching and Merging
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

