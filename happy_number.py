num = 7

def happy_number(num):

    h_num = num

    while h_num != 4 and h_num != 1:

        split = list((lambda x : x)(str(h_num)))
        h_num = sum(list(map(lambda x: int(x)**2, split)))
        print(h_num) 
    return True if h_num == 1 else False
    
print(happy_number(num))