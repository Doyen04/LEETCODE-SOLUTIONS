num = 103

def happy_number(num):

    if len(str(num)) <= 1: return False
    h_num = num

    while len(str(h_num)) > 1:

        split = list((lambda x : x)(str(h_num)))
        h_num = sum(list(map(lambda x: int(x)**2, split)))
        print(h_num)
    return True if h_num == 1 else False
    
print(happy_number(num))