from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256
import random

def sign(m):
	#generate public key
	#Your code here
	G=secp256k1.G
	n=ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
	d=1 
	public_key = d*G


	#generate signature
	#Your code here
	k=random.ranint(1,10000000000)
	W=k*G

	x1=W.x
	y1=W.y

	r=pow(x1,1,n)
	z=sha256(m).digest()
	s = pow(pow(k,-1,n)*pow((z+rd),1,n),n)

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )



