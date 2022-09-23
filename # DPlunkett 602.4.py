# DPlunkett 602.4
# Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
# lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name, and current
# balance.
# ● Make a series of deposits and withdrawals to test your class.

# %%
class BankAccount:
    def __init__(self, banknm, fnm, lnm, bal=0):
        self.bank_name = banknm
        self.first_name = fnm
        self.last_name = lnm
        self.balance = bal
        
    def deposit(self, amt):
        self.balance += amt
    
    def withdrawal(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print('Error: withdrawal cannot exceed balance')
    
    def __str__(self):
        return 'Account at {} belonging to {} {} has current balance of ${}'.format(
            self.bank_name, self.first_name, self.last_name, self.balance)

accnt=BankAccount('The Bank', 'Joan', 'deArc', 100)        
print('Before:', accnt)  
accnt.deposit(50)
accnt.deposit(51)
accnt.deposit(52)
accnt.withdrawal(10)
accnt.withdrawal(11)
accnt.deposit(53)      
print('After:', accnt) 

# %% [markdown]
# Q2: Create a class Box that has attributes length and width that takes values for length and width upon construction (instantiation via the constructor).
# In addition, create...
# ● A method called render() that prints out to the screen a box made with asterisks of length and width dimensions
# ● A method called invert() that switches length and width with each other
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations
# ● A method called double() that doubles the size of the box. Hint: Pay attention to return value here.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box
# ● A method get_dim() that returns a tuple containing the length and width of the box
# ● A method combine() that takes another box as an argument and increases the length
# and width by the dimensions of the box passed in
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle
# ● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
# box2 and box3 respectively
# ● Print dimension info for each using print_dim()
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
# ● Combine box3 into box1 (i.e. box1.combine())
# ● Double the size of box2
# ● Combine box2 into box1

# %%
import math #for the sqrt function
class Box:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def render(self):
        '''prints a rectangle of *'s of the length and width'''
        for a in range (self.length): #lenth is the # of rows
            for b in range (self.width): #width is the * in each row
                print('*',end='')
            print() #to go to the next line
    
    def invert(self):
        '''swap values of length and width'''
        old_lenth = self.length #need to capture this before changing 
        self.length = self.width
        self.width = old_lenth
        
    def get_area(self):
        '''return area of Box'''
        return self.length*self.width #area = l*w
    
    def get_perimeter(self):
        '''return perimeter of Box'''
        return 2*(self.length+self.width) #perimeter = 2*(l+w)
    
    def double(self):
        '''doubles both length and width'''
        self.length = 2*self.length
        self.width = 2*self.width
    
    def __eq__(self, other):
        return (self.length, self.width) == (other.length, other.width)
    
    def print_dim(self):
        '''prints the dimensions of Box'''
        print('Length is {} and width is {}' 
              .format(self.length, self.width))
        
    def get_dim(self):
        '''returns the dimensions of Box'''
        return [self.length, self.width]
    
    def combine(self, other):
        ''' adds the lengths and the widths of 2 Boxes'''
        self.length += other.length
        self.width += other.width
    
    def get_hypot(self):
        '''sets .hypoth to the sqrt(w^2 + l^2) for a Box'''
        self.hypoth = math.sqrt(self.width**2 + self.length**2)

            
box1 = Box(5,10)
box2 = Box(3,4)
box3 = Box(5,10)
box1.print_dim()
box2.print_dim()
box3.print_dim()
box1 == box2
box1 == box3
box1.combine(box3)
box2.double()
box1.combine(box2)
box1.print_dim()
#testing everything not tested above
box3.render()
box3.invert()
box3.print_dim()
print('area',box3.get_area())
print('permimeter',box3.get_perimeter())
box3.get_hypot()
print(box3.hypoth)
box3.get_dim()


