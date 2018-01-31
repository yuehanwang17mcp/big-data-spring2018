# Resolving Merge Conflicts

Sometimes, when working on a project, you and your colleagues will change the same line of code. This often happens unintentionally, and you end up with a conflict between two files. No need to panic, simply read the message, and locate what the error might be. If two people change the same line of code, Github will not know which one it should keep, so you have to tell which one, and remove the other.

When this happens, you will see an error similar to the following:

```sh
Auto-merging test.txt
CONFLICT (content): Merge conflict in test.txt
Automatic merge failed; fix conflicts and then commit the result.

```

What this is saying is that there is a conflict in the file **test.txt**. When we try to pull and there are conflicts, Github will add the conflicts to our file. To fix this conflict, we need to open the file and choose which of the competing lines we want to use.

## Identifying Merge Conflicts

Navigate to the file with conflicts on your computer and open it up using Atom (or your favorite text editor). We'll manually resolve the conflicts in the text editor. With the file open, locate the merge conflicts. These are identified by **conflict markers**, which look like **<<<<<<<**, **=======**, and **>>>>>>>**. The **<<<<<<<** delineates the start of the conflict. Immediately following are the changes you've made to your local copy of the repository. Following the comparison marker (**=======**), you'll find changes made to the remote repository. The **>>>>>>>** marker signals the end of the conflict.

To demonstrate, merge conflicts might look something like the following:

```sh
<<<<<<< HEAD # Start of changes made on your local machine

Hello. # Your changes and edits
======= # Comparison marker
Good bye. # Other changes and edits

>>>>>>> ANOTHER BRANCH # End of changes made on the remote repository
```

## Edit the File to Resolve Conflicts

To resolve these conflicts, determine which lines you want to keep, and remove the conflict markers and lines of code you don't want. Clean the file so that only the lines of code you want to keep are in it.

For example, to keep the local changes in the above example, remove the conflict markers and delete the lines of code that came from the remote repository.

```sh
Hello. # Your changes and edits
```

Save your file once you've made the edit and resolved the conflict.

In order to complete the merge and get the commit to properly perform, you need to fix all of the merge conflicts. Unfortunately, you do usually have to do this manually, as Github will not know which of the conflicts it should keep. There is a way to force Github to take changes using `git pull --force`... but you almost never want to do this! It will overwrite all of your changes!

## Commit and Push your Changes

Once you have finished resolving conflicts, you can push to your remote repo just as you would any other commit. First `commit` your changes, include a message that you are resolving conflicts in addition to your changes, then `push` them to the remote.

### Read the Docs

It's worth reading the [Github documentation's discussion of how to resolve merge conflicts](https://help.github.com/articles/resolving-a-merge-conflict-on-github/). If you run into any messages you don't understand, you'll want to start here! And then you can turn to Stack Exchange.
