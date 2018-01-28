
# Getting your Own Copy of the Class Repository
### Fork a Copy of the Class Repository (Command Line)

***

The Big Data class has a repository in which all of the course files and materials are uploaded, maintained, and stored. Each week, materials will be pushed by the teaching staff into the class respository.

Find the class repository here:

[https://github.com/civic-data-design-lab/big-data-spring2017](https://github.com/civic-data-design-lab/big-data-spring2017)

To get a copy of the files, **fork** a copy of the class repository into your own profile. **You only need to do this once.** This will give you your own version of the class repository, and it is still linked to the main class repository, meaning you can **fetch** and **pull** materials from it as needed. Let's start be making our **fork**.

#### A. Fork the Class Repository

Create your own personal copy, or ‘fork’, of the class repository.

1. First click fork on the github page of the main class repository.
(https://github.com/civic-data-design-lab/big-data-spring2017)[https://github.com/civic-data-design-lab/big-data-spring2017]
2. In GitHub, navigate to your profile and locate your personal fork of repository.
3. In the right sidebar of your fork's repository page and copy the clone URL for your fork.
4. Open Terminal (for Mac and Linux users) or the command prompt (for Windows users). Change to your github directory.
5. Type **git clone** followed by the URL to your forked repository.

***

```sh
git clone git@github.com:username/big-data-spring2017.git
```

***

After completing this step, you will be able to work with and edit your own version of the class repository that you have **forked** to your profile and **cloned** on to your machine. Changes here will not be made to the main class repository. You can **pull**, **merge**, **commit**, and **push** to your **fork** as much as you want.

## Get New Files from the Main Class Repository

#### B. Before getting files from the main repo, commit changes to your own repo.

After doing some work in your own repository, you will need to commit your own changes to your personal forked repository before you can **pull** new files from the class repository.

This will let Github know what has changed and what hasn’t. Once Github knows this, then you can you can pull from the original main class repository. When you pull the main class repository, Github will provide the main class files, give you files you don’t have, and flag items that were changed in both your personal fork and main class repo. To do this, run through the following steps.

1. Using Terminal, change into your personal forked repository.

***

```sh
cd path/to/my/repo
```

***

2. Before you pull, you need to check which files have changed , because you will need to commit these files before you can get the changes on Github. To get a list of files changed, use the following:

***

```sh
git status
```

***

For sake of example, when I did this, I saw that I had modified one file: **01_Pandas_Introduction.ipynb** If you have not changed any files , or you have already committed your changes to your own forked repository, you will get a message that everything is up to date.

*If you found that your repository is up to date, you can skip to PART
C*

3. If git tells you you have modified files in the step above, you need to commit those changes to your personal fork, then push them. This is required in order to prep for a pull from the main repo. The git process involves adding your files, committing them to the local version of your personal fork, and then pushing your commit to your remote personal forked repo.

***

```sh
# Tell git which files need to be committed to your repository (mine was 01_Pandas_Introduction.ipynb).
git add 01_Pandas_Introduction.ipynb

# Commit the changed files locally to your personal fork. Include a commit message, a short explanation of what you changed.
git commit –m ‘my commit message’

# Push the changes to Github. This syncs the files with the online version of our personal forked repo.
git push origin master
```

***

It's a **push**! **Origin** is the remote repository, and **master** is the branch we are pushing.



#### C. Pulling the Folders for the New Week

There are a couple of methods to get new materials from Github to your repo, we are going to show you here how to get just the new folders you specify. For example, each week we are uploading a new folder with the materials for that week, this is how you can get just the new weeks folder from the main class repository.

1. First, view and setup your remote versions. These are the Github repositories from the site that are associated with your personal forked repo, meaning this is your personal fork, and actually the main original fork as well (full class repo). To view the remote versions, type the following:

***

```sh
git remote -v
```

***

Here you will see your remote directories. Mine looked like this.

![Checking Remote Directories](images/screenshot.jpg "Checking Remote Directories")


Notice the first line, it is the main class repo! It starts with ‘civic-data-design-lab’.

2. Use **fetch** to retrieve the main class repo. In this step, you will use *git fetch* to grab the remote repository. Grab the listing that starts with civic-data-design-lab and we want the master branch. If you created a nickname for your repository, use that. If you don’t know what this means, you didn’t create one.

***

```sh
git fetch civic-data-design-lab master
```

***

3. Once this is run, we then need to grab our specific folder. We do that using git checkout. This will let us grab the specific file we are looking for by adding an argument to the end of the command. This argument is the relative path to the file you want to get from the location of the repo. This should be your file name and path. In this example, the week4 folder is in the main class repo at the base level, so we can just put week4.

***

```sh
git checkout civic-data-design-lab/master -- week4
```

***

This will bring you only the folder called ‘week4’. Obviously, this can be changed to retrieve the folder according the proper week (or name of the folder!).

4. You will now have the new folder called ‘week4’ in your personal fork, and they’ll be ready to edit, save, and do what you want with. To view the folder, open up the folder on your machine that contains your personal forked repository.

### Troubleshooting Pull Problems
If you get a publickey error, you need to configure your SSH setup. To do this, go through the following steps.

1. Check for SSH keys:
https://help.github.com/articles/checking-for-existing-ssh-keys/
2. Generate a new SSH Key and add it to the SSH agent:
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
Important note: if you already have one, click yes to OVERWRITE the old one.
3. Add your new SSH key to your Github account:
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
