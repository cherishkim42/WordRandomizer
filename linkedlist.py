#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    #In all algorithmic analyses, n = number of nodes, or items, in linked list

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self): #O(1), checking if self.head == None, constant time
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) because of incremented numerical variable in for loop. The returned counter is directly proportional to the number of loops required. If this function instead returned value of a .size property, it could have an algorithmic analysis of 0(1). Analogically, the presented function is driving a car, while opting to return value of a .size property is teleportation."""
        counter = 0 #initialize counter
        for item in self.items():
            counter += 1
        return counter

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because this function is not dependent on any dynamic factors. Simply change tail.next and .tail"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node #If a linked list has 1 item, the node refers to tail as well as head
        else: #Linked list isn't empty
            self.tail.next = node #Previous tail points us in the direction of new node
            self.tail = node #Set tail to node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because this function is not dependent on any dynamic factors. Simply change .head and node.next. The reasoning here is identical to that of the append function directly above"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else: #Linked list isn't empty
            node.next = self.head
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) if looking for item at or near head node because it doesn't need to check through numerous individual nodes before reaching the item where quality(item) is True
        TODO: Worst case running time: O(n) if looking for item at or near tail OR not in list at all. This would necessitate looping through many individual nodes, thereby increasing running time"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None

    def find_node(self, quality):
        node = self.head
        while node is not None:
            if quality(node.data):
                return node
            else:
                node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) if [self.is_empty() because it is a single step with constant runtime] OR [the node whose data matches given item is at or near head node. This means traversing through relatively few nodes and requiring a constant amount of running time]
        TODO: Worst case running time: O(n) if the node whose data matches given item is at or near tail OR not in list at all. The function needs to keep looping until it lands on the target node, and this drives up running timeself.
        WORTH NOTING: The reasoning for delete function's best and worst running times are just like those of the find function (directly above), except for the option of NO (or 0) running time in delete function, because no analagous "if" statement exists in the find function."""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
            raise ValueError("Linked list is empty")

        if self.head.data == item: #Checks if linked list contains only one word
            self.head = self.head.next #Set forward
            if self.tail.data == item:
                self.tail = None
            return

        current_node = self.head
        previous_node = None
        while current_node: #Checks all nodes in list until current_node.data is equal to passed-in argument item
            if current_node.data != item:
                previous_node = current_node
                current_node = current_node.next
            else:
                if self.tail.data == item: #Dingdingding they're the same! Set previous node to None and reinitialize tail
                    if previous_node:
                        previous_node.next = None
                        self.tail = previous_node
                        return
                    else:
                        self.head = None
                        self.tail = None
                        return
                else:
                    previous_node.next = current_node.next
                    return
        raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
