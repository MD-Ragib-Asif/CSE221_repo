with open('input5.txt','r') as file_in5:
    inputs = file_in5.read()

    inputs = inputs.split('\n')[1:]



    dic = {}

    for x in inputs:
        y = x.strip().split(' ')
        key = y[0] 
        t = y[-1].split(':')
        value = float(t[0]+'.'+t[1])
        # print(key, t, value)
        if key not in dic.keys():
            dic[key] = [[value,y[4],y[-1]]]
        else :
            dic[key].append([value,y[4],y[-1]])

    with open('output5.txt','w') as file_out5:
        for x in sorted(dic):
            # print(x, dic[x])
            for y in sorted(dic[x],reverse=1):
                # print(y)
                file_out5.write(f'{x} will departure for {y[1]} at {y[-1]} \n')