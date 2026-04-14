# Unpacking a sequence into separate variables
####################
# YOu have an N element of tuple or sequence that 
# you would like to unpack into a collection of N variables
##################

p = (4,5)
(x,y) = p
print(x)
print(y)

data = ['Acme', 50, 91.1, (2012, 12,21)]
name, shares, price, date = data
name, shares, price, (year, month, date) = data
print(f"The name of the company is {name}, the number of shares are {shares} with a price of {price} on the date {date}.")
print(f"The name of the company is {name}, the number of shares are {shares} with a price of {price} in the year {year} , {month} , {date}.")

# discarding values
_, shares, price, _ = data
print(f"{shares} number of shares with a price of {price}")

# Unpacking elements with arbitary lengths
####################
# YOu have an N element of tuple or sequence that 
# you would like to unpack into a collection of N variables
# however the N elements are arbitary
##################

def first_last_grades(grades):
     first, *middle, last = grades
     return (first + last)/ 2

avg_first_last = first_last_grades([10,20,99,89,100])
print(f"The avg of first and last exams is {avg_first_last}.")



record = ('Dave', 'dave@example.com', '0797979', '97968687587')
name, email, *phoneNumbers = record
print(name, email, phoneNumbers)

# Get trailing quarters avg and compare it with the current quarters
def calculateTrailingVsCurrent(salesRecord):
     *trailing, current = salesRecord
     avgTrailing = sum(trailing) / len(trailing)
     return current - avgTrailing
print(f"The trailing vs current is {calculateTrailingVsCurrent([10,9,8,6,4,9])}")


records = [
     ('foo', 1,2),
     ('bar', 'hello'),
     ('foo', 3,4)
]
print(records)
def do_foo(x, y):
     print('foo', x, y)
def do_bar(z):
     print('bar', z)

for tag, *args in records:
     if tag == "foo":
          do_foo(*args)
     elif tag == "bar":
          do_bar(*args)

