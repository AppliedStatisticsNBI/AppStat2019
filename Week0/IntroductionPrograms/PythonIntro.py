
# coding: utf-8

# # Introduction to Python
# 
# ***   
# ### Authors: 
# - Christian Michelsen (Niels Bohr Institute)
# - Troels C. Petersen (Niels Bohr Institute)
# 
# ### Date:    
# - 24-09-2018 (latest update)
# ***
# 
# This is a Jupyter notebook. This is a smart and easy way to run Python-code interactively in the browser. The term *interactively* means that we at any time can stop the process and see the individual outputs, change variable expressions or plot the intermediate results. This notebook is run on ERDA which means that you do not have to have Python installed on your own computer to run the files, although we recommend also having a local installation up and running. 
# 
# ***
# 
# This notebook is meant as a very basic introduction to Python. It introduces how to load packages, declare variables, print output, how to use lists, strings, numpy arrays, and different kinds of loops. Finally it also shows how to define and use functions and how to load and save files. 
# 
# ***
# 
# In the section below, we tell Python which modules it should load. 

# In[1]:


import numpy as np


# You can now access the functionality of e.g. numpy by `np.sqrt(number)` to get the square root etc. You can see some of Numpy's mathematical functions __[here](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html)__.

# ## Variable declaration
# 
# Below we show how to declare integers and floats:

# In[2]:


# Declare an integer
myint = 1


# In[3]:


# Declare a float
myfloat = 1.0


# Notice the difference in the declaration. Be carefull of the difference. Also notice that you can add comments in Python by using `#`.   
# One common error is if you want to compare your variables to a number: `myint == 1` Is true no matter what. `myfloat == 1.0` could be true. `myfloat` is a number with ??? digits, it could be either 0.9999999999999999999998 or 1.000000000000000001.  
# 
# Below some simple rules: 

# In[4]:


another_float = myint * 2.0        # int comined with float gives float
another_float


# In[5]:


another_int   = int(myfloat + 0.5) # Rounding floats to int
                                   # When rounding, you will always get the closest int lower
                                   # than the float. Thus if you add 0.5 before rounding, you
                                   # will always get the closest int to the original float
another_int


# One important operater you will use from time to time is the modulus operator `%`.
# `a % b` returns the remainder when deviding the integer `a` with the integer `b`.  
# So if you wish to find out if 9312312 is divisible by 17, you can check this
# by asking if 93112312 % 17 is zero. More on this below.
# 
# ## Strings:

# Of course Python can also handle letters in addition to just numbers. These are called strings. We will not go too much into depth with strings right now. 

# In[6]:


# Strings
mystring = "This is a string"      # Use strings to store strings of letters
mystring


# ## Printing output
# 
# You can use the print statement to print the output of your script:

# In[7]:


print("This is an int", myint)
print("This is a float", myfloat)
print(mystring)


# In Jupyter notebooks you can also just simply type the variable name to see its value:

# In[8]:


myint


# The print-method works more generally and allows us to also write a description (string) together with the variable which makes the reading of the output easier.

# In[9]:


print("This is an int", another_int, ". This is a float", another_float)


# This way of writing quickly becomes difficult to customize to ones specific needs. Therefore Python also comes with more advances string formatting options. The newest and preferable way of writing modern Python strings are with so-called f-strings. They work in the following way:

# In[10]:


string = f'This is an int {another_int}. This is a float {another_float}'
print(string)


# Notice that Python accepts both `'` and `"` as quotes (but you have to finish the quote with the same symbol as you started it with).   
# First of all f-strings (named so due to the `f` before the the actual string) are easy to read since you can simply input the variable name in the string by using `{}` brackets. f-strings also allows further customization by using `:` as a string formatter: 

# In[11]:


string = f'This is an int {another_int:2d}. This is a float {another_float:7.3f}'
print(string)


# Can you see what happened here?  
# 
# 
# For the integer why specify that it is a single digit using `d`. The `2d` then means that the width in the string should be 2 characters, therefore introducing the space in from of the 1. This is useful if you are counting to e.g. 15 and want the spacing to be the same (do not worry about the structure of the code here, we will return to loops below): 
# 

# In[12]:


for i in range(1, 15+1):
    print(f'This is an int {i:2d}')


# Looking back at the float above we first of all use the float formatter `f`. `7.3f` then means that it should have a width of 7 spaces and 3 digits after the decimal point. It is printed as `__2.000` (where `_` should be a space).  The space in front of the float in the string is then 1 because 7 (width) - 3 (the "`000`") - 1 (the "`2`") - 1 (the "`.`") = 1 space left.  
# 
# For completeness we show below the two older, and still valid, ways of writing the same expression:

