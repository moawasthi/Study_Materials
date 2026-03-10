def final_amount(*args, discount = 0.1 ):
    try:
        result = 0
        dis = discount
        for num in args:
            result += num
        return result - (result * discount)
    except TypeError as e:
        raise e
    except Exception as e:
        raise e
try:
    to_pay = final_amount(1,2,4,'5')
    print(to_pay)
except Exception as e:
    print(f"Some Non Blocking Error Occured. {e}")
