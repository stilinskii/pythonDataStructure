class HashTableLinearVer:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
            return

        slot = self.find_slot(h, key)
        self.arr[slot] = (key,value)

    def find_slot(self,index,key):
        prob_index = self.get_prob_range(index)
        for index in prob_index:
            if self.arr[index] is None or self.arr[index][0] == key:
                return index
        raise Exception("HashMap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        range = self.get_prob_range(h)
        for idx in range:
            if self.arr[idx] is not None:
                if self.arr[idx][0] == key:
                    self.arr[idx] = None

            # in the answer of this practice has this part
            # but it's wrong
            # bc if you try to delete the value with same hash key
            # after deleting the value that was inserted firstly among the values that have same hash key
            # the value which was inserted not firstly is not going to be deleted
            #
            # if self.arr[idx] is None:
            #     return

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return

        if self.arr[h][0] == key:
            return self.arr[h][1]

        prob_index = self.get_prob_range(h)
        for idx in prob_index:
            if self.arr[idx][0] == key:
                return self.arr[idx][1]


    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]

if __name__ == '__main__':
    t = HashTableLinearVer()
    print(t.get_hash("march 6"))
    print(t.get_hash("g"))
    print(t.get_hash("5"))
    print(t.get_hash("6"))
    t["g"]=7
    t["5"]=0
    t["march 6"] = 1
    t["gj"] = 3
    t["march whatever"] = 4
    t["6"] = 9
    print(t.arr)
    print(t["5"])
    del t["g"]
    del t["5"]
    print(t.arr)
