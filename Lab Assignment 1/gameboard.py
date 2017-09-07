hinp=int(input("Enter Height of Board : "))
winp=int(input("Enter Width of Board : "))

def board_draw(height,width):
    i=0

    for j in range(0,height):
        print(" ---  "*width)
        print("|   | "*width)
    print(" ---  "*width)

board_draw(hinp,winp)