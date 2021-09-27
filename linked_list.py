import hashlib
class Block:
    def __init__(self, index, timestamp, content, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.content = content
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
   
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.content).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()
      
M4BlockChain = []

from datetime import datetime
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")
    
M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
def next_block(last_block):

    return Block(last_block.index+1,datetime.now(),"this is block "+str(last_block.index+1),last_block.hash)

    
# append 5 blocks to the blockchain
def app_five(block_list):
    

    if(len(block_list)==0):
        fst=create_genesis_block()
        block_list.append(fst)

        sec=next_block(fst)
        block_list.append(sec)

        third=next_block(sec)
        block_list.append(third)

        forth=next_block(third)
        block_list.append(forth)

        fifth=next_block(forth)
        block_list.append(fifth)

        return

    lastb=block_list[0]

    for b in block_list:
        if b.index>lastb.index:
            lastb=b

    fst=next_block(lastb)
    block_list.append(fst)

    sec=next_block(fst)        
    block_list.append(sec)

    third=next_block(sec)
    block_list.append(third)

    forth=next_block(third)
    block_list.append(forth)

    fifth=next_block(forth)
    block_list.append(fifth)

    return

# if __name__ == '__main__':
#     bl=[]
#     bl.append(create_genesis_block())
#     app_five(bl)
#     print(len(bl))

