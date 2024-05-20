class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        # 100 is the size of hash table i will make
        return h % self.MAX

    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    ## todo review
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                # element[1] = val <== it's impossible to do so bc Tuple is immutable
                # so instead insert the new key value pair
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            #if key is not exists
            # append Tuple
            self.arr[h].append((key,val))



    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]



if __name__ == '__main__':
    t = HashTable()
    print(t.get_hash("gj"))
    print(t.get_hash("march 50"))
    print(t.get_hash("march 6"))
    t["march 6"] = 190
    print(t["march 6"])
    t["march 17"] = 180
    t["gj"] = 188
    print(t["march 17"])
    print(t.arr)
    del t["gj"]
    print(t.arr)
    print(t["gj"])
    print(t["march 6"])






