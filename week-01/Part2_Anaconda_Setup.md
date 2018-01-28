
# Anaconda Crash Course: Using Anaconda (“Conda”) to Supplement Python

***

Python is a valuable scripting language for data analysis and management; however managing a Python project environment can be nuanced and tricky. Anaconda is a platform built to complement Python by creating customizable and easily accessible environments in which you can run Python scripts. 

For reference, the Anaconda homepage is found at the following address.

https://www.continuum.io/why-anaconda

The following tutorial runs through the installation of Anaconda, and then introduces you to the concepts behind Anaconda that make it a nice and useful Python development environment.

***

### Install Anaconda (aka Conda)

The Anaconda homepage contains the materials that you need to install Anaconda on your machine. You will primarily be using Anaconda through the command line, so you will have to get comfortable working on the command line. 

## 1. Check Anaconda Version and Install

The first step is to open Terminal and check to see if you have Anaconda installed. If not, we will install it. To check the version, follow the following commands.

#### i. Open Terminal
#### ii. Check Version

The syntax to access Anaconda on the command line is simply ‘conda’. To check the version you have installed, use the following:

```sh
	conda info
```

If you have it installed, you will see platform information, version details, and environment paths after you hit enter, if not, the terminal will not recognize the command.


#### iii. Install Anaconda

To install ‘Conda’, navigate to the Anaconda downloads page at:

[Anaconda Homepage and Downloads](https://www.continuum.io/downloads)

Here, pick your system (Mac/Windows) and the Python version. In our case, we are going to pick Mac and select **version 3.6**. Use the graphical installer, it will provide us a wizard that will step us through the installation process.  Download the installer, double click the package file and follow the instructions. Just a heads up, the installation process takes 5-10 minutes, its a big program, but is straight forward.

If you run into problems installing, or you get an error that states that Anaconda cannot be install in the default location, visit this page for short instructions on how to troubleshoot installation.

[Anaconda Installation Docs](http://docs.continuum.io/anaconda/install#anaconda-install)

Anaconda is contained in one directory, so if you ever need to uninstall Anaconda, use Terminal to remove the entire Anaconda directory using **rm -rf ~/anaconda**.

We used Python 3, not Python 2. The guidelines on the site describe that we should use whichever version we intend to use most often, but ultimately it will not matter that much. Anaconda supports both, and if you ever want to use Python 2, you can create an environment that uses Python 2 and activate it. The main reason you would want to use Python 2 is that Linux distributions and Macs, Python 2.7 is still the default, and because the Python ecosystem has amassed a significant amount of quality software over the years in which some of it does not yet work on 3. Python 3, however, is designed to be more robust and fixes a lot of bugs in Python 2, so in the future, expect to see a continued migration to Python 3. We are set up with Python 3 as our default, but since we are using Anaconda, if we want to set up a Python 2 instance at some point, it will be easy to do!

## 2. Confirm the installation worked properly

Once we are finished with the installation, check to make sure it installed correctly by performing a version check.

```sh
	conda info
```

If you see a 4.X.X version number popup, and with platform and environment information, the installation worked. Now we can begin working with Conda.

***

## 3. The Anaconda 30-minute Test Drive

Now let’s familiarize with what exactly Anaconda allows us to do. On a basic level, Anaconda is a Python distribution that adds many features and streamlines work with the language. It does this by creating specific environments on your machine in which you can specify the packages that are installed and used, and easily lets you toggle between environments. With in the individual environments, you can perform analysis, run scripts, and develop code.

Environments are the bread and butter of Anaconda, because not all Python scripts you run will use the same packages, so you can customize exactly what you need, and create a sandbox that lets you try new things. Your environments will save the packages you have installed, allowing you to easily load an environment and run your scripts.

The Anaconda team has put together a very nice Test Drive that is designed to take about a half hour that will introduce you to concepts around Anaconda, including setting up an environment, toggling between environments, managing the Python version you are using, managing the Python packages you are using in your environments, and finally, removing or uninstall packages and environments if you no longer need them.

Follow the Test Drive at the following link:

[Anaconda 30-minute Test Drive](http://conda.pydata.org/docs/test-drive.html)

Working with Anaconda can make working with Python a much more pleasant experience. For additional resources, including cheatsheets and useful links, see the following materials.

***

## Additional Reading and Resources

#### Conda Command Line Cheatsheet -
http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf

#### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

#### Python Documentation -
https://docs.python.org/3/library/index.html
