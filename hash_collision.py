import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    

    dict={}
    mask=(1<<k)-1
    #print(bin(mask))

    while True:

        x=os.urandom(64)
    
        # hashed=hashlib.sha256(x).digest()

        # int_hashed=int.from_bytes(hashed,"little")

        int_hashed=gethash(x)
        
        key=int_hashed&mask

        if key in dict:
            y=dict[key]
            break
        else:
            dict[key]=x

    print(bin(gethash(x)&mask))
    print(bin(gethash(y)&mask))

    
    return( x, y )


def gethash(x):

    hashed=hashlib.sha256(x).digest()

    int_hashed=int.from_bytes(hashed,"big")

    return int_hashed

# if __name__ == '__main__':
    # print(hash_collision(9))



