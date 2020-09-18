# Stacks, Queues, and Deques
# Author: Marcelious Willis

class Node:
    """Node class to maintain nodes of a linked list"""
    def __init__(self,element):
        self.element = element
        self.next = None  
        
class Stack:
    """Stack class to create/modify a linked list. LIFO principle"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Method to check if the linked link exists
    def is_empty(self):
        if len(self.size) < 1:
            return True
        else:
            return False
    
    # Method to add a element to the head of the linked list
    def push(self,element):
        newNode = Node(element)  # Create Node instance for the new node
        newNode.next = self.head # Set the new node's next link to the old node.
        self.head = newNode      # Set the current head to the new next link.
        self.size += 1           # Increase the size of the linked list.
        
    # Method to remove the element at the head of the linked list    
    def pop(self):
        if self.is_empty():
            return("Your Linked List is empty. Nothing to pop!")
        self.head = self.head.next # Set the head to the next node
        self.size -= 1             # Decrease the size of the linked list
        
    # Method to display the element at the head of the linked list
    def top(self):
        if self.is_empty():
            return("Your Linked List is empty!")
        print(self.head)
        
    # Method to get the size of the linked list
    def get_size(self):
        if self.is_empty():
            return("Your linked list is empty!")
        print("Size of the linked link is: ",self.size)
        