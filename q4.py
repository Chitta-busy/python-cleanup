#Accept name and age — check if the user is a valid voter (18+).
a=input("Enter your Name:")
n=int(input("Enter your Age:"))
if n==18 or n>18:
    print("Hello",a,", you are a valid voter✅")
else:
    print("Hello",a,", you are not a valid voter❌")