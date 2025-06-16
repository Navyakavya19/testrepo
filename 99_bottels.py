#String interpolation
#99 bottles of beer

for i in range(99, 0, -1):
    print(f"{i} bottles of beer on the wall")
    print(f"{i} bottles of beer")
    print(f"Take one down, pass it around")
    print(f"{i-1} bottles of beer on the wall\n")

if i == 1:
    print("No more bottles of beer on the wall")
    print("no more bottles of beer")
    print("Go to the store and buy some more.")
    print("99 bottles of beer on the wall....")