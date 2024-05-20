# practice 2 °
def dama(tipe : str) -> str :
    # tipe = input('enter the quantity type .C° or F° . ')

    if tipe == 'F' :
        tempelet = int(input('How many degrees Fahrenheit? '))
        conver = tempelet -32.5
        return(f'{conver}°C is {tempelet}°F')

    else :
        tempelet = int(input('How many degrees C? '))
        conver = tempelet/5 + 32
        return(f'{conver}°F is {tempelet}°C')
    
# print(dama('C'))    

# ----------------------------
# practice 43 
    
def zarb6() :
    for i in range(1,11) :
        answer = 9 * i
        print(f'9 x {i} = {answer}')

# zarb6()        

# -----------------------------
# practice 44
    
def print_number() :
    for i in range(10) :
        print(f'{i}' * i)    

# print_number()


# ------------------------------

# practice 11

import random
def matrix(rows : int , culomns:int) -> list :
    """This function takes the number of columns and rows from the user and produces a single line matrix."""

    mainlist = []
    for i in range(1 , rows+1) :
        destroy_list = []
        for j in range(1 , culomns+1) :
            ran = random.randint(0 , 10) 
            destroy_list.append(ran)
        else:
            mainlist.append(destroy_list)
    return(mainlist)        

# print(matrix(2 , 3) )   

# -----------------------------------
# practice pynative 12 
def fib(n:int) :    
    mylist = [] 
    num_1 = 0
    num_2 = 1
    res = num_1 + num_2
    for i in range(n) :
        mylist.append(res)
        num_1 = num_2
        num_2 = res
        res = num_1 + num_2

    return(mylist)    

# print(fib(55))