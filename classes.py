class Person : 
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age

    def display(self) : 
        print (f'im {self.name} and my age {self.age}')


class Car : 
    def __init__(self , model: str , brand , year: int) -> None:
        if type(model) == int : 
            model = str(model)
        self.Model = model
        self.Brand = brand
        self.Year = year
    def display(self) : 
        print(23 * '-')
        print(f'This car is a {self.Brand} product, an {self.Model} model, and it was made in {self.Year}.')    





def main() : 
    while True : 
        Q = input('Which object do you want?')
        if Q == Car : 
            Braand = input('')
            modell = input('')
            yeear = input('')
        else : 
            namee = input('enter your name : ')
            if namee == '' :
                print('good luck...!')
                break
            else :
                agee = input('enter your age : ')
                prs = Person(namee , agee)
                prs.display()



# if __name__ == '__main__':
#     main()

