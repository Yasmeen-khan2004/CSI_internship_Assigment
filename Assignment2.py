class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer.")

        if n == 1:
            self.head = self.head.next
            return

        curr = self.head
        count = 1

        while curr and count < n - 1:
            curr = curr.next
            count += 1

        if not curr or not curr.next:
            raise IndexError("Index out of range.")

        curr.next = curr.next.next


# Test the LinkedList
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)

    print("Initial list:")
    ll.print_list()

    try:
        print("\nDeleting 3rd node:")
        ll.delete_nth_node(3)
        ll.print_list()
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\nDeleting node at index 10 (out of range):")
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\nDeleting node from empty list:")
        empty_list = LinkedList()
        empty_list.delete_nth_node(1)
    except Exception as e:
        print(f"Error: {e}")
