from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256
import random

def sign(m):
	#generate public key
	#Your code here
	G=secp256k1.G
	n=secp256k1.q
	d=1
	# print(type(d))
	# print(type(G))

	public_key =G*d


	

	#generate signature
	#Your code here
	k=random.randint(1,n)
	W=G*k
	

	x1=W.x
	y1=W.y
	
	r=pow(x1,1,n)
	
	z=int.from_bytes(sha256(m.encode('utf-8')).digest(),"big")

	print("k"+str(type(k)))
	print("n"+str(type(n)))
	print("z"+str(type(z)))
	print("r"+str(type(r)))
	print("d"+str(type(d)))

	s = pow(pow(k,-1,n)*pow((z+r*d),1,n),n)
	print("s done ")
	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )



# def test():
# 	n=int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8C",16)
# 	print(n)

# if __name__ == '__main__':
# 	test()