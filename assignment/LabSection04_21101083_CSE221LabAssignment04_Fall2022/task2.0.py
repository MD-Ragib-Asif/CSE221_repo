#task 2

class Queue:
    def __init__(self, arr, r_arr):
        self.arr = arr
        self.r = r_arr
    
    def de_queue(self):
        v = self.arr.pop(0)
        for i in self.r:
            if int(i[0]) == v:
                self.arr += [int(i[1])]
        return v

def graph(f):
    input = f.read().split('\n')
    c, r = map(int, input[0].strip().split())
    # print(c, r)

    roads = [input[i].strip().split(' ') for i in range(1, r+1)]
    # print(roads)
    
    default_array = [1]
    obj1 = Queue(default_array, roads)
    s = ''
    for i in range(r+1):
        value = obj1.de_queue()
        
        s += str(value) + ' '
        
    return s

with open('input2_1.txt', 'r') as file_in2_1:
    add = graph(file_in2_1)
    with open('output2_1.txt', 'w') as file_out2_1:
        file_out2_1.write(add)

with open('input2_2.txt', 'r') as file_in2_2:
    add2 = graph(file_in2_2)
    with open('output2_2.txt', 'w') as file_out2_2:
        file_out2_2.write(add2)

with open('input2_3.txt', 'r') as file_in2_3:
    add3 = graph(file_in2_3)
    with open('output2_3.txt', 'w') as file_out2_3:
        file_out2_3.write(add3)

with open('input2_4.txt', 'r') as file_in2_4:
    add4 = graph(file_in2_4)
    with open('output2_4.txt', 'w') as file_out2_4:
        file_out2_4.write(add4)