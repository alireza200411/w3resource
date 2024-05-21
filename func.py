# practice 4 pynative
def show_employee(name : str , salary :int = 9000) -> str :
    return f'Name :{name} \nSalary: {salary}'

# ------------------------------------------------
# practice 8 
def del_REpeat(Mylist:list) -> list :
    data = ''.join(Mylist)
    for i in data:
        if data.count(i) > 1 :
            cont = data.count(i)
            data = data.replace(i,'',cont-1)
    return data    

# ------------------------------------------------
