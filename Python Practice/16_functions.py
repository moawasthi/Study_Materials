# calculate the cost of grass 
# Land dimensions = 100 ft by 100 ft
# Garden dimension = 100 ft by 20 ft
# Home dimensions = 80 ft by 60 ft
from loguru import logger

def area_of_shape(length, width, shape):
    if shape.lower() in ["rectangle", "square"] :
        return length * width
cost_per_feet = 17    
land_area = area_of_shape(100 , 100 , "square")
garden_area = area_of_shape(100, 20, "rectangle")
home_area = area_of_shape(80, 60, "rectangle")
total_cost = (land_area - (garden_area + home_area) ) * cost_per_feet
logger.info(f"The total cost of carpeting is {total_cost}.")
