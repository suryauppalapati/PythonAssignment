# Question1:a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string.

# Sample String : 'w3resource'
# Expected Result : 'w3ce'

string = "w3resource"
splice_front=string[0:2]
splice_back=string[-2:]
spliced= splice_front + splice_back
print(spliced)


# Sample String : 'w3'
# Expected Result : 'w3w3'

string = "w3"
splice_front=string[0:2]
splice_back=string[-2:]
spliced= splice_front + splice_back
print(spliced)

# Sample String : 'w'
# Expected Result : Empty String

string = "w"
if(len(string)<=1):
    print('Empty String')
else:
    splice_front=string[0:2]
    splice_back=string[-2:]
    spliced= splice_front + splice_back
    print(spliced)

###########################################################################################################


# OPERATORS

# 1] Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math
r = float(input("enter no: "))
area = math.pi * r * r
print(area) 

# 2] Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

a= int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# 3] Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9

from datetime import date
d1 = date(2014, 7, 2 )
d2 = date(2014, 7, 11 )
difference = d2 - d1
print(difference.days)

###########################################################################################################


# Decision Control:

# 1] Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# if the given string already begins with "Is" then return the string unchanged.

string = "Fact"
checker = string.find("is")
if(checker == -1):
    print("is" + string)
else:
    print(string)
    
# 2] Write a Python program to
# find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

number = int(input("enter a num: "))
if(number%2==0):
    print("entered num is an even number")
else:
    print("entered number is an odd number")


# 3] Write a Python program to test whether a passed letter is a vowel or not.

element = input("enter an vowel: ")
vowels = ['a', 'e', 'i', 'o', 'u']
if element in vowels:
    print("entered element is an vowel")
else:
    print("entered element is not an vowel")

###########################################################################################################


# LOOPS:

# 1] Write a Python program to concatenate all elements in a list into a string and return it.

list = ['a', 'e', 'i', 'o', 'u']
string = ''
for i in list:
    string= string + i
print(string)

# 2] Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# Test Data :

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output : {'Black', 'White'}

set1 = set(["White", "Black", "Red"])
set2 = set(["Red", "Green"])
print(set1.difference(set2))

###########################################################################################################


# Functions:

# 1] Write a function in a Python program to compute the greatest common divisor (GCD) of two positive integers

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(10,5))

# 2] Write a Python function which accepts two arguments x and y and returns (x + y) * (x + y).

# Test Data : x = 4, y = 3

# Expected Output : (4 + 3) ^ 2) = 49

def fun(x,y):
    result = (x + y) * (x + y)
    return result
print(fun(4,3))

###########################################################################################################

# Variable scoping
# 1] Given the below code snippet, answer the following questions.

# def num_square(num):
# square = num * num
# return square
# input_num = 121
# if input_num > 100:
# result = num_square(5)
# print(result)


# (I) What is the scope of num, square, input_num, result?

              #ANSWER
        # scope of num : LOCAL SCOPE
        # scope of square: LOCAL SCOPE
        # scope of input : GLOBAL SCOPE
        # scope of result : GLOBAL SCOPE

# (II) What is the lifetime of each variable? When will they be created and destroyed?

                                    #ANSWER
# Variables have a life from the start of the execution of the function to the end of execution 
# i.e. the end of the function or the return statement. variables are created at the time of object creation 
# and will be destroyed when it goes for Garbage collection.


# (III )What would happen if input_num had a value of less than 100?

                                 #ANSWER
                        # 'result' is not defined


# (IV) What would be the scope and value of result if input_num has a value of less than 100?

                    #ANSWER - LOCAL SCOPE

######################################################################################################

# Classes and OOP

# 1] Create a class called Country
# which has a single class attribute called AVG_POPULATION.
# Set it to some default value.
# The constructor takes the parameters country_name and country_code.
# The constructor must check that country_name and country_code are strings. If not it must throw a ValueError.
# The constructor must check if the country code is exactly 3 letters long. If not it must throw a ValueError.

class Country:
    avg_population = 5000
    def __init__(self, country_name, country_code):
        try:
            if type(country_name) == str and type(country_code) == str and len(country_code)==3:
                self.country_name=country_name
                self.country_code = country_code  
            else:
                raise ValueError('enter a string')
        except ValueError :
            print("Please Enter the proper value")  

