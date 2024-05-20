# X = lambda x : x + 15
# Z = lambda X , y : X*y
# print(X(5))
# print(Z(X, 6))

# z = lambda x , y : f'{x} times {y} = {x*y}'
# print(z(2 , 15))

# -------------------------------------------------

# dick = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# c = sorted(dick , key= lambda x : x['color'])
# print(c)


# mylist = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# l = sorted(mylist , key= lambda x :x[1])
# print(l)


# practice 21

# a = int(input('enter the number : '))

# lst = [2 , 4  , 6 , 9 , 11]

# l = list(map(lambda x : x * a , lst ))
# print(l)

def func(x : list , y : list) :
    lst = []
    if len(x) < len(y) :

        for data in y :
            if data in x :
                lst.append(data)
    else : 
        for data in x :
            if data in y : 
                lst.append(data)

    return lst


mylist1 = [1, 2, 3, 5, 7, 8, 9, 10]
mylist2 = [1, 2, 4, 8, 9]

# c = filter(func , mylist1 , mylist2)    
# print(c)

print(type(func))