class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.no = 0 # 링크드 리스트의 길이
        self.head = None # 머리 노드
        self.current = None # 이터레이터에서 사용될 변수

    # iterator로 만들기 위한 메서드
    def __iter__(self):
        self.current = self.head
        return self
    
    # itertator로 만들었을때 다음 요소를 알려주거나 중단함
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

    # print 했을 때 str로 반환
    def __str__(self):
        pointer = self.head
        if pointer is None:
            return ''
        result = ''
        while pointer is not None:
            result += f'{pointer.data} → '
            pointer = pointer.next
        return result.rstrip(' → ')
    
    # len()에서 동작하게 해줌
    def __len__(self):
        return self.no
    
    # in 에서 동작하게 해줌
    def __contains__(self, data):
        return True if self.search(data) >= 0 else False
    
    def search(self, data):
        """입력값과 같은 첫번째 요소의 위치를 리턴하고, 없을 시 -1을 리턴"""
        count = 0
        pointer = self.head
        while pointer is not None:
            if pointer.data == data:
                return count
            count += 1
            pointer = pointer.next
        return -1
    
    def add_first(self, data):
        """첫번째 위치에 노드를 추가"""
        pointer = self.head
        self.head = Node(data, pointer)
        self.no += 1
    
    def add_last(self, data):
        """마지막 위치에 노드를 추가"""
        pointer = self.head
        if pointer is None:
            self.add_first(data)
            return
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = Node(data, None)
        self.no += 1

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.no -= 1 
    
    def remove_last(self):
        if self.head.next is None:
            self.remove_first()
        else:
            cur_pointer = self.head
            pre_pointer = self.head
            while cur_pointer.next is not None:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next
            pre_pointer.next = None
            self.no -= 1
    
    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.remove_first()
                return True
            
            pointer = self.head
            while pointer.next is not None:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    return True
                pointer = pointer.next
        return False
    
    def append(self, data):
        self.add_last(data)

    def popleft(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            self.no -= 1
        return data
    
    def pop(self):
        if self.head.next is None:
            data = self.popleft()
        else:
            cur_pointer = self.head
            pre_pointer = self.head
            while cur_pointer.next is not None:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next
            data = cur_pointer.data
            pre_pointer.next = None
            self.no -= 1
        return data

linked_list = LinkedList()

for i in [1,2,3,4,5]:
    linked_list.add_last(i)
print('add last 1,2,3,4,5 : ', linked_list)

linked_list.append(6)
print('append 6 : ', linked_list)

linked_list.add_first(0)
print('add first 0 : ', linked_list)

print('len : ', len(linked_list))

print('current linked_list : ', linked_list)
print('serch 3 : ', linked_list.search(3))
print('serch 7 : ', linked_list.search(7))

print('current linked_list : ', linked_list)
print('3 in : ', 3 in linked_list)
print('7 in : ', 7 in linked_list)

linked_list.remove_first()
print('remove first : ', linked_list)
linked_list.remove_last()
print('remove last : ', linked_list)
print('remove 3 : ', linked_list.remove(3))
print('remove 6 : ', linked_list.remove(6))

print('current linked_list : ', linked_list)
print('popleft ', linked_list.popleft())
print('pop ', linked_list.pop())

print('current linked_list : ', linked_list)
print('for i in linked_list:')
for i in linked_list:
    print(i)
