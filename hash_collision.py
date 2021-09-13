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
    
    x=os.urandom(64)
    
    hashed=hashlib.sha256(x).digest()

    int_hashed=int.from_bytes(hashed,"big")
    mask=(1<<k)-1

    key=int_hashed&mask
    #print (mask)

    dict={}


    while True:

        x=os.urandom(64)
    
        hashed=hashlib.sha256(x).digest()

        int_hashed=int.from_bytes(hashed,"little")
        mask=(1<<k)-1
        key=int_hashed&mask

        if key in dict:
            y=dict[key]
            break
        else:
            dict[key]=x


    
    return( x, y )

if __name__ == '__main__':
    print(hash_collision(9))



