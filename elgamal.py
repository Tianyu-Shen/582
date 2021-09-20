import random

from params import p
from params import g
# g=9698439374675276823390863679085787099821687964590973421364530706908301367232976242960049544758496470828675688981570819335336142993170304256564916507021997
# p=17485407687035251201370420829093858071027518631263552549047038216080132036645437679594890870680904087373138192057582526597149370808367592630377967178132719


def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,p)
    return pk,sk

def encrypt(pk,m):
    q=(p-1)/2
    r=random.randint(1,q)

    c1 = pow(g,r,p)
    
    c2= pow(pow(pk,r,p)*pow(m,1,p),1,p)
    
    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]

    #m = pow(c2/pow(c1,sk),1,p)
    #print("working")
    #m = pow(pow(c2,1,p)/pow(c1,sk),1,p)
    m= pow(pow(c2,1,p)*pow(c1,-sk,p),1,p)
    return m

# if __name__ == '__main__':
#     pk,sk=keygen()
#     print("done")
#     e_text=encrypt(pk,111)
#     print("done")
#     print(decrypt(sk,e_text))
#     print("done")
