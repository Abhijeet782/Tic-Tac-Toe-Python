p1,p2=[],[]
l = []
for i in range(0,9):
    p1.append(0)
    p2.append(0)
    l.append(0)

flag = 0
print(' 1 | 2 | 3 ')
print(' - | - | - ')
print(' 4 | 5 | 6 ')
print(' - | - | - ')
print(' 7 | 8 | 9 ')
print("PLAYER 1 -> X ")
print("PLAYER 2 -> O ")
print("--------------")
for i in range(0,9):
    print('',l[0],'|',l[1],'|',l[2])
    print(' - | - | - ')
    print('',l[3],'|',l[4],'|',l[5])
    print(' - | - | - ')
    print('',l[6],'|',l[7],'|',l[8])
    
    if i%2==0:
        print("Player 1 : Enter the position ")
        n = int(input())
        while l[n-1] == 'X' or l[n-1] == 'O':
            print("This position is already in used")
            n = int(input())
        
        p1[n-1] = 1
        l[n-1] = 'X'

        #Horizontal
        if p1[0]==1 and p1[1]==1 and p1[2]==1:
            flag = 1
        if p1[3]==1 and p1[4]==1 and p1[5]==1:
            flag = 1 
        if p1[6]==1 and p1[7]==1 and p1[8]==1:
            flag = 1

        #VERTICAL
        if p1[0]==1 and p1[3]==1 and p1[6]==1:
            flag = 1
        if p1[1]==1 and p1[4]==1 and p1[7]==1:
            flag = 1
        if p1[2]==1 and p1[5]==1 and p1[8]==1:
            flag = 1

        #SLANT
        if p1[0]==1 and p1[4]==1 and p1[8]==1:
            flag = 1
        if p1[2]==1 and p1[4]==1 and p1[6]==1:
            flag = 1
        
    else:
        print("Player 2 : Enter the position ")
        n = int(input())
        while l[n-1] == 'X' or l[n-1] == 'O':
            print("This position is already in used")
            n = int(input())
        p2[n-1] = 1
        l[n-1] = 'O'
        
        #Horizontal
        if p2[0]==1 and p2[1]==1 and p2[2]==1:
            flag = 2
        if p2[3]==1 and p2[4]==1 and p2[5]==1:
            flag = 2 
        if p2[6]==1 and p2[7]==1 and p2[8]==1:
            flag = 2

        #VERTICAL
        if p2[0]==1 and p2[3]==1 and p2[6]==1:
            flag = 2
        if p2[1]==1 and p2[4]==1 and p2[7]==1:
            flag = 2
        if p2[2]==1 and p2[5]==1 and p2[8]==1:
            flag = 2

        #SLANT
        if p2[0]==1 and p2[4]==1 and p2[8]==1:
            flag = 2
        if p2[2]==1 and p2[4]==1 and p2[6]==1:
            flag = 2
        
    if flag != 0:
        print("Player ",flag, "is Winner")
        break;

if flag == 0:
    print("Game has tied!!! No Winner ")
