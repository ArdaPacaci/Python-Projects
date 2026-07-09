import math
mynumber=int(input("enter a number:"))
square_root=math.sqrt(mynumber)


if(square_root==int(square_root)):
    print(f"The square root of {mynumber} is an integer: {int(square_root)}")
else:
    print(f"the square root of {mynumber} is not an integer: {int(square_root)}")
