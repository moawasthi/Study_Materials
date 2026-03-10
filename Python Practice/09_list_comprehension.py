
from loguru import logger
number_list = []
for i in range(1,11):
    number_list.append(i)

new_list = [number for number in number_list if number%2 == 0]
logger.info(f"{new_list}")

new_list_odd_even = ["Even" if number %2 == 0 else "Odd" for number in number_list]
logger.info(f"{new_list_odd_even}")
