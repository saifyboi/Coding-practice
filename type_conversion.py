def int_to_str(num):
    print(num, "started as:", type(num))
    print("but now it's:", type(str(num)))
    return num
    
    
def str_to_int(string):
    print(string, "started as:", type(string))
    print("but now it's:", type(int(string)))
    return string


print(int_to_str(7))
print(str_to_int("70"))

