from loguru import logger

list_sample = ["Mohit", "Shankar", "Ravi", "Rachin"]
result = " ".join(list_sample)
logger.info(result)

result = ""
for name in list_sample:
    result = result + " " + name

logger.info(result)

# join will not work on anything apart from strings
list_sample_num = [1,3,4,56,66]
result_num = " ".join(str(list_sample_num))

logger.info(str(result_num))

# Join
list_query = [{"State" : "TS", "Dept" : "HR"},
              {"State": "UK", "Dept": "IT"}]

sep = " OR "
query_condition = []
for query in list_query:
    for key, values in query.items():
        query_condition.append(f"{key} = '{values}'")

sep = " OR "
final_query = sep.join(query_condition)

print(final_query)


