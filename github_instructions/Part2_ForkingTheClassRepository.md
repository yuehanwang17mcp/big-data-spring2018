# Forking the Class Repository

Key concepts: fork, fetch

Most of our work this semester will be channeled through a class Github repository in which all of the course files and materials are uploaded, maintained, and stored. Each week, course materials will be pushed by the teaching staff into the class repository; student submissions will also be pushed to forks of the class repository.

Find the class repository here:

[https://github.com/ericmhuntley/big-data-spring2018](https://github.com/ericmhuntley/big-data-spring2018)

To download a local copy of the course files, **fork** a copy of the class repository into your own Github profile. **You only need to do this once.** This will give you your own copy of the class repository that you can edit it at will. However, it will also still be linked to the original repository, meaning you can **fetch** and **pull** materials from it as needed. Let's start be making our **fork**.

#### A. Fork the Class Repository

Create your own personal copy, or ‘fork’, of the class repository.

1. First click fork on the Github page of the main class repository.
[https://github.com/ericmhuntley/big-data-spring2018](https://github.com/ericmhuntley/big-data-spring2018)
2. In Github, navigate to your profile and locate your personal fork of repository.
3. Open Terminal (for Mac and Linux users) or Git Bash (for Windows users). Change to your github directory.
5. Type `git clone https://github.com/<Github username>/big-data-spring2018.git`.

After completing this step, you will be able to work with and edit your own version of the class repository; you have now **forked** the repository and **cloned** it onto your machine. Changes here will not affect the main class repository. You can **pull**, **merge**, **commit**, and **push** to your **fork** as much as you want.

## Get New Files from the Main Class Repository

#### B. Before getting files from the main repo, commit changes to your own repo.

You will need to commit any changes you've made to the forked repository before you can **pull** new files from the class repository. This will let Github know what has changed and what hasn’t. When you pull the main class repository, Github will provide the main class files, give you files you don’t have, and flag any items that were changed in both your personal fork and main class repo. To do this, run through the following steps.

1. Using Terminal or Git Bash, change into the directory that contains the local copy of your forked repository.

```sh
cd path/to/my/repo
```

2. Before you pull, you need to check if any files have changed because you will need to commit these files before you can **pull** changes to the class repo from Github.

```sh
git status
```

If you have not changed any files, or you have already committed your changes to your own forked repository, you will get a message informing you that everything is up to date.

3. If Git tells you you have modified files in the step above, you need to stage and commit those changes to your personal fork, then push them. This is required in order to prep for a pull from the main repo. This process should be starting to feel familiar...

```sh
# Tell git which files need to be committed to your repository.
git add changed_file.md

# Commit the changed files locally to your personal fork. Remember to include a commit message to serve as a short explanation of what you changed.
git commit –m ‘my commit message’

# Push the changes to Github. This syncs the files with the online version of our personal forked repo.
git push origin master
```

It's a **push**! **Origin** is the remote repository, and **master** is the branch we are pushing.

#### C. Fetching the Folders for the New Week

There are a couple of methods to get new materials from Github and incorporate them into your forked repo: the primary commands are `pull` and `fetch`. We are going to show you here how to `fetch` only the new folders you specify. Each week we will be uploading a new folder with the materials for that week; use the method below to retrieve only the new week's folder from the remote class repository.

1. First, view and setup your remote versions. These are the remote Github repositories that are associated with your forked repo, meaning this is your personal fork, and actually the main original fork as well (full class repo). To view the remote versions, type the following:

```sh
git remote -v
```

Here you will see your remote directories. Mine looked like this.

![Checking Remote Directories](images/screenshot.jpg "Checking Remote Directories")

Notice the first line, it is the main class repo! It starts with ‘civic-data-design-lab’.

2. Use `fetch` to retrieve the main class repo. In this step, you will use `git fetch` to grab the remote repository. Grab the listing that starts with ericmhuntley and we want the `master` branch.

```sh
git fetch ericmhuntley master
```

3. We then need to grab our specific folder. We do that using `git checkout`. This will let us grab the specific file we are looking for by adding an argument to the end of the command. This argument is the relative path to the file you want to get from the location of the repo. This should be your file name and path. In this example, the week-04 folder is in the main class repo at the base level, so we can just put week-01.

```sh
git checkout ericmhuntley/master -- week-01
```

This will bring you only the folder called ‘week-01’. Obviously, this can be changed to retrieve the folder according the proper week (or name of the folder!)

4. You will now have the new folder called ‘week-01’ in your personal fork, and they’ll be ready to edit, save, and do what you want with. To view the folder, open up the folder on your machine that contains your personal forked repository.

<!--
### Troubleshooting Pull Problems
If you get a publickey error, you need to configure your SSH setup. To do this, go through the following steps.

1. Check for SSH keys:
https://help.github.com/articles/checking-for-existing-ssh-keys/
2. Generate a new SSH Key and add it to the SSH agent:
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
Important note: if you already have one, click yes to OVERWRITE the old one.
3. Add your new SSH key to your Github account:
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/ -->
