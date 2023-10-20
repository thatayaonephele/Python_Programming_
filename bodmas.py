def bodmath_func():
    prompt_user_msg = "Please answer the following questions in 60s:"
    attempts = 0
    correct_ans = "Well done, next question..."
    print(prompt_user_msg)
    ans1 = input("abs(4 - 20 //3)**3?")
    while ans1 != 8:
        print(prompt_user_msg)ans1 = input("")
        attempts+= 1
        if attempts == 3:
            print("Oops, your answer was incorrect again")
            break
    else:
        print(correct_ans)
bodmath_func()