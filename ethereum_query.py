from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
# #     This line will mess with our autograders, but might be useful when debugging
# #     print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = {}   #YOUR CODE HERE
    return w3.eth.get_transaction(tx)

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    
    t=get_transaction(tx)

    return t.get("gasPrice")  

def get_gas(tx):
    
    rec=w3.eth.get_transaction_receipt(tx)

    return rec.get("gasUsed")

def get_transaction_cost(tx):
    
    price=get_gas_price(tx)
    a=get_gas(tx)
    return a*price

def get_block_cost(block_num):
    block_cost = 1  #YOUR CODE HERE
    b=w3.eth.get_block(block_num)
    ts=b1.get("transactions")

    sum=0

    for i in ts:
        sum+=get_transaction_cost(i)

    return sum

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    b=w3.eth.get_block(block_num)

    ts=b.get("transactions")

    high=0

    for i in ts:
        fee=get_transaction_cost(i)

        if fee>high:
            high=fee
            tx=i

    max_tx=HexBytes(tx)
    return max_tx

