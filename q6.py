#Accept temperature in °C and print a description.
t=int(input("Enter temperature in °C:"))
if t<0:
    print("Freezing ❄️")
elif t>=0 and t<10:
    print("Cold 🥶")
elif t>=10 and t<25:
    print("Pleasant 😊")
else:
    print("Hot 🥵")