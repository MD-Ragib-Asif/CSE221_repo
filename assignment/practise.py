class PriorityQueue:
    def __init__(self):
        self.arr = []


    def enqueue(self, name, priority):
        self.arr.append([priority, name])
        self.pequeue()
    def see_doctor(self):
        v = self.arr.pop(0)
        print(v[1])

    def pequeue(self):
        for i in range(len(self.arr)):
            for j in range(i-1, -1, -1):
                if self.arr[j][0]< self.arr[j+1][0]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]



with open('input.txt', 'r') as f:
    a = f.read().split('\n')
obj1 = PriorityQueue()
for i in a:
    if i == 'see doctor':
        obj1.see_doctor()
    else:
        i = i.split(" ")
        obj1.enqueue(i[0], int(i[1]))

    

