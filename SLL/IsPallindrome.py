class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def is_pallindrome(self):
    # Method 1
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_pallindrome2(self):
    # Method 2
        p = self.head
        q = self.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        count = 1
        while count <= i // 2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def is_pallindrome3(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True





llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("C")
llist.append("E")
llist.append("C")
llist.append("A")
llist.append("R")

llist1 = LinkedList()
llist1.append("A")
llist1.append("B")
llist1.append("C")

print(llist.is_pallindrome())
print(llist1.is_pallindrome())
print("\n")
print(llist.is_pallindrome2())
print(llist1.is_pallindrome2())
print("\n")
print(llist.is_pallindrome3())
print(llist1.is_pallindrome3())