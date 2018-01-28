
# Problem Set 1: Intro to Python
This problem set is meant to create a good foundation of programming. We emphasize code readability and reusability over performance. Code performance can be measured in many different ways, and is by no means the focus of this course, however, we expect your code to be non-repetitive, clean, and efficient enough to deal with medium-to-large datasets. As we move forward with the course, you will be introduced to some functional programming techniques, iterators, and objects that will help speed-up the data munging of the type of data sets that we will be dealing with. 

`Throughout the course you will be using multiple online resources to help you solve the assignments, we do too. However, if you are using other people’s code, make sure to credit the source, and come up with your own implementation. In this problem set, you are welcome to refer to online resources and documentation. One of the primary ones you will find you use is:` [Stack Overflow]( http://stackoverflow.com/).

## 1. Lists
Do the following:
1. Create a list containing any 4 strings.
2. Print the 3rd item in the list
3. Print the 1st and 2nd item in the list using [:] index slicing.
4. Add a new string with text “last” to the end of the list and print the list.
5. Get the list length and print it.
6. Replace the last item in the list with the string “new” and print


## 2. Strings 
Given the following list of words:
```Python
list1=['I', 'am', 'learning','Python','to','munge','large','datasets','and','visualize','them']
```
1. Convert the list into a normal sentence with [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join), then print.
2. [**Reverse**](https://docs.python.org/3.6/tutorial/datastructures.html) the order of this list `[“them”,”visualize”,…]`
3. Now [**sort**](https://docs.python.org/3/library/functions.html#sorted) the list using the default sort order in python
4. Modify the sort to do a case [**insensitive**](http://matthiaseisen.com/pp/patterns/p0005/) alphabetic sort
5. Now print the list in reverse alphabetic sort order


## 3. Random Function
Here is a python snippet for generating a random integer:

```Python
import random
# this returns random integer: 100 <= number <= 1000 
num = random.randint(100, 1000)
```

* Implement your own random function that builds on this python function, returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).

* Test your function by adding the following 2 assert statements to your file (replace myrandom and low with the names you used). The [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement helps you debug, by testing if a statement is true. 

```Python
assert(0 <= myrandom(100) <= 100)
assert(50 <= myrandom(100,low=50) <= 100)
```


1. Inputs: 
  1. Two `integers` that will be used as lower and upper bounds of the function. 
2. Outputs: 
  1. A random number within the established bounds. 

## 4. String Formatting Function 
Write a function that expects 2 inputs from the command line. The first is a title that may be multiple words, the second is a number. Given these inputs print the following string (replacing N and Title with the dynamic values passed in to the script each time it runs).

`The number N bestseller today is: Title` 

* If not already title-cased, the function should **title-case** the string. 
* Build one function making the first input optional (keeping the 2nd required).
* Build another function making the second input optional (keeping the 1st required).
* Build a third function making both inputs optional.


## 5. Password Validation Function 
Write a password validation function. Ask the user to input a password that meets the criteria listed below. You can either use the **Python** [`input`](https://docs.python.org/3/library/functions.html#input) built-in function, or just pass the password as a function argument. Validate that the user’s password matches this criteria. After 3 bad tries, quit with an error message. If password is valid, print a helpful success message.

* password length must be 8-14 characters
* password must contain at least 2 digits
* password must contain at least 1 uppercase letter
* password must contain at least 1 special character from this set !@#$%^&*()-_+=



1. Inputs: 
  1. A `string` that will be tested for the password requirements. The string can be passed as an argument to the function, or as an input through the `input` function.
2. Outputs: 
  1. A **success** message if the password works, otherwise an **error** message. 


## 6. Exponentiation Function
Create a function called **exp** that asks for two digits and then prints an exponentiation, without using the exponentiation operator (`**`). You may assume these are positive integers. Use at least one custom-defined function.

For example, some outputs of this function could be:
* 2 , 3 => 8
* 5 , 4 => 625

1. Inputs: 
  1. An `integer` that will be recursively multiplied
  2. An `integer` that will define the number of times to multiply the number to get the exponentiation.
2. Outputs: 
  1. An `integer` that is the result of the exponentiation. 

`Hint: You can recursively multiply a number. The second number defines the number of times the recursive loop happens. Every time the loop happens, you can redefine the variable that gets multiplied.` 

## 7. Min and Max Functions (Bonus)

EXTRA CREDIT

Write your own versions of the Python built-in functions **min** and **max**. They should take a list as an argument and return the minimum or maximum element. Assume lists contain numeric items only. 

1. Inputs: 
  1. A `list` of `numbers` to be tested. 
2. Outputs: 
  1. A `number` of the list that is the maximum or minimum. 

`Hint: Pick the first element as the minimum(maximum) and then loop through the elements to find a smaller(larger) element. Each time you find a smaller (larger) element, update your minimum (maximum).`

## 8. Hangman Game (Bonus)

EXTRA CREDIT

Implement a basic hangman game through functions.
* Show a user the word or phrase (5-15 letters) that they have to guess with dashes as placeholders for unsolved letters. You can hardcode this word into your source.
* Prompt the user to guess a letter or solve the puzzle through the user [`input`](https://docs.python.org/3/library/functions.html#input) function. They get up to 8 guesses. After each guess, show the word with any instances of correctly guessed letters filled in. Show the number of tries left. Handle possible issues with user input in a consistent way.
* Continue to prompt the user until either they’ve used up their 8 guesses or solved.
* If they solve the puzzle in time, show the completed word and a congratulatory message.
* If they fail to solve the puzzle, show the completed word and a Game Over message.


Here’s a sample transcript.
> You have 8 guesses to solve this word. 

>------------------------------------------   

>guess a letter or solve: b 

>b--b--b--  (7 tries left) 

>guess a letter or solve: x 

>b--b--b--  (6 tries left) 

>guess a letter or solve: e 

>b--b-ebee  (5 tries left) 

>guess a letter or solve: bumblebee 

>bumblebee  (4 tries left) 

>Congratulations, you won!

1. Inputs: 
  1. A `string` that will be tested to see whether or not it is part of the secret word. 
2. Outputs: 
  1. A message that shows the user the number of guessed letters at the time.
  2. A **success** message if the user wins, otherwise a **try again** message. 