# In[13]:


string_percentsign = "This is an int %2d, This is a float %7.3f" % (another_int, another_float)
string_format = "This is an int {0:2d}, This is a float {1:7.3f}".format(another_int, another_float)
string_f = f'This is an int {another_int:2d}. This is a float {another_float:7.3f}'

print(string_percentsign)
print(string_format)
print(string_f)


# Of course you can also include line breaks and tabulate parts of a string. This is done using `\n` for new line and `\t`for tabulation:

# In[14]:


print("Line \n new line starts here \t and is tabulated") 
print("") # Print an empty line

string = f'This is an int \t\t{another_int}. \nThis is a float \t{another_float}'
print(string)


# Notice that you have to write `\nNew Text Here` and not `\n New Text Here` unless you want to start the new line with a space. 

# ## Lists 

# Often you want to store a large number of variables together, intead of having to declare them one by one.  
# The list offers a simple way of organising these:

# In[15]:


simplelist = [0.0, 0.0, 0.0, 0.0, 0.0]   # List of 5 floating point zeros
simplelist[2] = 13.0   # Assign the '2' entry to 13.0.
simplelist


# NOTE: As in most modern programming languages, you count from zero, which is why it is the third element that is now 13.0 and not the second. For a short argument as to why this is, see https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html, and for a short description its history in Python, see https://python-history.blogspot.com/2013/10/why-python-uses-0-based-indexing.html.   
# 
# We can of course also append new numbers to the list (as lists are mutable):

# In[16]:


simplelist.append(1.0) 
simplelist.append(5.0)
simplelist.append(3.0)
simplelist


# One good thing to remember with Python lists is that they are cyclical, which means
# you can also access the numbers in the following way:

# ```Entry number:  -8   -7   -6   -5   -4   -3   -2   -1 ```  
# ```simplelist = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 5.0, 3.0]``` 

# The reason this is smart is that if you use the append function and want to access the last appended value, you can use `simplelist[-1]` instead of `simplelist[len(simplelist)-1]`, where `len(list)` is the function that gives you the length of a list.

# A lot of times it is cumbersome to declare each entry in the list by hand.
# If it is for instance necessary to store 100 numbers in your analysis, you can declare a list to contain them in the following way (if you are a Python
# expert you probably know 10 other ways of doing this).

# In[17]:


alotofzeros = [0.0]*100
alotofzeros


# In case you want to have have a list of only numbers, you can take advantage of a 
# Numpy array. These are more similar to Matlab lists in a lot of ways.

# In[18]:


numpyarray = np.array([0., 21., 10., -4., 1/5.])


# Numpy arrays allow you to do the following:

# In[19]:


numpyarray_2 = numpyarray + 1
numpyarray_2


# In[20]:


numpyarray_3 = numpyarray*12.4
numpyarray_3


# Numpy also has a lot of convience functions for creating specific types of arrays. For example if you want to create an array numbers from 0 to 4 (the first 5 numbers), this is called a range:

# In[21]:


numpyrange = np.arange(5)
numpyrange


# Another type of array needed could be the evenly spaced ranges from 0 to 5 in 10 intervals:

# In[22]:


numpylinspace = np.linspace(0, 5, 10+1) # can you see why we need a +1 here?
numpylinspace


# We can also initialize an empty list of zeros (or ones):

# In[23]:


numpyzeros = np.zeros(10000)
numpyzeros


# In[24]:


numpyones = np.ones(10000)
numpyones


# We can of course print both normal Python lists and Numpy arrays:

# In[25]:


print("My simple list    : ", simplelist) 
print("Which has         : ", len(simplelist), "Entries")
print("The first entry is: ", simplelist[1])
print("The last entry is : ", simplelist[-1], simplelist[len(simplelist)-1])
print("") 
print("A large list: ", alotofzeros)    # Not so nice output, will be adressed below.
print("")
print("A numpy array                :", numpyarray)   
print("A numpy range                :", numpyrange)   
print("A numpy linearly spaced range:", numpylinspace)   
print("An array of zeroes           :", numpyzeros)   
print("")


# A great strenght of the python list is that you can store just about everything you want to
# in them. Say if you want to store a name and a score for some persons : 

# In[26]:


mixedlist = [ ["Max"  ,  7 ] , # This is a list of lists, each containing a string and an integer 
              ["John" ,  12] , 
              ["Nick" , -3 ] ,
              ["Niels",  10] ]
mixedlist


# If you want to sort by score you can use the sorting function: 

# In[27]:


