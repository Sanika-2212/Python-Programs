def main():
    Ans = 0

    try:
        print("Enter First Number:-")
        No1 = int(input())

        print("Enter Second Number:-")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is Successfull")

    except ZeroDivisionError as zobj:
        print("Exception Occured Due to Second Operand is zero:",zobj)

    except ValueError as vobj:
        print("Exception Occured Due to Invalid Datatype:",vobj)

    except Exception as eobj:
        print("Exception Occured:",eobj)

    finally:
        print("Inside Finally Block...")
 
    print("Result is:-",Ans)

if __name__=="__main__":
    main()