# Write a method called country_short_form() which takes the country_name as a parameter 
# and returns the first 2 letters of the country name in uppercase. 
# Suitable validations must be done for the method.

    def country_short_form(self, country_name):
        two_letters = country_name[0:2]
        return two_letters

# Write a class method called is_densly_populated(), 
# which takes a single parameter population and returns true if the population is greater than 
# AVG_POPULATION otherwise false. Suitable validations must be done for the method.

@classmethod
def is_densly_populated(cls,population):
    if (type(population)== int):
      if(population > cls.AVG_POPULATION):
        return True
      else:
        return False
    else:
      print("please enter the numeric value")

# Write a method called formatted_country_name which returns a string containing the country_name 
# ( country_code) [ ex - India ( IND) ]. Make this method into a property using decorators, 
# and write a getter, setter, and a deleter for manipulating the values of country_name and country_code. 
# Suitable validations must be done for the method.

@staticmethod
def world_avg_population(array):
    try:
      if(len(array)>0):
        sum=0
        for i in array:
          sum=sum+i
        return (sum/len(array))
      else:
        print("Enter appropriate array")
    except:
      print("Enter the list of integer values")
  
@property
def formatted_country_name(self):
    return "{0} ( {1} )".format(self.country_name,self.country_code)
  
#Getters
def get_country_name(self):
    return self.country_name
def get_country_code(self):
    return self.country_code
  #setters
def set_country_name(self,country_name):
    try:
      if type(country_name) == str:
        self.country_name=country_name
      else:
        raise ValueError('Enter a string.')
    except ValueError :
      print("Please provide the string value")
  
def set_country_code(self,country_code):
    try:
      if type(country_code) == str and len(country_code)==3:
        self.country_code=country_code
      else:
        raise ValueError('Enter a string.')
    except ValueError :
      print("Please Enter the proper value")
  #deleters
def del_country_name(self):
    print("Deleted country_name property")
    del self.country_name
def del_country_code(self):
    print("Deleted country_code property")
    del self.country_code


# 2] Create a base class
# Shapes. It must have 2 suitable instance variables and 2 suitable methods.

# Create 2 child class of
# Shapes. For example Triangle and Quadrilateral. They must inherit the Shapes class and override 1 variable and 1 method. They must have 1 additional attribute and
# method.

# Create 1 child class each of
# the above Triangle & Quadrilateral. They must override 1 method and have 2 additional attributes and 1 additional method.

# Your program must
# instantiate the lowest child classes and print all attributes and methods of the class and all inherited attributes and methods as well. Suitable error handling must be done for
# all methods.



import math
class Shape:
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
    def get_length(self):
        return self.__length
    def set_length(self, length):
        self.__length = length
    def get_breadth(self):
        return self.__breadth
    def set_breadth(self, breadth):
        self.__breadth = breadth
    def get_area(self):
        return self.__length * self.__breadth
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def get_area(self):
        return math.pi * self.__radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
r1 = Rectangle(10.5, 2.5)
print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
c1 = Circle(12)
print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())


##########################################################################################################


# Exception Handling

# 1] Write a function that raises
# 5 built in python exceptions without using the raise key word and
# print appropriate messages for each exception.

# KeyboarInterrupt Exception
try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
#ZeroDivisionError
try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")
#Attribute Error
class Attributes(object):
    a = 2
    print (a)
try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")

#lookup Error
try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
else:  
    print ("Success, no error!")

#NameError
try:
    print(ans)
except NameError:  
    print ("NameError: name 'ans' is not defined")
else:  
    print ("Success, no error!")


#  Create 4 custom exception
# classes that inherit from the exception class. Your function must take a person object as an input. 
# Raise an exception for the following cases: invalid name, invalid age, invalid
# email, invalid phone number. Write appropriate messages for each exception. 
# If no exception has occurred, only then add the object to a global array of persons.

class Person:
  def __init__(self, name, age,email,phone):
    self.name = name
    self.age = age
    self.email=email
    self.phone=phone
p1 = Person("John", 36,"john@gmail.com","9920987620")
import re
class NameException(Exception,p1):
    try:
        regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
        res = regex_name.search(p1.name)
        if res:
            print("Valid")
    except:
        print("Invalid Name")

