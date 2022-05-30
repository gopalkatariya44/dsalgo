from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order \n
    - Recursively divide the linked list into sublists containing a single node\n
    - Repeatedly mearge the sublists to produce sorted sublists until one remains\n

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges tow linked lists, sorting by data in nodes\n
    Returns a new, merged list
    """
    # create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # Add fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tial node of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to meraged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linlked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtian node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # if data on left is gretedr than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move right head to next node
        current = current.next_node
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(1)
l.add(10)
l.add(40)
l.add(3)
l.add(33)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
