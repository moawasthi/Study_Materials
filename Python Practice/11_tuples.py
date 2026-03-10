from loguru import logger
test_tuple = [1,2,3,True, "Mohit"]
logger.info(test_tuple[0])

#using slicing in tuple
logger.info(test_tuple[0:])
logger.info(test_tuple[0:3]) # last value is not included

#using count 
logger.info(test_tuple.count("Mohit"))

#using len
logger.info(len(test_tuple))

#using index
logger.info(test_tuple.index(2)) 

#Write a program to return entire element as a tuple 
#which can have a list in tuple input

test_tuple = ([1,2], [3,4], [5,6])
list_tuple = []
for i in range(len(test_tuple)):
    for number in test_tuple[i]:
        list_tuple.append(number)

tuple_output = tuple(list_tuple)
print(tuple_output)


result = ()
for list in test_tuple:
    var_output = tuple(list)
    result += var_output
print(result)

#write a program to return a tuple which is exponential of given two tuples

tuple_1 = (2,4,5)
tuple_2 = (2,3,5)
result = ()
for i in range(len(tuple_1)):
    result_tup = tuple_1[i] ** tuple_2[i]
    result += (result_tup,)
logger.info(result)
