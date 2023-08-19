from linked_list import LinkedList

list_1 = LinkedList()
for num in [1, 2, 2, 1]:
    list_1.append(num)

list_2 = LinkedList()
for num in [1, 2]:
    list_2.append(num)

def isPalindrome(linked_list):
    head = linked_list.head
    if not head:
        return True
    while linked_list.no > 1:
        if linked_list.popleft() != linked_list.pop():
            return False
    return True

assert isPalindrome(list_1)
assert not isPalindrome(list_2)