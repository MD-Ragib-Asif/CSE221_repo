#task 4
def function2(f):
    a, b = map(int, f.strip().split(" "))
    lst = []
    if a == 0 and b == 0:
        return
    for i in range(a, b+1):
        r = i**(1/2)
        r2 = int(r)
        if r2 == r:
            lst.append(i)
    # print(lst)

    return len(lst)


def function(f):
    inputs = f.strip().split("\n")
    string = ""
    for i in inputs:
        a = function2(i)
        if a != None:
            string += str(a) + "\n"

    return string

with open("input4.txt", "r") as filein4:
    a = function(filein4.read())
    with open("output4.txt", "w") as fileout4:
        fileout4.write(a)