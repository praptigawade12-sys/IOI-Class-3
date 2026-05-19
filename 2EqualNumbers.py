def check_if_same(num1,num2):
    if ((num1 ^ num2) != 0):
        print("The numbers are not equal.")
    else:
        print("The numbers are equal.")

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
check_if_same(n1,n2)