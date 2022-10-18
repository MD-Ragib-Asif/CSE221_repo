#1a
def even_odd_checker(n):
    if int(n)%2==0:
        return f'{n} is an Even number. \n'
    else:
        return f'{n} is an Odd number. \n'

with open('input1a.txt','r') as file_in:
    s=file_in.read()
    lst = [x for x in s.split('\n')]

    with open('output1a.txt', 'w') as file_out:
        for i in lst:
            # print(i)
            a = even_odd_checker(i)
            s2 = file_out.write(a)


#---------------------------------------------------------------------

#1b
def calculate(string):
    lst = [x for x in string.split(' ')]
    if lst[1]=='+':
        total = int(lst[0]) + int(lst[2])
    elif lst[1]=='-':
        total = int(lst[0]) - int(lst[2])
    elif lst[1]=='/':
        total = int(lst[0]) / int(lst[2])
    elif lst[1]=='*':
        total = int(lst[0]) * int(lst[2])
    return f'The result of {lst[0]} {lst[1]} {lst[2]} is {total} \n'

with open('input1b.txt', 'r') as file_in1:
    s3 = file_in1.read()
    lst2 = [x for x in s3.split('\n')]

    with open('output1b.txt', 'w') as file_out1:
        for i in lst2[1:]:
            # print(i)
            result = calculate(i.strip('calculate '))
            s4 = file_out1.write(result)
        