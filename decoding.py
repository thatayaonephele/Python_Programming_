"""
#The program works proper now. Can be improved if we allow delimeter to be eith , OR " "
def decoder_func_2():
    usr_input = (input("Please enter a sequence of Unicode numbers")).split(",")
    for x in usr_input:
        output = int(x)
        print(chr(output),end=" ")
decoder_func_2()



#The problem with this code, it only works for 1 strings not multiple strings
#The could will crash if the number is out of range of the unicode digits

def decoder_func():
    usr_input = (input("Please enter a sequence of Unicode numbers"))
    i = 0
    while i < len(usr_input):
        temp = int(usr_input)
        print(f"The unicode converted is: {chr(temp)}",end=" ")
        i += 1
decoder_func()

    y = len(usr_input)
    z = int(usr_input)
    print(chr(z))

    for x in usr_input:
        input_list.append((x))
#    for y in input_list:
        print(input_list,end=" ")
"""

#The program works proper now. Can be improved if we allow delimeter to be eith , OR " "
def decoder_func_2():
    usr_input = (input("Please enter a sequence of Unicode numbers: ")).split(" ")
    for x in usr_input:
        output = int(x)
        print(chr(output), end=" ")
decoder_func_2()

#NB: My input is different from what I expect to get?