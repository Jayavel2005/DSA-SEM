class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert multiple nodes
    def insert(self):
        n = int(input('Enter the number of Nodes: '))
        for i in range(n):
            newNode = Node(int(input("Enter the node value: ")))
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                self.tail.next = self.head  # Circular link
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head  # Maintain circular link

    # Display the circular linked list
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        print("Circular Linked List: ", end="")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")  # Indicate circular structure

    # Insert a node at the front
    def insertFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head  # Circular link
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head  # Update tail's next link

    # Insert a node at the end
    def insertLast(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head  # Circular link
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head  # Maintain circular link

    # Delete the first node
    def deleteFront(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Update tail's next link

    # Delete the last node
    def deleteLast(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp  # Update the tail

    # Delete a node at a specific position (1-based indexing)
    def deleteByPosition(self, pos):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        
        if pos == 1:  # Delete the first node
            self.deleteFront()
            return

        temp = self.head
        count = 1
        prev = None

        while count < pos and temp.next != self.head:
            prev = temp
            temp = temp.next
            count += 1

        if count < pos:  # Position is out of range
            print("Position out of range.")
            return

        # Remove the node
        prev.next = temp.next
        if temp == self.tail:  # If deleting the last node
            self.tail = prev

        print(f"Node at position {pos} deleted.")

# Testing the CircularLinkedList
cll = CircularLinkedList()

# Insert nodes
cll.insert()  # Input number of nodes and values
cll.insertFront(5)  # Insert a node at the front
cll.insertLast(99)  # Insert a node at the end
cll.display()  # Display the list

# Deletion operations
cll.deleteFront()  # Delete the first node
cll.display()

cll.deleteLast()  # Delete the last node
cll.display()

cll.deleteByPosition(3)  # Delete the node at position 3
cll.display()

cll.deleteByPosition(10)  # Attempt to delete a node at an out-of-range position