sortedlist = sorted(mixedlist, key=lambda column: column[1])
sortedlist


# This is a bit more advanced since, you have to tell Python that it should sort it by the 'second entry' in each list (i.e. column 1)
# If you only have a list with numbers `thelist = [0, -214, 35, 12, 343, 1224]`, you can simply use `sorted(thelist)` or `thelist.sort()`.
# 
# If instead you wanted to sort by name and not score (i.e. the first column), you would do:

# In[28]:


sortedlist_v2 = sorted( mixedlist, key=lambda column : column[0])
sortedlist_v2


# The printed output is not very nice/readable, but more on that just below!

# ## Looping and logical statemants

# A lot of times you want to repeat a calculation with some different initial parameters
# which is where the loop comes in handy:

# In[29]:


# This is a simple loop
for i in range(10) : 
    # This is the block within the loop
    print(f"Counting to ten: {i}")


# This will tell the intepreter that it should make a list with the numbers 0, ..., 9.  
# For each of these numbers, it will assign `i` to the given value and perform whatever is inside the 'loop block' with that specific value of `i`.  
# 
# If you want to "control" the loop range more, options are:

# In[30]:


for i in range(4, 10): 
    print(f"Counting from four to ten: {i}")
for i in range(4, 10, 2):
    print(f"Counting every second number from four to ten: {i}")


# Notice that Python uses half-open intervals and thus does not include the end point the range.  
# 
# In addition to the `range` method of looping, Python also allows us to loop over a list directly:

# In[31]:


for val in simplelist:
    print(val)


# In case we need both the index and the value of a list, we can use `enumerate`:

# In[32]:


for index, val in enumerate(simplelist):
    print(f'index: {index}, value: {val}')


# We can now return to how you can print list more nicely:

# In[33]:


for name, score in mixedlist :
    print(f'Name: {name} \t -> \t Score: {score:3d}')


# Even though `mixedlist` contains both name and score, we can still use `enumerate` to get the index:

# In[34]:


for index, (name, score) in enumerate(mixedlist):
    print(f'Counter: {index} \t Name: {name} \t -> \t Score: {score:3d}')


# ## A note on programming blocks

# As is the case with programming, you will structure your code as blocks:

# ```
# statement1 : 
#     
#     This is coding block1
# 
#     statement2 : 
#        
#         This is the coding block2
# 
#         ...
#    
# ```

# Note that all the variables you declare in statement2 is only known in coding block2, but everything you define in statement1 is also known in statement2.  
# Most programming languages you have probably seen incloses the statements with brackets or curly braces. In Python this is done solely by indention 
# (The recommeded pratice is to use four __[spaces](https://www.python.org/dev/peps/pep-0008/?#tabs-or-spaces)__. This means that the interpreter knows where e.g. coding block2 is (8 spaces) and when it stops (when you are back
# to 4 spaces).  
# 
# To learn more about the Python development team's stance on braces, try to import: `from __future__ import braces`.

# ## Back to looping and logical statemants
# 
# To compare values, you can use the if statement:

# In[35]:


anint   = 3
afloat  = 314.0
astring = "string"

if anint == 3: 
    print("The integer value is three ")


# Notice that when making boolean comparisons you use double equal signs, `==` and not single (which is used for assigment). In addition to `if` there is also `elif` (else if) and `else`:

# In[36]:


if afloat > 1000.0: 
    print("The float value is greater than 1000")
elif 100.0 < afloat < 500.0: 
    print("The float value is somewhere between 100. and 500.")
else: 
    print("The float is neither > 1000 nor in the range [100,500]")


# The negation comparison is `!=`:

# In[37]:


if astring == "string": 
    print("'astring' says", astring)

if astring != "blah": 
    print("'astring' does not say 'blah'")    


# One very nice thing with python is that you can combine lists, for loops and if statements in an intuitive way.  
# If you e.g. want a list containing the first 20 square numbers, you can use what is called a list comprehension: 

# In[38]:


sqrnumbers = [i*i for i in range(10)]
sqrnumbers


# In[39]:


for i in sqrnumbers:
    print(f"This is a square number {i}")


# If you only want the even square numbers, you can use the modulus operator (`%`):

# In[40]:


evensqrnumbers = [i*i for i in range(10) if i%2 == 0]
evensqrnumbers


# In[41]:


for i in evensqrnumbers :
    print(f"This is an even square number {i}")
print("")


# Another form of loop is the while statement:

# In[42]:


whilevar = 0.0
while (np.tan(whilevar) < 1000.0): 
    whilevar += 3.1415926535897932385 / 10000
#    whilevar += np.pi / 10000

