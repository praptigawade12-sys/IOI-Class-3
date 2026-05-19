def odd_occurring(arr):
    res = 0
    for e in arr:
        res = res^e

    return res

arr = []

n = int(input("Enter a the length of array: "))

while(n):
    num = int(input("Enter the array element:"))
    arr.append(num)
    n-=1

print(odd_occurring(arr))