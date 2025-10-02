# Positive, Negative, or Zero
# Write a program to check whether a number is positive, negative, or zero.

num = int(input())
if num > 0:
    print(num,"is positive number")
elif num < 0:
    print(num,"is negative number")
else:
    print("zero")



# Even or Odd
# Write a program to check if a number is even or odd.

num = int(input())
if num % 2 == 0:
    print("even")
else:
    print("odd")


# Maximum of Two Numbers
# Write a program to find the largest of two numbers.

A = int(input())
B = int(input())
if A > B:
    print(A,"is largest")
elif A < B:
    print(B,"is largest")
else:
    print("both are equall")