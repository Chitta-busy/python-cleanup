#Accept two numbers and print the greatest between them.
n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))
if n1>n2:
    print(f"{n1} is greater than {n2}")
elif n1==n2:
    print(f"{n1} and {n2} are equal")
else:
    print(f"{n2} is greater than {n1}")
