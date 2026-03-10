#########################################################
# 1. To check if output is expected or not
# 2. check if variable or list is empty or not
# 3. check if dataframe is empty
# 4. backdated job Run
# 5. to raise some error
##########################################################

result = int(input("Enter a number: "))
if result % 2 == 0:
    if result < 100:
        print(f"{result} is two digit even number.")
    elif result > 100 and result < 1000:
        print(f"{result} is a three digit even number.")
    else:
         print(f"{result} is even.")
else:
    print(f"{result} is odd.")