#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(1) due to absence of dynamic factors. Running time is therefore constant."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(1) because appending takes constant time."""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) because extending takes linear time. n = length of list being added. I don't actually understand this conceptually. This answer is based on the Python Wiki. https://wiki.python.org/moin/TimeComplexity"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n^2) because the running time is directly dependent on the number of buckets and the number of key-value entries in each of those buckets. (Not certain about this one)"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        entry_count = 0 #initialize this leetle counter
        for bucket in self.buckets:
            entry_count += bucket.length()
        return entry_count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Best case running time: O(1) because of the if loop. n = average length of lists (load factor: [# of key, value entries]/[# of buckets]). This best case will stand if we're looking for an item at or near the head node.
        TODO: Worst case running time: O(n) because of the while loop. This worst case will stand if we're looking for an item at or near the tail node. When looking at the while and if loops together, the runtime is O(n + 1), which is simplified to O(n) because of the relative small size of the constant."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        current_node = bucket.head
        while current_node is not None:
            if current_node.data[0] == key: # [0] for key and [1] for value bc tuple inside node.data
                return True
            current_node = current_node.next # Set to next node so that while loop continues
        return False #false is returned if current_node is None OR if node.data[0] !== key

    def get(self, key): #Running time: same as contains
        """Return the value associated with the given key, or raise KeyError.
        TODO: Best case running time: [O(1) if the target node is located at or near the head node. This function must loop through the nodes in the bucket until it finds a match, so proximity to the head node yields shorter runtime]; [O[1] if key is not found. A KeyError is raised; this takes constant time because no dynamic input is required.]
        TODO: Worst case running time: O(n) if the target node is located at or near the head node OR does not exist. Since the function must loop through a great quantity of nodes to either find the matching node or to ascertain the absence of such a match, greater runtime is required.
        WORTH NOTING: Similar logic implemented in algorithmic analysis for both this get function and the contains function directly above"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        current_node = bucket.head
        while current_node is not None:
            return current_node.data[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Best case running time: [O(1) should the conditions of the if statement not be met. The function will append the (key, value) pair to bucket. This takes constant time]; [O(1) should the conditions of the if statement be met AND should the target node be at or near the head node. Fewer nodes to loop through --> decreased runtime.]
        TODO: Worst case running time: O(n) should the conditions of the if statement be met AND should the target node be at or near the tail node. More nodes to loop through --> increased runtime."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket.find(lambda tuple: tuple[0] == key) is not None:
            node = bucket.find_node(lambda tuple: tuple[0] == key)
            node.data = (key, value)
        else:
            bucket.append((key, value))

        # index = self._bucket_index(key)
        # bucket = self.buckets[index]
        # current_node = bucket.head
        # if bucket.is_empty() and bucket.head is None:
        #     bucket.append((key, value))
        # elif bucket.find(lambda item: item == current_node.data):
        #     # print("HEY YOU YOU SMELL LIKE PANCAKES")
        #     while current_node.data[0] != key:
        #         current_node = current_node.next
        #         if current_node == bucket.tail:
        #             bucket.append((key, value))
        #             break
        #     current_node.data = (key, value)
        # else:
        #     raise KeyError('key not found lol')

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Best case running time: [O[1] should the conditions of the if statement not be met. The function raises KeyError, which requires no dynamically changing variable input and thus requires constant runtime]; [O[1] should the conditions of the if statement be met AND should the target node be at or near the head node. Fewer nodes to loop through --> decreased runtime]
        TODO: Worst case running time: O(n) should the conditions of the if statement be met AND should the target node be at or near the tail node. More nodes to loop through --> increased runtime """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket.find(lambda tuple: tuple[0] == key) is not None:
            node = bucket.find_node(lambda tuple: tuple[0] == key)
            bucket.delete(node.data)
        else:
            raise KeyError("Key not found: {}".format(key))

        # index = self._bucket_index(key)
        # bucket = self.buckets[index]
        # current_node = bucket.head
        # # current_node = bucket.find(lambda data: data[0] == key)
        # if current_node is None:
        #     raise KeyError('Deletion failed. Key not found: {}'.format())
        # else:
        #     bucket.delete(current_node)

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10), ('X', 11)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
