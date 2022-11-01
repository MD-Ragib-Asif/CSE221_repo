#4
#method 1 using bubble_sort
class PriorityQueue:
    def __init__(self):
        self.arr = []


    def enqueue(self, name, priority):
        self.arr.append([priority, name])
        # print('Before sort: ',self.arr)
        self.bubble_sort()
        

    def see_doctor(self):
        v = self.arr.pop(0)
        return v[1]

    # def print(self):
    #     print(self.arr)

    def bubble_sort(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-1-i):
                if self.arr[j][0] < self.arr[j+1][0]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        # print('After sort: ',self.arr)

with open('input4.txt', 'r') as f:
    a = f.read().split('\n')
obj1 = PriorityQueue()

with open('output4.txt', 'w') as file_out4:
    s4 = ''
    for i in a:
        if i.strip() == 'see doctor':
            value = obj1.see_doctor()
            s4 += value + '\n'
            
        else:
            i = i.split(" ")
            obj1.enqueue(i[0], int(i[1]))
    file_out4.write(s4)

    # obj1.print()


#----------------------------------------------------------

#method 2 using heap sort
#i still not understand the heap sort. That's why i have left it empty