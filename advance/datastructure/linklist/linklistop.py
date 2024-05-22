class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def insertAtBegining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtLast(self,data) :
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        
    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
                
    def deleteAtStart(self):
        if(self.head == None):
            return
        self.head = self.head.next
        
    def deleteAtEnd(self):
        if(self.head == None):
            return
        else:
            current_node = self.head
            while(current_node.next.next):
                current_node = current_node.next
            current_node.next = None
            
    def deleteAtIndex(self,index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
                
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
linkList = LinkList()
linkList.insertAtBegining(2)
linkList.insertAtBegining(5)
linkList.insertAtLast(4)
linkList.insertAtIndex(5,2)

# linkList.printLL()
linkList.deleteAtStart()
linkList.insertAtLast(4)
linkList.deleteAtStart()
linkList.deleteAtIndex(2)
linkList.printLL()
