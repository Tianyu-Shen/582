
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for a in plaintext:

    	idx=ord(a)+key

    	while(idx>90):
    		idx-=26

    	while(idx<65):
    		idx+=26

    	ciphertext+=chr(idx)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HER
    for a in ciphertext:

    	idx=ord(a)-key

    	while(idx>90):
    		idx-=26

    	while(idx<65):
    		idx+=26

    	plaintext+=chr(idx)

    return plaintext


# def main():

# 	# a="Z"
# 	a="BASE"
# 	key=1

# 	b=encrypt(key,a)

# 	c=decrypt(key,b)
# 	# print(ord(a))
# 	print("Encrypted String is "+b)

# 	print("Decrypted String is "+c)


# if __name__ == '__main__':
# 	main()
