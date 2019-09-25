class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def addLast(self, item):
        temp = Node(item)
        t = self.head
        if self.head == None:
            self.head = Node(item)
            return
        else:
            while t.next is not None:
                t = t.next
            t.next = temp

    def addFirst(self, item):
        self.head = Node(item, self.head)

    def add(self, index, item):
        if index <= 0:
            self.head = Node(item, self.head)
            return
        count = 0
        t = self.head
        temp = Node(item)
        while count != index:
            if (t.next is not None):
                count = count + 1
                t = t.next
            else:
                break
        tnex = t.next
        t.next = temp
        temp.next = tnex

    def clear(self):
        self.head = None

    def contains(self, x):
        if self.head is None:
            print("list is empty")
            return False
        curr = self.head
        while curr is not None:
            if curr.item == x:
                return True
            else:
                curr = curr.next
        return False

    def get_index_of(self, item):
        count = 0
        temp = self.head
        while temp.item != item:
            if temp.next is None:
                print("ITEM: ", item, " is not in the list")
                return -1
            count = count + 1
            temp = temp.next
        return count

    def get(self, index):
        count = 0
        temp = self.head
        if temp is None:
            print("Index: ", index, " is not in this list")
            return None
        while count != index:
            if temp.next is None:
                print("Index: ", index, " is not in this list")
                return None
            count = count + 1
            temp = temp.next
        return temp.item

    def get_first(self):
        return self.head.item

    def get_last(self):
        t = self.head
        if self.head == None:
            return
        else:
            while t.next is not None:
                t = t.next
            return t.item

    def remove(self, index):
        if index <= 1:
            return None
        count = 0
        a = self.head
        while count != index - 1:
            if (a.next is not None):
                count = count + 1
                a = a.next
            else:
                break
        a.next = a.next.next

    def remove_first(self):
        a = self.head
        if self.head == None:
            return
        self.head = a.next

    def remove_last(self):
        a = self.head
        while a.next is not None:
            if a.next.next is None:
                a.next = None
                break
            a = a.next
        a = None

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next

        return count

    def is_empty(self):
        return self.head is None

    def print_list(self):
        print("LIST:")
        temp = self.head
        while temp is not None:
            print(temp.item)
            temp = temp.next

    def reverse(self):
        prev = None
        temp = self.head
        while (temp is not None):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def delete_duplicates(self):
        temp = self.head
        while temp.next is not None:
            if temp.item == temp.next.item:
                self.remove(self.getIndexOf(temp.item))
            temp = temp.next
