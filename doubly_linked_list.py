class Node:

    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class Doubly_linked_list:

    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,self.head,None)
        if self.head != None:
            self.head.previous = node
        self.head = node

    def get_item_by_index(self,index):
        if index >= self.get_length() or index < 0:
            raise Exception("out if index, index:" + str(self.get_length()))

        if index == 0:
            return self.head

        cnt = 0
        itr = self.head
        while itr:
            if cnt == index:
                return itr
            itr = itr.next
            cnt += 1


    def print(self):
        if self.head is None:
            print("list is Empty")
            return

        itr = self.head
        str_data = ""
        while itr:
            str_data += str(itr.data) +" <----> "

            itr = itr.next

        print(str_data)

    def insert_at_end(self, data):
        if self.head == None:
            node = Node(data,None,None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data,None,itr)
        itr.next = node

    def print_reverse(self):
        if self.head == None:
            raise Exception("no element in the list")

        itr = self.head
        while itr.next:
            itr = itr.next

        list_str = ""
        while itr:
            list_str += str(itr.data) + "<===>"
            itr = itr.previous

        print(list_str)


    def get_length(self):
        if self.head == None:
            return 0

        cnt = 0
        itr = self.head
        while itr:
            cnt += 1
            itr= itr.next

        return cnt


    def insert_values(self, data_list):
        if self.head == None :
            previous = self.head
            for idx,data in enumerate(data_list):
                if idx == 0:
                    node = Node(data,None,None)
                    self.head = node
                    previous = node
                else:
                    node = Node(data,None,previous)
                    previous.next=node
                    previous=node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            for data in data_list:
                node = Node(data,None,itr)
                itr.next = node
                itr = node

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("out of index")

        itr = self.head
        if index == 0:
            itr.next.previous = None
            self.head = itr.next
            itr.next = None

        cnt = 0
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next
                itr.next.next.previous = itr.next
            itr = itr.next
            cnt += 1


    # todo need to review
    def insert_at(self,index,data):
        if index < 0 and index >= self.get_length():
            raise Exception("out of index")

        if index == 0:
            self.insert_at_begining(data)
            return

        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                node = Node(data,itr.next,itr)
                if itr.next:
                    itr.next.previous = node
                itr.next = node
                break
            cnt += 1
            itr = itr.next


    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next,itr)
                if itr.next:
                    itr.next.previous = node
                itr.next = node
                break
            itr=itr.next

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
            itr.next.previous = None
            itr.next = None
            return

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next != None :
                    itr.next.previous = itr
                break
            itr = itr.next

    # def get_last_node(self):

if __name__ == '__main__':
    dl = Doubly_linked_list()
    # dl.insert_at_begining(2)
    # dl.insert_at_end(3)
    # dl.insert_at_end(5)
    # dl.print()
    # dl.print_reverse()
    # print(dl.get_item_by_index(0).data)
    # # print(dl.get_item_by_index(1).previous.data)
    # print(dl.get_length())
    dl.insert_at_begining(4)
    dl.insert_at_end(3)
    dl.insert_values(["d","g","dg"])
    dl.print()
    dl.print_reverse()
    dl.remove_by_value("d")
    dl.print()
    dl.insert_at(4,"good")
    dl.print()
    dl.insert_after_value("good","girl")
    dl.print()