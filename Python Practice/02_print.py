# #########################################
# 01. Why do we need print statement
# 02. How can we print new line in print statement
# 03. What is escape sequence and how to use it
# 04. What is string formatting
##########################################

# We primarily use print statements for debugging purpose.
lengthOfLand = 100
lengthOfGarden = 100
nameofLabour = 'Ram Pyaare'
isHome = True
print("Length of land is", lengthOfLand)

# we can also use single quotes in print statements
print('length of garden is ', lengthOfGarden)

#using escape sequences

print('length fo garden is "awesome" ', lengthOfGarden)
print("length of garden is \"awesome\" ", lengthOfGarden)

#using triple quotes
print(''' My home is "4 BHK" and 
length of garden is "awesome"''', lengthOfGarden)

#string formatting using f string
print(f"Length of land is {lengthOfLand}\nLength of garden is {lengthOfGarden}\nName of labour is {nameofLabour}")

#string formatting using .format
print("Length of land is {0} \nLength of garden is {1} \nName of labour is {2}".format(lengthOfLand,lengthOfGarden, nameofLabour))



