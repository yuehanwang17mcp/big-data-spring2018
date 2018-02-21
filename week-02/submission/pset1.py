#A.1 Create a list containing any 4 strings
lst_a = ['i','love','learning','python']
print (lst_a)
#A.2 Print the 3rd item in the list
print (lst_a[2])
#A.3 Print the 1st and 2nd item in the list using [:] index slicing
print (lst_a[0:2])
#A.4 Add a new string with text “last” to the end of the list and print the list.
lst_a.append ('last')
print (lst_a)
#A.5 Get the list length and print it.
print (len(lst_a))
#A.6 Replace the last item in the list with the string “new” and print
lst_a[4] = 'new'
print (lst_a)


#B.1 Convert the list into a normal sentence with join(), then print
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
print (' '.join(sentence_words))
#B.2 Reverse the order of this list using the .reverse() method, then print
sentence_words.reverse()
print (sentence_words)
#B.3 Now user the .sort() method to sort the list using the default sort order
sentence_words.sort()
print (sentence_words)
#B.4 Perform the same operation using the sorted() function
print (sorted(sentence_words))
# The .sort() method modifies the list in place while the sorted() function
# builds a new sorted list from an iterabel. Besides, .sort() is only defened
# for lists, while sorted() accepts any interable.
#B.5


#C Ramdom Function
from random import randint
def ranum(high,low=0):
    return randint(low, high)
print(ranum(20,9))


#D String Formatting Function
def str_format(n,title):
    return "The number {} bestseller today is: {}".format(n,title)
print(str_format(2,'big data spring 2018'))


# E Password Validation Function
def validate(password):
    numcount = 0
    lettercount = 0
    charcount = 0
    # test password length
    if len(password) < 8 or len(password) > 14:
        return ("your password should be 8-14 characters long")
        # test if password has at least two digits
    for i in password:
        for num in '0123456789':
             if i == num:
                numcount += 1
    if numcount < 2:
        return ("your password should include at least 2 digits")
    # test if password has uppercase letter
    for i in password:
        for upletter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i == upletter:
                lettercount += 1
    if lettercount == 0:
        return ("your password should include at least 1 uppercase letter")
    # test if password has special character
    for i in password:
        for spchar in ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']:
             if i == spchar:
                charcount += 1
    if charcount == 0:
        return ("your password should include at least 1 special character from (!?@#$%^&*()-_=+)")
    # if password passes all of the tests, then it works well
    return ("your password works well")

print(validate("088566382@P"))


#F.1 Exponentiation Function
def exp(num,expo):
    return num**expo
print(exp(5,4))
#F.2 Exponentiation Function using loop
def exp(num,expo):
    a=1
    if expo == 0:
        return 1
    else:
        while expo >= 1:
            a = a*num
            expo = expo-1
        return a
print(exp(5,4))


#G Min and Max Function
def min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(min([9,-79,4,5,7]))

def max(list):
    max = list[0]
    for j in list:
        if j > max:
            max = j
    return max
print(max([9,-79,4,5,7]))
