
#2 (merge_sort)

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i,j,k = 0,0,0 


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1  

with open('input2.txt','r') as file_in2:
    inputs = file_in2.read().split('\n')

# print(inputs)

arr = [int(x) for x in inputs[1].split(' ') if x != '']

merge_sort(arr)

s = ''
for x in arr: 
    s += str(x) +' '

with open('output2.txt','w') as file_out2:
    file_out2.write(s)