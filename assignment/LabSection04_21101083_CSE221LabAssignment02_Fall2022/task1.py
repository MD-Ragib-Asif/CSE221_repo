#1 (decending order insertion sort)

def insertionRev(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
        
with open('input1.txt','r') as file_in1:
    inputs = file_in1.read()

inputs = inputs.split('\n')
roll = [int(x) for x in inputs[1].split(' ') if x != '']
mark= [int(x) for x in inputs[2].split(' ') if x != '' ]
dic = {}
for x in range(len(mark)):
    if mark[x] in dic.keys():
        dic[mark[x]]  += [roll[x]]
    else:
        dic[mark[x]]  = [roll[x]]

insertionRev(mark)
print(mark)

new_roll  = []
for x in mark:
    if x not in new_roll:
        new_roll += [x]

s = ''
for x in new_roll: 
    for i in dic[x]:
        # print(i)
        s += str(i) +' '

with open('output1.txt','w') as file_out1:
    file_out1.write(s+'\n')