#############################################################################################################

#Regular_Expressions


# 1] Create a function that
# takes a date string as an input and checks if it is of the format Month date, year. 
# The month must be the full month name and date must have 0 padding (01) and year must have full
# year. Example June 03, 2007
# If the date is not valid the
# function must return false otherwise true.

import re
date="June 03,2007"
pattern=(('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\.)?(\w*)?(\.)?(\s*\d{0,2}\s*),(\s*\d{4})', re.S + re.I).findall('Some wrong date is September 28, 2002date') + ['n/a'])[0]
res=re.match(pattern,date)
if res:
    print("true")
else:
    print("false")


#2] Create a function that
# checks if a number is a valid credit card number. If not it must return false otherwise true. 

# The following are the conditions.
# It must start with a 3, 4 or 9.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It must have digits in groups of 4, separated by one hyphen "-".
# It must NOT have 2 or more consecutive repeated digits.

raw_input = input("enter card no.")
total_count = int(raw_input())
numbers_list = []

#Condition1 refernece list to check the starting series
start_list = [3,4,9]

for count in range(total_count):
    numbers_list.append(raw_input())

#condition 2, validates the length of the number
def val_len(num):
    check = num
    check2 = True
    if "-" in num:
        check = "".join(num.split("-"))
        check2 = val_group(num)

    if ((len(check) == 16) and check2): #is16Digits
        return True
    else:
        return False

#condition 3, validates the starting series
def val_start(num):
    if int(num[0]) in start_list:
        return True
    else:
        return False

#condition 5 It must have digits in groups of 4, separated by one hyphen "-".
def val_group(num):
    for val in num.split("-"):
        if len(val) != 4:
            return False
    return True

#condition 5, validates the repetition of any number for 2 consective times
def val_rep(num):
    res = ""
    for i in range(0, 2):
        try:
            if (res[i] == res[i+1]):
                if (res[i+1] == res[i+2]):
                    if (res[i+2] == res[i+3]):
                        return False
        except IndexError:
           pass
    return True

Decorators


# 1] Write a decorator
# function_timer that times the execution of any function it is attached to and 
# print the time taken after the function execution ends.

import timeit
def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()
@timer
def addition():
  total = 0
  for i in range(0,1000000):
    total += i
  return total

###############################################################################################################

# Modules

# 1] Import the math module
# and call the sin function.

  import math   
a = math.pi / 6
print ("The value of sine of pi / 6 is : ", end ="") 
print (math.sin(a))

# 2] Create your own module
# City having 3 functions suitable functions.

import city
city.city_name("Mumbai")
city.city_code("401107")

###########################################################################################################

# Packages

# 1] Import any 1 python
# built-in package and use 1 module and 3 functions within it.

import json

# convertim python object into json object
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print(json.dumps(student))

#converts python sring to json string
string1 = 'Python and JSON'
print(json.dumps(string1))

# Serializing JSON and writing JSON file
details = {
        "name": "Felix Maina",
        "years": 21,
        "school": "Makerere"
}
with open("details.json", "w") as file_object:
    print(json.dump(details, file_object))



# 2] Create a custom python
# package Animals which would have 3 modules within them and each module must contain 2 functions

import Animal.appearance, Animal.habitat
Animal.appearance.eye_color()
Animal.appearance.color()
Animal.habitat.type()
Animal.habitat.kingdom()

#######################################################################################################

# File Handling

# 1] Create sample data. Write
# this sample data to a new text file. Read the sample data from the text file, append some new data, and write it back to the text file. The text file must contain both the
# previous data as well as the updated one.

f=open("file.txt","w")
f.write("This is the write command")
f=open("file.txt","a")
f.write("Add new line ")
f=open("file.txt","r")
print(f.read())


# 2] Create a sample.csv file,
# read the CSV file, and print each row to stdout. Add another column to the CSV and update the CSV file. 
# Again read the updated CSV file and print each row.

import csv
filename = "addresses.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))
  
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col),
    print('\n')
#write operation
rows=[['peter','skstone','PD','202025']]
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
for row in rows[:5]:
    for col in row:
        print("%10s"%col),
    print('\n')











