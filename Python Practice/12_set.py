from loguru import logger
var_dict = {} # this will create a dictionary and not a set
logger.info(type(var_dict))

set_var = set()
logger.info(type(set_var))

set_var = {1,2,2,4,5,6,7, 3} # a set is immutable, unordered collection of data

logger.info(set_var)

for num in set_var: # you can always iterate a set like a normal collection
    logger.info(num)

new_set = {5,6,89,91,84,6,2,4} # declaring a new set

logger.info(new_set.union(set_var)) # using union method

logger.info(new_set.intersection(set_var)) # using intersection method

logger.info(new_set.difference(set_var)) # using difference method

logger.info(new_set.isdisjoint(set_var)) # checking if disjoint

new_set.add(45) # using add method

logger.info(new_set)

new_set.remove(45) # will through error if the value is not present

new_set.discard(99) # this will not throw error if value is not present

logger.info(new_set)

# Given two lists, find the missing and additional values in both the lists
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]
set1 = set(list1)
set2 = set(list2)

additional_values =set1.difference(set2)
missing_values_l1 = set2.difference(set1)
print(additional_values)
print(missing_values_l1)


# Given three lists, find the elements common in all the lists
final_list = []
list1 = [1,2,4,5,6]
list2 = [1,7,8,9,4]
list3 = [1,4,89,90]


common_set = set(list1).intersection(set(list2), set(list3))

logger.info(f"The final common set is {common_set}")



