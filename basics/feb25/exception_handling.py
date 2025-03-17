if __name__ == "__main__":
    try:
        number1 = int(input("Enter number 1:  "))
        number2 = int(input("Enter number 2:  "))
        print(number1 + number2)
    except Exception as e:
        print("Invalid Values Entered")
        print(e)
    finally:
        print("bye..")

