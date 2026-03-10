from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r"D:\03_Study\repos\python_practice\config_file.ini")
brick_cost = config["raw_materials"]["bricks_cost"]
bar_cost = config["raw_materials"]["bar"]
logger.info(f"cost of brick {brick_cost} and datatype is {type(float(brick_cost))}")
logger.info(f"cost of brick {bar_cost} and datatype is {type(float(bar_cost))}")


student_details = {1 : ["something", "History"],
                   2 : ["Biology", "Chemistry", "History"],
                   3: ["Science"]
                   }
def total_cost_per_student(books):
    try:
        cost_per_student = 0
        for book in student_details[books]:
            cost_per_student += int(config["books_price"][book])
        return cost_per_student
    except KeyError as e:
        logger.info( f"Missing Key : {e}")


try:
    for books in student_details:
        cost_of_books = 0
        cost_of_books += total_cost_per_student(books)
        logger.info(f"total cost of books for {books} are {cost_of_books}")
except Exception as e:
    print(f"Some non blocking error occured {e}")
    #raise e

