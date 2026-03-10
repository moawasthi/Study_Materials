from loguru import logger
email_name = "cmhhamzaalimanzari987@gmail.com"
morphed_name = ''
split_name = email_name.split("@")
logger.info(split_name)
for i in range( len(split_name[0] ) ):
    if i == 0 or i == len(split_name[0] ) -1 :
        morphed_name += split_name[0][i]
    else:
        morphed_name += "*"

logger.info(morphed_name + '@' + split_name[1]) 
