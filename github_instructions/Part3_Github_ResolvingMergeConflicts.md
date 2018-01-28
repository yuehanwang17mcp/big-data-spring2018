
# Resolving Merge Conflicts (Command Line)

***

Sometimes, when working on a project, you and your colleagues will change the same line of code. This often happens unintentionally, and you end up with a conflict between two files. No need to panic, simply read the message, and locate what the error might be. If two people change the same line of code, Github will not know which one it should keep, so you have to tell which one, and remove the other.

When this happens, you will see an error similar to the following:

***

```sh
Auto-merging test.txt
CONFLICT (content): Merge conflict in test.txt
Automatic merge failed; fix conflicts and then commit the result.

```

***

What this is saying is that there is a conflict in the file **test.txt**. When we try to pull and there are conflicts, Github will add the conflicts to our file. To fix this conflict, we need to open the file and choose which of the competing lines we want to use.


### 1. Navigate to and Open the File

Navigate to the file with conflicts on your computer and open it up using your favorite text editor (i.e. Sublime Text). We'll make all of the changes that are needed to resolve the conflicts in the text editor.

### 2. Identify the Merge Conflicts

With the file open, locate the merge conflicts. They are signified using **conflict markers**. The conflict markers are signifed by **<<<<<<<**, **=======**, **>>>>>>>**. The **<<<<<<<** signified the start of the conflicted lines and represents the changes on your local machine. It is separated by a **=======** marker, and the **>>>>>>>** marker signals the remote conflict.

Conflicts in the conflicted file will look like the following.

***

```sh
<<<<<<< HEAD # Start of changes made on your local machine

Hello. # Your changes and edits
======= # Comparison marker
Good bye. # Other changes and edits

>>>>>>> ANOTHER BRANCH # End of changes made on the remote repository
```

***

### 3. Edit the File to Resolve Conflicts

To resolve these conflicts, determine which lines you want to keep, and remove the conflict markers and lines of code you don't want. Clean the file so that only the lines of code you want to keep are in it.

For example, to keep the local changes in the above example, remove the conflict markers, and delete the lines of code that came from the remote repository, keeping only the edits you've made.

***

```sh
Hello. # Your changes and edits
```

***

Save your file once you've made the edit and resolved the conflict.

### 4. Fix all of the Merge Conflicts

In order to complete the merge and get the commit to properly perform, you need to fix **all** of the merge conflicts. Unfortunately, often you have to do this manually, as Github will not know which of the conflicts it should keep. There is a way to force Github to take changes using **git pull --force** but you almost never want to do this, it will overwrite all of your changes!

### 5. Commit and Push your Change

Once you have completed resolving conflicts, you can push just as you would any other commit. First **commit** your changes, include a message that you are resolving conflicts in addition to your changes, then **push** them to the remote.

### Read the Docs

Github has nice documentation on merge conflicts, read them at the following:

[https://help.github.com/articles/resolving-a-merge-conflict-on-github/](https://help.github.com/articles/resolving-a-merge-conflict-on-github/)

If you run into any messages you don't understand, don't forget to read the documentation, or search Stack Exchange!
