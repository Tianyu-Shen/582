import math

def num_BTC(b):


    cnt=b
    curr_price=50

    sum=0

    while cnt>=210000:
        cnt-=210000
        sum+=curr_price*210000
        curr_price/=2

    sum+=cnt*curr_price
    return sum

# if __name__ == '__main__':
#     print(num_BTC(210001))

