hinp=int(input("Enter Height of Board : "))     
winp=int(input("Enter Width of Board : "))      #For taking input height and input width respectively

def board_draw(height,width):                   #Initializing a drawing function
    for j in range(0,height):                   #In this loop, the reverse shaped 'U's are drawn which contains - and |, according to count given
        print(" ---  "*width) 
        print("|   | "*width)
    print(" ---  "*width)                       # prints the last line of '---'

board_draw(hinp,winp)                           #draws board using the function
