
# coding: utf-8

# In[167]:

from hashlib import sha256


# In[168]:

class Block:
    def __init__(self,index,data,prev_hash):
        self.index=index
        self.data=data
        self.prev_hash=prev_hash
        self.hash_value=self.hash_block()
        
    def hash_block(self):
        temp=sha256()
        temp.update(str(self.index)+str(self.data) + str(self.prev_hash))
        return temp.hexdigest()
    
    def display(self):
        print("Block Index :"+str(self.index)+" \nBlock Data:  " +str(self.data) +" \nPrevious Block hash :"+ 
              str(self.prev_hash)+" \nCurrent Block hash : "+ str(self.hash_value)+"\n\n")


# In[169]:

def create_next_block(current_block,data):
    return Block(current_block.index+1,data,current_block.hash_value)


# In[170]:

class User:
    def __init__(self,name,amount):
        self.name=name
        self.balance=amount


# In[171]:

def transfer(sender,reciever,amount):
    if sender.balance>=amount:
        sender.balance=sender.balance-amount
        reciever.balance=reciever.balance+amount
        return sender.name+" paid "+reciever.name+" an amount of "+str(amount)+ " coins. "
    else:
        return 0




Raj=User("Raj",100)
Rahul=User("Rahul",50)
Mohit=User("Mohit",15)



transactions=[]
transactions.append(transfer(Raj,Rahul,10))
transactions.append(transfer(Mohit,Rahul,12))
transactions.append(transfer(Mohit,Rahul,5))
transactions.append(transfer(Raj,Mohit,20))


genesis_block=Block(0,"Genesis Block",0)
blocks=[genesis_block]



for i in range (len(transactions)):
    if(transactions[i]!=0):
        blocks.append(create_next_block(blocks[-1],transactions[i]))


for i in range (len(blocks)):
    blocks[i].display()


print(Raj.balance)


print(Rahul.balance)


print(Mohit.balance)

