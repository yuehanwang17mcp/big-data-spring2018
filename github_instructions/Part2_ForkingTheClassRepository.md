# Forking the Class Repository

Most of our work this semester will be channeled through a [class Github repository](https://github.com/ericmhuntley/big-data-spring2018). This repo is where you will find all of the course materials; these will be pushed up by the teaching staff each week. student submissions will also be pushed to forks of the class repository.

To download a local copy of the course files, `fork` a copy of the class repository into your own Github profile. **You only need to do this once.** This will give you your very own copy of the class repository that you can edit at will. However, it will also still be linked to the original repository, which makes magic possible: you can `fetch` and `pull` materials from the original repository as it the teaching staff update it.

## Fork the Class Repository

Create your own personal copy, or ‘fork’, of the class repository!

1. Click 'fork' on the Github page of the [main class repository](https://github.com/ericmhuntley/big-data-spring2018). If you navigate to your profile page after doing so, you'll see a copy of the class repo. This is your fork!
2. Open Terminal (for Mac and Linux users) or Git Bash (for Windows users). Change to your github directory (remember `cd`?).
3. Type `git clone https://github.com/<Github username>/big-data-spring2018.git`.

You have now forked the repository and cloned it onto your machine. This means that you can now work with and edit your own version of the class repository. Changes made here will not affect the main class repository.

## Commit changes to your fork

You will need to commit any changes you've made to the forked repository before you can fetch new files from the class repository. This way, Git will know what has changed and what hasn’t. When you fetch the main class repository, Github will provide the main class files, give you files you don’t have, and flag any items that were changed in both your personal fork and main class repo. As a reminder, you stage, commit, and push changes using the following series of steps.

Using Terminal or Git Bash, change into the directory that contains the local copy of your forked repository.

```sh
cd path/to/my/repo
```

Before you fetch, you need to check if any files have changed because you will need to commit these files before you can fetch changes to the class repo from Github.

```sh
git status
```

If you have not changed any files, or you have already committed your changes to your own forked repository, you will get a message informing you that everything is up to date.

If Git tells you you have modified files in the step above, you need to stage and commit those changes to your personal fork, then push them. This is required in order to prep for a fetch from the main repo. This process should be starting to feel familiar...

```sh
# Tell git which files need to be committed to your repository.
git add changed_file.md

# Commit the changed files locally to your personal fork. Remember to include a commit message to serve as a short explanation of what you changed.
git commit –m ‘my commit message’

# Push the changes to Github. This syncs the files with the online version of our personal forked repo.
git push origin master
```

It's a `push`! `origin` is your forked remote repository and `master` is the branch we are pushing.

## Fetch new content

There are a couple of methods to get new materials from Github and incorporate them into your forked repo: the primary commands are `pull` and `fetch`. We are going to show you here how to `fetch` new content and merge it into your current branch. Each week we will be uploading new content; use the method below to retrieve this content from the Github remote.

### Set up a remote

First, view and setup your remotes. These are the remote Github repositories that are associated with your forked repo, meaning this is your personal fork, and actually the main original fork as well (full class repo). To view the remote versions, type the following:

```sh
git remote -v
```

Here you will see your remote repositories (often referred to simply as 'remotes'). We need to add a remote that refers to the original class repository!

We do this using the `git remote add` command. We're going to add a remote repository that we'll call 'class' and that will link our fork to the original class repository.

```sh
git remote add class https://github.com/ericmhuntley/big-data-spring2018.git
```

### Fetch and merge

Use `git fetch` to grab the `master` branch of the remote class repository (i.e., `origin`). We then want to merge it into our master branch.

```sh
# Check out our fork's master branch.
git checkout master
# Fetch changes.
git fetch class
# Marge master branch of class repo into our current branch (`master`)
git merge class/master
```

You might ask: why use `fetch` and not `pull`? Essentially, `pull` takes the two above commands (`fetch` and `merge`) and collapses them into one. "How efficient," you might say! True, but it can cause trouble and lead to situations where you lose work completed locally. If you're curious, you can [read this article](https://longair.net/blog/2009/04/16/git-fetch-and-merge/) for a longer-winded justification.

## Fin.

You've just fetched a changes to an upstream repository and merged them with your master branch without affecting your changes to the repository! Pretty cool, eh? In part 3, we'll talk about how to resolve the conflicts that can occur when merges don't go quite so smoothly.

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
