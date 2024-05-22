class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def __hash(self,key):
        return hash(key)%self.capacity
    
    def insertdata(self,key,value):
        index = self.__hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key,value)
            self.size += 1
        else:
            current_node = self.table[index]
            while(current_node):
                if current_node.key == key:
                    current_node.value = value
                    return
                current_node = current_node.next
            new_node = Node(key,value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size +=1
            
    def searchdata(self,key):
        index = self.__hash(key)
        current_node = self.table[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        raise KeyError
    
    def remove(self,key):
        index = self._hash(key) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        raise KeyError(key) 
    
if __name__ == '__main__':            
            
    htobj = Hashtable(6)

    htobj.insertdata("hii",2)
    htobj.insertdata("surbhi",1)
    htobj.insertdata("megha",4)
    print(htobj.searchdata("hii"))
    htobj.remove("surbhi")
    print(htobj.searchdata("surbhi"))
    
    # using insert you can also update the value
    htobj.insertdata("hii",67)
    print(htobj.searchdata("hii"))
    


        