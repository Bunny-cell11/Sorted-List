from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merges two sorted linked lists.

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    current = dummy

    # Iterate while both lists have elements
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one of the lists is exhausted, append the remaining elements of the other list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # The merged list starts from the next of the dummy node
    return dummy.next

# Helper function to create a linked list from a Python list
def createLinkedList(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head: Optional[ListNode]):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))

# Example Usage:
if __name__ == "__main__":
    list1_arr = [1, 2, 4]
    list2_arr = [1, 3, 4]
    list1 = createLinkedList(list1_arr)
    list2 = createLinkedList(list2_arr)

    print("List 1:")
    printLinkedList(list1)
    print("List 2:")
    printLinkedList(list2)

    merged_list = mergeTwoLists(list1, list2)
    print("Merged Sorted List:")
    printLinkedList(merged_list)

    list3_arr = []
    list4_arr = [0]
    list3 = createLinkedList(list3_arr)
    list4 = createLinkedList(list4_arr)

    print("\nList 3:")
    printLinkedList(list3)
    print("List 4:")
    printLinkedList(list4)

    merged_list2 = mergeTwoLists(list3, list4)
    print("Merged Sorted List 2:")
    printLinkedList(merged_list2)
