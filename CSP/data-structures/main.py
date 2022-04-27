#Stack data structure

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def _isempty(self):
        return not bool(self.items)

    def peek(self):
        if self._isempty():
            return self.items[-1]

#
#Stack data structure examples
#

#bracket parsing

bracket_match = {
    "(":")",
    "{":"}",
    "[":"]"
}

def parse_brackets(string):
    stack = Stack()

    for char in string:
        if char in "([{":
            stack.push(char)
        else:
            if char in ")]}":
                if not stack._isempty():
                    s_top = stack.pop()
                    if not bracket_match[s_top] == char:
                        return False
                else:
                    return False
            

    return stack._isempty()

#print(parse_brackets("print([f'hello {username}'])"))
#print(parse_brackets("print('whoops'"))

#string reversing

def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)
    
    astr = ""

    for x in range(len(string)):
        astr += (stack.pop())
    
    return astr

#print(reverse_string("ABCDEFGHI LOL 2D"))

# div by 2 int to bin converter

def int_to_bin(num):
    stack = Stack()

    while num / 2 > 0:
        remainder = num % 2
        num //= 2
        stack.push(remainder)

    binstr = ""
    while not stack._isempty():
        binstr += str(stack.pop())
    
    return binstr

#print(int_to_bin(70))

#
# Singly Linked Lists
#

# Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"[{self.data}]"

# NodeException

class NodeException(Exception):
    pass

# LinkedList

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insertion Methods

    def append(self, data): # add
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
            raise NodeException("Previous Node does not exist.")
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    #finding methods

    def _find_node(self, key):
        cur_node = self.head
        while cur_node.data != key:
            cur_node = cur_node.next
        return cur_node.data
    
    def _find_node_pos(self, pos):
        cur_node = self.head
        for x in range(pos):
            cur_node = cur_node.next
        return cur_node

    #deletion methods

    def delete(self, key):
        cur_node = self.head

        if cur_node:
            if cur_node.data == key:
                self.head = cur_node.next
                cur_node = None
                return
            else:
                prev = None

                while cur_node and cur_node.data != key:
                    prev_node = cur_node
                    cur_node = cur_node.next
                
                if cur_node is None:
                    return

                prev_node.next = cur_node.next
                cur_node = None
                return
    
    def delpos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.delete(self.head.data)
            else:
                prev_node = None
                for x in range(pos):
                   prev_node = cur_node
                   cur_node = cur_node.next
            
            if cur_node is None:
                return
            
            prev_node.next = cur_node.next
            cur_node = None
            return
    
    #length method

    def len(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_recur(self, node=None):
        if node is None:
            return 0
        return 1 + self.len_recur(node.next)

    #representation method

    def __repr__(self):
        cur_node = self.head
        repr_str = "<"

        while cur_node:
            repr_str += "[" + cur_node.data + "]->"
            cur_node = cur_node.next
        
        return repr_str[:-2] + ">"

linklist = LinkedList()

linklist.append("A")
linklist.append("B")
linklist.append("C")
linklist.append("D")

print(linklist)