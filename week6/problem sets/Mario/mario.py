from cs50 import get_int

while True:
    h = get_int("Height: ")
    if int(h) and h>0 and h<9 :
        break
for i in range(h):
    print(" "*(h-i-1),end="")
    print("#"*(i+1))
