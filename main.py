def palin(my_str):
    my_str = my_str.lower()
    temp = my_str[::-1]
    print(temp)
    if palin == temp:
        return True
    else:
        return False
print(palin("fddf"))
