def bubbleSort(arr):
    for i in range(len(arr)-1): 
        f = True    # This is a flag that will help to determine if the array is already sorted or not
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                f = False       # the flag gets changed if the array is not already sorted
        if f:       #when it is known that the array is already sorted then sorting is not required anymore so breaking out of the loop
            break

#for this function we know that the time complexity is O(n^2) because the number of iterations is n^2. But the way i changed the code is that i added a flag which will help to determine if the array is already sorted or not. If the array is already sorted then the flag will not change and the loop will break out. So the time complexity will be O(n) in the best case and O(n^2) in the worst case.

with open('input3.txt','r') as file_in3:
    inputs = file_in3.read()
    lst3=inputs.split('\n')

    with open('output3.txt','w') as file_out3:
        for i in lst3[1:]:
            lst3_1=i.strip(" ")
            lst3_2=[int(x) for x in lst3_1.split(" ")]
        bubbleSort(lst3_2)
        string3 = ''
        for j in lst3_2:
            string3 += str(j) + ' '
        file_out3.write(string3)