#Diana Plunkett
#DATA 602 
#Sept 5, 2022

#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = int(input('Enter the score for test 1: ')) #modified input lines to convert the input value to int
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) #this line, asking for test3 to be entered, was missing
# Calculate the average test score.
average = (test1 + test2 + test3) / 3  #needed parens around the addition
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: #the variable HIGH_SCORE should be in caps, as it was when set to 95
    print('Congratulations!')
    print('That is a great average!')  #needed to indent so this is part of the if stmt

#Q2
#The area of a rectangle is the rectangle’s length times its width. 
# Write a program that 
# asks for the length and width of two rectangles and prints to 
# the user the area of both 
# rectangles. 

for x in range(2):  # loop to ask for length and width for 2 rectangles
    print ("For rectangle ", x+1)  #since x starts at 0, we add 1 to get counting numbers. 
    #get the dimensions 
    length = int(input('Enter the length of the rectangle: '))
    width = int(input('Enter the width of rectangle: '))
    print ("The area of rectangle", x+1, "is", length*width)
    
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name 
# and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along 
# the lines of:
# "Happy birthday, name!  You are age years old today!"
#get name and age
Fname = input('Enter your first name: ')
age = int(input('Enter your age: '))
#in the print, put desired spaces in the "" and use sep="" so there is no space btwn Fname and ! 
print ("Happy Birthday, ", Fname, "! You are ", age," years old today!", sep="")
