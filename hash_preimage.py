import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    target=int(target_string,2)
    #print(target)
    
    l=len(target_string)

    mask=(1<<l)-1
    
    while True:
        
        x=os.urandom(64)

        int_hashed=gethash(x)

        key=int_hashed&mask

        if key==target:
            break

    return x

def gethash(x):

    hashed=hashlib.sha256(x).digest()

    int_hashed=int.from_bytes(hashed,"big")

    return int_hashed


# if __name__ == '__main__':
#     print(hash_preimage("11"))
