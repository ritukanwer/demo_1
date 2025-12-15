
def mian():
    try:
        a = int(input("enter a number :-"))
        print(a)
        return

    except:
        print("print a valid intc")
        return

    finally:
        print("i am inside in finally")

mian()

#     # finally code always executes, when function return(if we use function)
# 
