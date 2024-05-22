from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,key):
        self.container.append(key)

    def pop(self):
        pop = self.container.pop()
        # print(pop)
        return pop

    def peek(self):
        container_ = self.container[-1]
        print(container_)
        return container_

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)



if __name__ == '__main__':
    s = Stack()
    s.push("jj")
    print(s.size())
    s.peek()
    s.pop()


    def reverse_string(value):
        st = Stack()
        for char in value:
            st.push(char)

        returnValue = ""

        while st.size() != 0:
            returnValue += st.pop()

        return returnValue

    print(reverse_string("We will conquer COVID-19"))

    def is_balanced(value):
        st = Stack()
        match_dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        open = "{(["
        close = "})]"
        for char in value:
            if char in open:
                st.push(char)
                continue
            if char in close:
                if st.size() == 0 or match_dict[st.pop()] != char:
                    print(False)
                    return False

        is_balanced_return = (st.size() == 0)
        print(is_balanced_return)
        return is_balanced_return

    is_balanced("({a+b})")
    is_balanced("))((a+b}{")
    is_balanced("00))")

