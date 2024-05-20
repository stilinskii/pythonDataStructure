class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        mem = self.head
        while mem.next:
            mem = mem.next

        mem.next = Node(data,None)

    def get_length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next

        return length

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data);

    def remove_at_answer_ver(self,index):
        if self.get_length()-1 < index or 0 > index:
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def remove_at(self,index):
        # if length-1 < index then return
        if self.get_length()-1 < index or 0 > index:
            raise Exception("invalid index")

        # if index = 0
        if index == 0:
            removed = self.head
            itr = removed.next
            removed.next = None
            self.head = itr
            return removed

        # else then loop through the list
        cnt = 0
        itr = self.head
        while itr.next:
            if cnt == index-1:
                removed = itr.next
                itr.next = itr.next.next
                return removed.data
            itr = itr.next
            cnt += 1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")

        if index == 0:
            node = Node(data,self.head)
            self.head = node
            return

        cnt = 0
        itr = self.head
        while itr:
            if cnt == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            cnt += 1

    def insert_after_value(self, data_after,data_to_insert):
        #추가
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                return
            itr = itr.next

        print("no data [" + data_after + "]")

    def remove_by_value(self, data):
        if self.head is None:
            return

        itr = self.head
        if itr.data == data:
            self.head = itr.next
            itr.next = None
            return

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        print("no data [" + data + "]")

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["ba","bo","ha"])
    ll.print()
    print(ll.get_length())
    # print(ll.remove_at(2))
    ll.insert_at(3,"figs")
    ll.print()

    ll.insert_after_value("figs","ru")
    ll.print()

    ll.remove_by_value("ba")
    ll.print()