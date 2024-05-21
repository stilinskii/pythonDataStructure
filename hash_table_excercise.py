import hash_table as ht
import re
if __name__ == '__main__':

    wArray = []
    with open('nyc_weather.csv','r') as f:
        for line in f:
            tokens = line.split(',')
            val = re.sub('[^0-9]', '', tokens[1])
            if val != "":
                wArray.append(val)

    print(wArray)

    #1. What was the average temperature in first week of Jan
    average_temperature = 0
    for i in range(6):
        average_temperature += int(wArray[i])
    average_temperature = average_temperature/7
    print(average_temperature)


    #2. What was the maximum temperature in first 10 days of Jan
    wArray.sort(reverse=True)
    print(wArray[0])


    t = ht.HashTable()
    with open('nyc_weather.csv', mode='r') as f:
        for line in f:
            tokens = line.split(',')
            key = tokens[0]
            val = tokens[1]
            t[key] = val

    print(t.arr)

    #3. What was the temperature on Jan 9?
    print(t["Jan 9"])
    #4. What was the temperature on Jan 4?
    print(t["Jan 4"])

    w_table = ht.HashTable()
    with open('poem.txt','r') as w:
        for line in w:
            tokens = line.split(" ")
            for word in tokens:
                word = word.strip()
                if w_table[word] is not None:
                    w_table[word] = int(w_table[word]) + 1
                else:
                    w_table[word] = 1

    print("'diverged' :" + str(w_table["diverged"]))
    print("'in' :" + str(w_table["in"]))
    print("'I' :" + str(w_table["I"]))
