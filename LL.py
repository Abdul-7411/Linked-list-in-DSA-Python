class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
    # Creating an Empty Linkedlist
        self.head = None
        self.n = 0# Number of nodes in the LL
        
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        # create a new node
        new_node = Node(value)
        
        # connection
        new_node.next = self.head
        # Reassign
        self.head = new_node
        self.n+=1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data)
            curr = curr.next
        return result[::-1]
    
    def append(self,item):
        new_node = Node(item)
        
        if self.head == None:
            self.head = new_node
            self.n+=1
            return
            
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n +=1
        
    def insert_tail(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr !=None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            #logic
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            print("No item found..\n")
            
    def clear(self):
        self.head = None
        self.n = 0
    
    def del_head(self):
        if self.head == None:
            print("Linked List is Empty...")
            return 
        self.head = self.head.next
        self.n -=1
    def pop(self):
        curr = self.head
        if curr == None:
            print("Linked List is Empty...")
            return
        
        if curr.next == None:
            self.del_head()
            return
        
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -=1
    
    def remove(self,value):
        curr = self.head
        
        if curr == None:
            print("LL is Empty...")
            return 
        
        if curr.data == value:
            return self.del_head()
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next 
        # Case1 if item not found
        if curr.next == None:
            print("Item not found..")
            return
        curr.next = curr.next.next
        self.n-=1
    
    def search(self,value):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos+=1
        return "Item Not Found"
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos+=1
        return "Index out of range"
    
    def replace_max(self,value):
        temp = self.head
        max_num = temp
        
        while temp != None:
            if temp.data > max_num.data:
                max_num = temp
            temp = temp.next
        max_num.data = value
    
    def odd_sum(self):
        curr = self.head
        pos = 0
        sum_num  =  0
        while curr != None:
            if pos%2!=0:
                sum_num = sum_num + curr.data
            curr = curr.next
            pos +=1
        return sum_num

    def reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
    
    def change_sent(self):
        
        temp = self.head
        
        while temp != None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                if temp.next.data == '*' or temp.next.data == '/':
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next
                    
            temp = temp.next

ll = LinkedList()