print(f"{whilevar:6.3f} is the first value whose tangent is greater than 1000 ({np.tan(whilevar):8.3f}) (in steps of pi/10000). ")


# Above while loop test weather `tan(whilevar)` is less than 1000. If it is greater than 1000 it will exit the loop.   
# In the block inside the loop it will increment `whilevar` with pi/10000 and run the test again.
# 
# Notice also that you can have whole expressions in f-strings, `{np.tan(whilevar)}`. 

# ## Random numbers

# To generate some randoms numbers, we will use the numpys class random, which is both
# very efficient, and produces high quality random numbers (think about what that means!).

# In[43]:


# Get the object from the numpy random module
r = np.random
r.seed(42) 


# If you don't set any value you get a new (series of) random number(s) every time you run.  
# With a specified seed, you get the same (series of) random number(s).  
# 
# Print some random numbers uniformely distributed between 0 and 1:

# In[44]:


for i in range(10): 
    print(f"This is a uniformly generated number: {r.uniform()}")   # Calls the uniform function


# See the behaviour of setting a specific seed:

# In[45]:


r.seed(42)
for i in range(10): 
    print(f"This is a uniformly generated number: {r.uniform()}")   # Calls the uniform function


# Create some lists/arrays containing 1000 uniformly distributed random numbers:

# In[46]:


uni_list = [r.uniform() for i in range(1000)] 
uni_array = r.uniform(size=1000)

print(uni_list[:10])
print("")
print(uni_array[:10])


# Above we have shown how to create the random numbers in two ways. The first is by using list comprehension and is thus a normal Python list.  
# The other is by using Numpy directly, which is both simpler to write and computationally more efficient.   
# 
# 
# In addition to creating uniform numbers we can also create normally (Gaussianly) distributed random numbers:

# In[47]:


# List with 1000 unit normally (Gaussianly) distributed random numbers:
gauss_array = r.normal(0.0, 1.0, 1000)
print(gauss_array[:10])


# Where `0` is the mean, `1` is the standard deviation and `1000` is the number of random numbers created. 
# 
# Print a couple of numbers from the list:

# In[48]:


for single_uni, single_gauss in zip(uni_array[:10], gauss_array[:10]): 
    print(f"Uniform number {single_uni:5.3f} \t Gaussian number {single_gauss:+5.3f}")


# Here we have introduced 2 new things:
# 
# 1. the `zip` operator. This allows us to loop over two (or more!) lists, arrays or anything else that can be iterated over. Here we iterate over the first 10 elements of `uni_array` and `gauss_array`. Doing it this ways allows us to not have to use index notation, `uni_array[i]` and `gauss_array[i]`, but instead using the variables `single_uni` and `single_gauss`.
# 
# 2. the `+` in our string formatter in the f-string. This simply shows the sign of the number (in this case a float) which make the output aling out nicely when printed. Another way of doing this would simply to use: `{single_gauss:6.3f}` which would then leave a space instead of a plus.

# ## Functions

# To define a function, use the following structure
# 
# ```
# def(input):
#     ...  
#     function block   
#     ...   
#     return value
# ```
# 
# 
# Normally, it is good pratice to put this in the beginning of your script, but can be done anywhere, and for the sake of readability we will just do
# it here in this case. 
# 
# Define a function that returns the square of a number:

# In[49]:


def sqr(a): 
    return a**2 # or a*a


# Print the square of some of your random numbers: 

# In[50]:


for single_uni, single_gauss in zip(uni_array[:10], gauss_array[:10]): 
    print(f"Uniform: {single_uni:5.3f}^2 = {sqr(single_uni):5.3f} \t Gaussian: {single_gauss:6.3f}^2 = {sqr(single_gauss):5.3f}")


# Define a more complicated function that calculates the mean and RMS of the values in a list.

# Can you define it yourself?

# In[51]:


def MeanAndRMS(inlist): 

    if len(inlist) == 0: 
        print("Ups, called function with an empty list. \nIf I don't exit now, I will divide by zero when calculating the mean")
        return [-9999999999.9, -99999999999.9]

    elif len(inlist) == 1: 
        print("Ups, called function with a list of length one. \nIf I don't exit now, I will divide by zero when calculating the RMS")
        return [inlist[0], -99999999999.9]

    # Find the mean:
    mu = 0.0 # fill this out yourself

    # Find the standard deviation (RMS):
    rms = 0.0 # fill this out yourself

    return [mu, rms] # Return a list with two values: [mean, rms]


# In[52]:


# Calculate the mean and rms of the values in your two lists with random numbers :
mu_sigma_uni = MeanAndRMS(uni_array)
mu_sigma_gauss = MeanAndRMS(gauss_array)


