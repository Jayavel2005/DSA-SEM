class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        n = int(input("Enter the number of nodes: "))
        for i in range(n):
            value = int(input(f"Enter the value for node {i + 1}: "))
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                temp = self.head
            else:
                temp.next = newNode
                temp = newNode

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insertFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertlast(self):
        value = int(input("Enter the value for the new node: "))
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def insertPosition(self):
        value = int(input("Enter the value for the new node: "))
        position = int(input("Enter the position: "))
        newNode = Node(value)

        if position == 1:
            self.insertFront(value)
            return

        temp = self.head
        for i in range(1, position - 1):
            if temp is None:
                print("Position out of bounds!")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds!")
        else:
            newNode.next = temp.next
            temp.next = newNode

    # Deletion Techniques
    def deleteFront(self):
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return
        print(f"Deleted: {self.head.data}")
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return

        if self.head.next is None:
            print(f"Deleted: {self.head.data}")
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        print(f"Deleted: {temp.next.data}")
        temp.next = None

    def deletePosition(self):
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return

        position = int(input("Enter the position to delete: "))

        if position == 1:
            print(f"Deleted: {self.head.data}")
            self.head = self.head.next
            return

        temp = self.head
        for i in range(1, position - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds!")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of bounds!")
        else:
            print(f"Deleted: {temp.next.data}")
            temp.next = temp.next.next

# Example usage
sll = LinkedList()

# Insert initial nodes
sll.insert()

# Display the linked list
print("Initial Linked List:")
sll.display()

# Insert at the front
value = int(input("Enter the value to insert at the front: "))
sll.insertFront(value)

# Insert at the end
sll.insertlast()

# Insert at a specific position
sll.insertPosition()

# Display the linked list
print("Linked List after insertions:")
sll.display()

# Delete the first node
sll.deleteFront()

# Delete the last node
sll.deleteLast()

# Delete a node at a specific position
sll.deletePosition()

# Display the final linked list
print("Linked List after deletions:")
sll.display()
