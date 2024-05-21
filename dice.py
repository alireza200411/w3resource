# practice 7 & 6

# def squd(to : int) -> dict :

#     dice = {}

#     # to = int(input('enter the number : '))
#     for counter in range(1 , to+1) :
#         squ = counter ** 2
#         dice[counter] = squ
#     return dice

# print(squd(16))    

# -------------------------------------
# peactice 23
def frequency(counter: int) -> dict : 
    dic = {}
    mainlist = []
    # counter = int(input('enter the counter: '))
    for i in range(1 , counter + 1) : 
        print(f'Getting the {i} list data')
        sublist = []
        indx1 = input('enter the first element: ')
        indx2 = input('enter the second element: ')
        sublist.append(indx1)
        sublist.append(indx2)
        mainlist.append(sublist)
    orderlist = []
    orderlist.append(tuple(mainlist))
    # print(orderlist)
    for data in orderlist : 
        # print(type(data))
        for d in data : 
            # print(type(d))
            x = data.count(d)
            s = str(d)
            dic[s] = x

    return dic       

