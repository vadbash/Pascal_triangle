def zip(*args):
    length = min(len(element) for element in args)
    struct_list = [tuple(struct[i] for struct in map(list, args))
        for i in range(length)]
    return struct_list

pasclist = [0, 1, 0]
print('[0]')
for i in range(30):
    print(str(pasclist))
    pasclist = [sum(x) for x in zip([0]+pasclist, pasclist+[0])]
    for i in range(len(pasclist)):
        if pasclist[i]%2==1:
            pasclist[i] = 1 
        else:
            pasclist[i] = 0
    
