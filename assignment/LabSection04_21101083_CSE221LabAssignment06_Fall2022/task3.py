#task 3
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def function(f):
    inputs = f.split("\n")
    th = [int(x) for x in inputs[1].strip().split(" ")]
    # print(th)
    ths = insertion_sort(th)
    # print(ths)
    string = ""
    jtl =[]
    jtl2 = []
    
    for i in inputs[2]:
        if i == "J":
            a = ths.pop(0)
            string += str(a)
            jtl.append(a)

        else:
            count = 0
            idx = len(jtl) - 1
            while count < 1:
                if jtl[idx] in jtl2:
                    idx -= 1
                else:
                    jtl2.append(jtl[idx])
                    string += str(jtl[idx])
                    count += 1
                idx -= 1
    # print(jtl)
    # print(jtl2)

    f_string = ""
    f_string += string + "\n"
    f_string += f'Jack will work for {sum(jtl)} hours \nJill will work for {sum(jtl2)} hours'

    return f_string
    
    
with open("input3_1.txt", "r") as filein3_1:
    a = function(filein3_1.read())
    with open("output3_1.txt", "w") as fileout3_1:
        fileout3_1.write(a)

with open("input3_2.txt", "r") as filein3_2:
    a2 = function(filein3_2.read())
    with open("output3_2.txt", "w") as fileout3_2:
        fileout3_2.write(a2)