from datetime import datetime
import hashlib
import json

def hashEntry(entry):
    return(hashlib.sha256(entry.encode('utf-8')).hexdigest())


def setEntry(previous, timestamp, data, index, nonce):
    if previous == None:
        return str(timestamp)+data+str(index)+str(nonce)
    else:
        return str(timestamp)+data+str(index)+previous+str(nonce)


class Block:

    def __init__(self, index, previous, timestamp, data):
        self.nonce = 0
        self.index = index
        self.previous = previous
        self.timestamp = timestamp
        self.data = data
        entry = setEntry(self.previous, self.timestamp, self.data, self.index, self.nonce)
        self.hashcode = hashEntry(entry)
        
    def mine(self):
        while self.hashcode[0:3] != "000":
            self.nonce +=1
            entry = setEntry(self.previous, self.timestamp, self.data, self.index, self.nonce)
            self.hashcode = hashEntry(entry)

class BlockChain():

    def __init__(self):
        self.maxNonce = 50000
        self.validity = True
        self.nbr_blocks = 0
        self.blockchain = {}
        
    def __str__(self):
        output = "BlockChain =>"
        for i in range(0,len(self.blockchain)):
            output += ",\nindex = "
            output += str(self.blockchain[i].index)
            output += "\n: [data = "
            output += str(self.blockchain[i].data)
            output += ",\n: timestamp = "
            output += str(self.blockchain[i].timestamp)
            output += ",\n hashcode = "
            output += str(self.blockchain[i].hashcode)
            output += ",\n previous = "
            output += str(self.blockchain[i].previous)
            output += ",\n NOUNCE = "
            output += str(self.blockchain[i].nonce)
            output += "]"
        return output

    def newBlock(self, list):
        print("add...")
        for arg in list:
            print(arg)
            if type(arg) is str:
                print(arg)
                index = len(self.blockchain)
                timestamp = datetime.now()
                if index == 0:    
                    previous = None
                else:
                    previous = self.blockchain[index-1].hashcode
                newBlock = Block(index, previous, timestamp, arg)
                newBlock.mine()
                if newBlock.nonce <= self.maxNonce:
                    self.blockchain[len(self.blockchain)] = newBlock
                else:
                    print("Block enlevé, trop de nonce")

    def delete(self):
        self.blockchain = {}
        return self.blockchain
        

chain1 = BlockChain()

while True:
    value = input("Créer un nouveau block: (les séparer d'une virgule pour en ajouter plusieurs)\n").split(',')
    chain1.newBlock(value)
    print(chain1)
    dictForJson = {}
    for i in range(0,len(chain1.blockchain)):
        dictForJson.update({chain1.blockchain[i].index: [chain1.blockchain[i].data, chain1.blockchain[i].hashcode, chain1.blockchain[i].previous] })
    with open('blockchain.json', 'w') as f:
        json.dump(dictForJson, f)  