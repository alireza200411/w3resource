# practice 107 
import random
def remover(lenth : int , counter : int , dell : int) -> list :
    """     lenth -> How long is each list? 

     counter -> How many lists do you have in mind?

     dell -> Enter the column you want to delete
     """
    # lenth = int(input('How long is each list? '))
    # counter = int(input('How many lists do you have in mind? '))
    # dell = int(input('Enter the column you want to delete : '))
    dell = dell - 1
    mother_list = []
    for i in range(1 , counter+1) :
        test = []
        for i_2 in range(1 , lenth+1) :
            shu = random.randint(-9,10)
            test.append(shu)
        else:
            mother_list.append(test)
    print("Original Nested list:")        
    print(mother_list)
    # cp = mother_list
    for data in mother_list :
        data.remove(data[dell])
    print(f"After removing {dell} column:") 
    print(mother_list) 
    return 'end'

# d = {'dell' : 2 , 'lenth' : 3 , 'counter' : 5  }    
# print(remover(**d))

#  ---------------------------------------------
# practice 17

def prime(data:list[int]) -> bool :
    """This function identifies prime numbers in the list and returns false if there is a composite number in the list, even zero and one."""
    for i in data :
        if i == 1 or i == 0  :
            return(f'({data}) -> False')
        else :
            for j in range(2 , i) :
                if i%j == 0 :
                    return(f'({data}) -> False') 
                else : 
                    return(f'({data}) -> True')    
                
# print(prime([3, 4, 7, 9]))

# -------------------------------------------------
# practice 58

def change_list(firstlist :list , secondlist :list ,n:int=1) -> list :
    """"""
    m = n * -1
    firstlist[m:] = secondlist
    return firstlist 


print(change_list([1,2,3,4,5,'a' , True] , [6 , 7 , 8 , 9] , 2))

# ----------------------------------------------------
# practice 35

# mylist = ['p' , 'q']
# n = 5
# for data in mylist :    
#     for i in range(1 , n+1) :
#         data = 




    
  