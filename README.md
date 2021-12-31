# python_course


question 1 : what is wrong with this code?
            room_numbers = {
                    ['Freddie', 'Jen']: 403,
                    ['Ned', 'Keith']: 391,
                    ['Kristin', 'Jazzmyne']: 411,
                    ['Eugene', 'Zach']: 395
                }
 
 
question 2 : What is the first key in dictionary?

question 3  : print all the keys and values in the dictionary separately 
              jp_population_rank = {'3': 'osaka', '1': 'tokyo', '2': 'kanagawa'}
question 4 : give an example of tuple unpacking

question 5: names = ["Garcia", "O'Kelly", "Davis"]
            print something like this using the list above --- # Garcia-O'Kelly-Davis

question 6: eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

          # TODO: Modify this line so it prints the last three elements of the list
 
 question 7 : months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            # TODO: Modify this line so it prints ["July", "August", "September"]
            
 question 8 : write a docstring for the following function
            def readable_timedelta(days):
              # insert your docstring here
              

              weeks = days // 7
              remainder = days % 7
              return "{} week(s) and {} day(s)".format(weeks, remainder)
 
question  9 : write a function to calculate the volume of a cyclinder



###NEW QUESTIONS
## question 1: Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# question 2
Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

## question 3
Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
## question 4
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# TODO 
## question 5
Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

### 2
### 4
### 6
### 8
### 10
### 12
### 14
### 16
### 18
### 20

## question 6
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:
numbers = [12, 75, 150, 180, 145, 525, 50]

## question 7
write a program to calculate the cube of all numbers from 1 to a given number

Given:

input_number = 6


## question 7

Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:
For example: print('Name', 'Is', 'James') will display Name**Is**James


Exercise 1: Reverse a list in Python
Given:
list1 = [100, 200, 300, 400, 500]

Exercise 2 : Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
output ---> ['My', 'name', 'is', 'Kelly']

Exercise 3 : Given a list of numbers. write a program to turn every item of a list into its square.

Given:
numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:
[1, 4, 9, 16, 25, 36, 49]

exercise 4 : Write a program to add item 7000 after 6000 in the following Python List

Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

Eercise 5 : You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
Given:
list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:
[5, 10, 15, 200, 25, 50, 20]

exercise 6 : Get all values from the dictionary and add them to a list but don’t add duplicates
Given:
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:
[47, 52, 44, 53, 54]

exercise 7 : Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method


