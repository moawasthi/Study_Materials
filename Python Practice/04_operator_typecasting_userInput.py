# =========================================
# What are Python Operators
# what is BODMAS Rule in Python
# How to use floor and ceil in python
# What is modulo operator in python
# Types of typecasting in python
# how to take user input in python
# =========================================

from loguru import logger
import math
lengthofLand = 100
breadhofLand = 100 

areaofLand = lengthofLand * breadhofLand
perimeterOfLand = 2 * (lengthofLand + breadhofLand)

logger.info(f"Area of Land is {areaofLand} sq ft.")
logger.info(f"Perimeter of Land is {perimeterOfLand} ft.")

print(math.floor(lengthofLand // 3) , lengthofLand /3)
print(math.ceil(breadhofLand / 7), breadhofLand / 7)
print(lengthofLand % breadhofLand)