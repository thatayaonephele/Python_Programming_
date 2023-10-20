def encoding_func():
    usr_input = input("Please enter a message you'd like to encode")
    for x in usr_input:
        print(ord(x),end=" ")
encoding_func()