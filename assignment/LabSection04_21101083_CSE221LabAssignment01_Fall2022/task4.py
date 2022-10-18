def insertion(arr:list,arr2):
    for i in range(0,len(arr)-1):
        temp = arr[i+1]
        temp2 = arr2[i+1]
        j= i
        while j>=0:
            if arr[j]>temp:
                arr[j+1] = arr[j]
                arr2[j+1] = arr2[j]
            else:
                break 	
            j= j-1      
        arr[j+1] = temp
        arr2[j+1] = temp2

def insertionRev(arr:list,arr2):
    for i in range(0,len(arr)-1):
        temp = arr[i+1]
        temp2 = arr2[i+1]
        j= i
        while j>=0:
            if arr[j]<temp:
                arr[j+1] = arr[j]
                arr2[j+1] = arr2[j]
            else:
                break 	
            j= j-1      
        arr[j+1] = temp
        arr2[j+1] = temp2

with open('input4.txt','r') as file_in4:
    inputs = file_in4.read()

    inputs = inputs.split('\n')[1:]
    roll_list = list(map(int, inputs[0].strip().split(' ')))
    mark_list = list(map(int, inputs[1].strip().split(' ')))


    insertion(roll_list,mark_list)
    insertionRev(mark_list,roll_list)
    # print(roll_list,mark_list)

    with open('output4.txt','w') as file_out4:
        for i in range(len(mark_list)):
            file_out4.write(f'ID: {roll_list[i]} Mark: {mark_list[i]} \n')
