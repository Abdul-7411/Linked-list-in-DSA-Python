# Linked-list-in-DSA-Python
Linked List in Python

This repository contains a custom implementation of a Singly Linked List in Python.
The implementation includes all the basic operations like insertion, deletion, searching, and traversal, along with some additional utility functions.

📌 Topics: Linked List
✅ Features Implemented

Create an Empty Linked List

Insert Operations

Insert at head (insert_head)

Insert at tail (append)

Insert after a specific node (insert_tail)

Delete Operations

Delete head node (del_head)

Delete last node (pop)

Remove specific node by value (remove)

Clear the entire Linked List (clear)

Access & Search

Search for a value (search)

Get item by index (__getitem__)

Other Utilities

Replace maximum value (replace_max)

Sum of values at odd positions (odd_sum)

Reverse the Linked List (reverse)

Modify characters in a sentence (change_sent)

⚙️ How It Works
Node Structure
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

Linked List Structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0  # Number of nodes

🚀 Usage
Creating a Linked List
ll = LinkedList()

Inserting Elements
ll.insert_head(10)
ll.append(20)
ll.insert_tail(10, 15)  # Insert 15 after 10

Deleting Elements
ll.del_head()   # Remove head
ll.pop()        # Remove last node
ll.remove(15)   # Remove node with value 15

Searching and Access
print(ll.search(20))  # Returns index if found
print(ll[0])          # Access by index

Other Operations
ll.reverse()           # Reverse the linked list
ll.replace_max(99)     # Replace max element with 99
print(ll.odd_sum())    # Get sum of elements at odd positions

🧾 Example Output
ll = LinkedList()
ll.insert_head(5)
ll.insert_head(10)
ll.append(20)
print(len(ll))  # 3
print(ll)       # "20510" (string representation reversed)
