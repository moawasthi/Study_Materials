from loguru import logger
def sum(*numlist):
    result = 0
    for num in numlist:
        result += num
    return result

def customLogging(**kwargs):
    file_path = "D:\\03_Study\\01_Daily Practice Log\\"
    file_name = "logmessage.txt"
    for key, value in kwargs.items():
        with open(file_path + file_name, "w", encoding="utf-8") as f:
            f.write(f"{key} {value}\n")
        return "file written successfully"

result_sum = sum(1,3,4,5, 6,1)
logger.info(f"The total sum is {result_sum}")
logmessage = input("Enter log message")
customLogging(message = logmessage)



