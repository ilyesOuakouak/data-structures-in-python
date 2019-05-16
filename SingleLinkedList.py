# Create the class node
class ListNode:
    def __init__(self, data):
        """Constructor to initiate this object"""

        # store data
        self.data = data

        # store the reference (next item)
        self.next = None
        return

    def has_value(self, value):
        """Method to compare the value with the node data"""
        if self.data == value:
            return True
        else:
            return False


# Create a SingleLinkedList class
class SingleLinkedList:
    def __init__(self):
        """Constructor to initiate this object"""
        self.head = None
        self.tail = None
        return

    # Create a method that adds a node to the list
    def add_item_to_list(self, item):
        """ add an item at the end of the list """
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    # Method to count the number of nodes in the list
    def list_length(self):
        """ Returns the number of nodes in the list """
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            # go to the linked node
            current_node = current_node.next
        return count

    # Method to output the value of a node
    def display_list_items(self):
        """ Output the value of a node """
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # go to the linked node
            current_node = current_node.next
        return

    # Method to search the linked list for a specific value
    def unordered_search(self, value):
        """ Search for a specific value """

        current_node = self.head
        # define position
        node_id = 1

        # define a list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next
            node_id += 1
        return results

    def remove_list_item_by_id(self, item_id):
        """ Remove an item according to the id given """
        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we d'ont have to look any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id += 1

        return


# a simple test

item1 = ListNode(13)
item2 = ListNode(25)
item3 = ListNode(72)
item4 = ListNode(42)
item5 = ListNode(25)

# Create a linked list
myLinkedList = SingleLinkedList()

# Add items to the list
myLinkedList.add_item_to_list(item1)
myLinkedList.add_item_to_list(item2)
myLinkedList.add_item_to_list(item3)
myLinkedList.add_item_to_list(item4)
myLinkedList.add_item_to_list(item5)

# Remove an item from the list
myLinkedList.remove_list_item_by_id(5)

print("length : %i" % myLinkedList.list_length())
print(myLinkedList.display_list_items())
# Search for an item in the list
print(myLinkedList.unordered_search(25))
