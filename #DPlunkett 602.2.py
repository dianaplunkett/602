#DPlunkett 602.2
#Q1. What will the following code display?
#Can you debug and fix the output? 
# The code should return the entire list
numbers = [1, 2, 3, 4, 5]
print(numbers[:]) #easiest way to print the entire lilst is to use :

#Q2. Design a program that asks the user to enter a store’s sales 
# for each day of the week. The amounts should be stored in a list. 
# Use a loop to calculate the total sales for the week and display 
# the result.
days_of_w=['M','Tu','W','Th','F','Sa', 'Su']
sales_lst = []
for i in range (0,7):
    print('Enter sales for', days_of_w[i])
    sales_tmp= float(input())
    sales_lst.append(sales_tmp)
total = sum(sales_lst)   
print ('Total Sales for the week: ', total)

#Q3. Create a list with at least 5 places you’d like to travel to. 
# Make sure the list isn’t in alphabetical order
travel_bucket_lst =['Iceland', 'Barcelona', 'Maderia Islands',
                    'Turtle Island, Fiji', 'Istanbul']
#● Print your list in its original order.
print('Unsorted List: ',travel_bucket_lst)
#● Use the sort() function to arrange your list in order and 
# reprint your list.
travel_bucket_lst.sort()
print('Sorted List: ', travel_bucket_lst)
#● Use the sort(reverse=True) and reprint your list.
travel_bucket_lst.sort(reverse=True)
print('Reverse Sorted List: ', travel_bucket_lst)
#Q4. Write a program that creates a dictionary containing course 
#numbers and the room numbers of the rooms where the courses meet. 
#The program should also create a dictionary containing course 
#numbers and the names of the instructors that teach each
#course. After that, the program should let the user enter a 
#course number, then it should display the course’s room number, 
# instructor, and meeting time.
locations = {101:'Rm 1', 102:'Rm 2', 103:'Rm 3'}
instructors = {101:'Ava', 102:'Barbara', 103:'Charlotte'}
#question did not ask to create this, but assume it is needed
times={101:'1pm', 102:'2pm', 103:'3pm'} 
input_course= int(input('Enter Course Number: '))
print('Course', str(input_course), 'is taught by', 
instructors[input_course], 
'in', locations[input_course], 
'at', times[input_course])

#Q5. Write a program that keeps names and email addresses in a 
# dictionary as key-value pairs. 
emails={"Ava":"ava@school.edu", 
"Barbara":"barb@school.edu", 
"Charlotte":"charlotte@school.edu"}
print('Original email data: ', emails)
# The program should then demonstrate the four options:
#● look up a person’s email address,

name= input("Whose email do you need? ")

print('The email is: ', emails[name])
#● add a new name and email address,
emails['Dawn']='dawn@school.edu'
print('Emails with Dawn: ', emails)
#● change an existing email address, and
emails["Barbara"]="barbara@school.edu"
print('Emails with Barbara corrected: ', emails)
#● delete an existing name and email address.
del(emails["Ava"])
print('Emails without Ava: ', emails)