#range(stop)             # 0 up to stop-1
#range(start, stop)      # start up to stop-1
#range(start, stop, step)# start, jumping by step

#list(range(5))         # [0, 1, 2, 3, 4]
#list(range(1,6))       # [1, 2, 3, 4, 5]
#list(range(0,10,2))   # [0, 2, 4, 6, 8]

for i in range(1, 6):
    print(i,end=' ')

print("\n")
name = "Chitta"

# Method 1 — via index
for i in range(len(name)):
    print(name[i],end="")
print("\n")
# Method 2 — direct (simpler!)
for char in name:
    print(char,end="")