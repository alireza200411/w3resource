# practice 72
def del_reapet(word:str , letter:str) -> str :
    spell_word = list(word)
    # letter = input('enter the letter : ')
    test = []
    # print(spell_word)
    for data in spell_word :
        if data == letter :
            test.append(data)
            answer = ''.join(test)
    else:
        return answer        
    
# ---------------------------------------------
# practice 112

# n1 = int( input('enter the first number : '))
# n2 = int(input('enter the second number : '))
# answer = n1 + n2
# print(f'(\'{n1}\' ,\'{n2}\') ->\'{answer}\' ')

# ----------------------------------------------
# practice 44
def address(word:str) -> int :
    """This function shows the address of the characters of a string in the output. To exit the execution of the function, just press the enter button when asking a question."""
    while True :
        adr = input('enter address or empty for canael. ')
        if adr == '' : 
            break
        else:
            if adr not in word :
                print(f'{adr} does not exist in the {word}.')

                continue
            else :
                if word.count(adr) > 1 :
                    answer1 = word.index(adr)
                    answer2= word.index(adr,answer1+1)
                    return(f'Current character {adr} position at {answer1} , {answer2}')
                else:
                    answer = word.index(adr)
                    return(f'Current character {adr} position at {answer}')
            
# --------------------------------------------
# practice 23
# functional
def remove_newline(phrase:str) -> str :
    if '\n' in phrase:
        new_string = phrase.replace('\n' , ' ')
        return(new_string)


