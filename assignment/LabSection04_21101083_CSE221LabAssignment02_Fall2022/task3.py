#3 (Quick_sort)

def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    # print(i)
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], pivot = pivot, arr[i+1]
    # print(i)
    return i + 1

def quickSort(arr,l,h):
    if l < h:
        q = partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)

with open('input2.txt','r') as file_in3:
    inputs = file_in3.read().split('\n')

arr = [int(x) for x in inputs[1].split(' ') if x != '']
quickSort(arr,0,len(arr)-1)
s = ''
for x in arr: 
    s += str(x) +' '

with open('output3i.txt','w') as file_out3:
    file_out3.write(s)

def findk(arr,l,r,k):
 
    if (k > 0 and k <= r-l +1):
        p_index = partition(arr, l, r)

        if (p_index - l == k - 1):
            return arr[p_index]
        
        if (p_index - l > k - 1):
            return findk(arr, l, (p_index - 1), k)
 
        return findk(arr, p_index + 1, r, k)
    return 'out of  index'


with open('input3.txt','r') as file_in3b:
    inputs2 = file_in3b.read()

inputs2 = [x for x in inputs2.split('\n')]
arr = [int(x.strip()) for x in inputs2[0].split(':')[1].split(' ') if x.strip() != '']
k = [int(x.split('=')[-1].strip()) for x in inputs2[1:] if x.strip() != '']
# print(inputs2)
# print(arr)
# print(k)

s2 = ''

for x in k:
    s2 += str(findk(arr,0,len(arr)-1,x))+'\n'

with open('output3.txt','w') as file_out3b:
    file_out3b.write(s2)