# Print the results. Do these values make sense?

# In[53]:


print(f"For 1000 uniformely distributed numbers:   mu = {mu_sigma_uni[0]:5.3f}   rms = {mu_sigma_uni[1]:5.3f}")
print(f"For 1000 Gaussianly distributed numbers:   mu = {mu_sigma_gauss[0]:5.3f}   rms = {mu_sigma_gauss[1]:5.3f}")
print("Is this what you would expect? \n")


# ## Writing and reading files

# Often you will have to read and write ascii files (i.e. human readable text files).  
# We start with writing a file randomnumbers.dat containing some random numbers. 
# 
# First we open `randomnumbers.dat` in write mode. Note that the file is only open in the block opened by the `with ... as file` statement.   
# Afterwards we fill the file with random numbers.

# In[54]:


with open('randomnumbers.dat', 'w' ) as file: 
    
    outline = f"Uniform \t Gaussian \t Poisson \t Exponential \t Power \n"    
    print(outline[:-2]) # do not print the '\n'
    file.write(outline)
    
    for i in range(25): 

        # Numbers distributed according to the following pdfs: uniform, gaussian, poissonian, exponential, power
        outline = f"{r.uniform():9.4f} \t {r.normal():9.4f} \t {r.poisson(10.0):9.0f} \t {r.exponential():9.4f} \t {r.power(1):9.4f} \n"
        print(outline[:-2]) # do not print the '\n'
        file.write(outline)


# ***
# Now we will read the same file in again. 
# 
# First we define lists that can contain the table of random numbers:

# In[55]:


uni = []
gauss = []
pois = []
exp = []
power = []


# 1. We open (read) the file, skip the first line (header) with the `next` command, and then read each line.  For each line the whole line in string format, but want it back in floating point format.   
# 
# 2. Take `line` and strip it of '\n and \t' (i.e. newlines and tabulations) using `line.strip()`
# 3. Split the line into a list using `strip_line.split()`
# 4. Append each of the elements in `format_line` to the empty lists created in the cell above

# In[56]:


with open('randomnumbers.dat', 'r' ) as file: 
    
    next(file)
    
    # Loop through each line in the file
    for line in file: 

        strip_line = line.strip()
        format_line = strip_line.split()

        uni.append( float(format_line[0]) )        # Now "uni" gets the first number in the line.
        gauss.append( float(format_line[1]) )        # Now "gauss" gets the second numb...
        pois.append( float(format_line[2]) )
        exp.append( float(format_line[3]) )
        power.append( float(format_line[4]) )
        
        
        # alternative way using list comprehension:
        # format_line = [float(ientry) for ientry in iline.strip().split()]
        
print(uni)


# Again, this could have been done simpler using Numpy. Numpy provides the method `np.loadtxt`: 

# In[57]:


uni_np, gauss_np, pois_np, exp_np, power_np = np.loadtxt('randomnumbers.dat', unpack=True, skiprows=1)
print(uni_np)


# We see that we get the same output whether or not we use the Numpy version. In case you are unsure about what the keywords `unpack` and `skiprows` does, try to type: `?np.loadtxt` in the cell below here:

# To check that the import fully worked, print the lines 10 to 19: 

# In[58]:


print("\nRandom numbers (range 10-19 read from file): ")
for i in range(10, 20) : 
    print(f"{uni[i]:8.4f} \t {gauss[i]:8.4f} {pois[i]:8.4f} \t {exp[i]:8.4f} \t {power[i]:8.4f}")


# Lastly create a latex table you can copy paste into your paper/thesis with the mean and rms of the numbers you have genereated:

# In[ ]:


print("\\begin{tabular}{|l|cc|}")
print("\t \\hline")
print("\t \\multicolumn{3}{|c|}{PDF Means and RMS}")
print("\t \\hline")
print("\t {0:15s} & {1:7s} & {2:7s}\\\\".format( "pdf", "$\\mu$", "$\\sigma$" ))
print("\t \\hline")

for name, mu_sigma in zip(['Uniform', 'Gaussian', 'Poissonian', 'Exponential', 'Power'], 
                          [MeanAndRMS(lst) for lst in [uni, gauss, pois, exp, power]]):
    print(f"\t {name:15s} & {mu_sigma[0]:7.3f} & {mu_sigma[1]:7.3f} \\\\")

print("\t \\hline")
print("\\end{tabular}")
print("")


# This can be quite useful, when the result of code needs to go into a document (thesis?). Try yourself to write the above LaTeX table into a file, which could then be included by your LaTeX code.
