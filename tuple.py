
def changer_type(data) -> any :
    """This function takes the value from the input and if the value is a number, it returns the number with its own type."""
    # data = input('enter number : ')
    if data.isalpha() == True :
        raise TypeError ("The given value is not a number..!")
    try:
        if '.' in data:
            data1 = float(data)
            return data1
        else:
            data1 = int(data)
            return data1
    except:
        pass
        return data
    
# --------------------------------------------
# practice 16 
def tup_to_dict (counter : int) -> dict :
    """"""
    list_I = []
    list_II = []
    dic_I = {}
    dic_I[1] = 'key'
    dic_I[2] = 'value'
    # counter = int(input('enter the counter : '))

    for i in range(1 , counter+1) :
        for n in range(1 , 3) :
            # tup = ()
            vorodi = input(f'enter the {dic_I[n]} : ')
            vorodi = changer_type(vorodi)
            print(type(vorodi))
            list_I.append(vorodi)
        else:
            tup = tuple(list_I)
            
            list_II.append(tup)
            del tup
            list_I = []
    dic_II = {}    
    # print(list_II)   
    for k , v in list_II :
        # print(item)
        dic_II[k] = v
    return dic_II

# -----------------------------
# practice 19 changed
# khat be khat
# counter = int(input('enter the counter: '))
datalist = []
# for i in range(counter):
    # sublist = []
    # for i2 in range(1 , 3) :
        # data = input(f'enter the data{i2}: ')
        # sublist.append(data)
    # else:
        # sublist = tuple(sublist)    
    # datalist.append(sublist)
# print(datalist)    
# dic = {}
# for j in datalist:
    # dic[j[0]] = j[1]
# print(dic)

# functional
def list_to_dict(counter:int):
    
    datalist = []
    for i in range(counter):
        sublist = []
        for i2 in range(1 , 3) :
            data = input(f'enter the data{i2}: ')
            sublist.append(data)
        else:
            sublist = tuple(sublist)    
        datalist.append(sublist)
    # print(datalist)    
    dic = {}
    for j in datalist:
        dic[j[0]] = j[1]
    return dic

# --------------------------------------------
# practice 31

# t = ((1, 2, 3, 4) ,(3, 5, 2, 1) ,(2, 2, 3, 1))
# mainlist = []
# for data in t : 
#     i = 0
#     sublist = []
#     while i < len(t) : 
#         sublist.append(data[i])
#         continue
#     else :

