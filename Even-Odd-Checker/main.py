
def userinput():
    while True:
        userinputs = input("ENTER YOUR NUMBER: ")

        if not userinputs.isdigit():
            print("INVALID NUMBER! TRY AGAIN")
            continue

        print("NUMBER ACCEPTED")
        break

    return int(userinputs)


def evenoddchecker():
    check = userinput()

    if check % 2 == 0:
        print("YOUR NUMBER IS EVEN")
    else:
        print("YOUR NUMBER IS ODD")


evenoddchecker()
