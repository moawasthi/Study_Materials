################################################
# 1. How to create a list in Python
# 2. What is a list : collection of same or different data types
# 3. What is multidimensional list
# 4. How to access data from a list
# 5. Methods to access data from a list
# 6. -ve indexing in list
# ################################################
from loguru import logger

list_labour = ["Mahesh", "Mithilesh", "Ramesh", "Sumesh"]

logger.info(f"Total number of labours are {len(list_labour)}")

logger.info(f"Labour 1 is {list_labour[0]}")

logger.info(f"Labour 4 is {list_labour[-1]}")

new_labour = ["Ram", "Mohan"]

list_labour.extend(new_labour)

logger.info(list_labour)

list_labour.append("McMohan")
logger.info(list_labour)

#Multi Dimensional list
list_labour = [ ["Mahesh", 500], ["Ramesh", 200]]
logger.info(f"Labour {list_labour[0][0]} charges {list_labour[0][1]}")

# Adding two liststogether
list_wages = [400, 300, 600, 700]
list_labour = ["Mohan", "Ram", "Samay", "Amit"]

list_new = list_labour + list_wages
logger.info(list_new)

#using len method
logger.info(f"{len(list_new)}")

#using string split
string_long = "Visa/4242424242424242/12/34/123/Mastercard/5555555555554444/11/33/123/AmEx/378282246310005/10/32/1234/Discover/6011111111111117/09/31/123"
string_split_list = string_long.split("/")
logger.info(string_split_list[-1])

#using colon in list
logger.info(f"Card brand is : {string_split_list[-5:][0]} \n" 
            f"CVV is {string_split_list[-5:][-1]}" 
            )

#changing a list value
list_labour[0:2] = ["Pyare Mohan", "Ram Kumar"]
logger.info(list_labour)

#using pop in list
list_labour.pop()
logger.info(list_labour)

removed_value = list_labour.pop(1)
logger.info(f"{list_labour} is the modifiied list, and removed element is {removed_value}")

#Inserting into a list
list_labour.insert(1,"Ram Kumar Ka Beta")
logger.info(list_labour)

#Deleting a list
del list_labour

