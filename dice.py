# practice 7 & 6
def squd(to : int) -> dict :
    dice = {}
    # to = int(input('enter the number : '))
    for counter in range(1 , to+1) :
        squ = counter ** 2
        dice[counter] = squ
    return dice

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

# -------------------------------------
# practice 10 
d1 = {'a' : 200 , 'b' : 100 , 'c' : 300}
d2 = {'a' : 100 , 'b' : 200 , 'd' : 400}
d3 =  {}
for data in d1 : 
    if data in d2 : 
        answer = d1[data] + d2[data]
        d3[data] = answer 
    else : 
        d3[data] = d1[data]
for i in d2 : 
    if i not in d3 : 
        d3[i] = d2[i]
# print(d3)

# -------------------------------------
# practice 43
        
counter = 7 
n = 3 
mainlist = []
for i in range(counter) : 
    mainlist.append([])

for lst in mainlist : 
    for j in range()