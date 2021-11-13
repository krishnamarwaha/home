
def check_number(y,x):
    s = str(y)
    a = int(s[1:4])
    b = int(s[0:1]+s[2:4])
    c = int(s[0:2]+s[3:4])
    d = int(s[0:3])
    if(y-a == x):
        print (y,a)
        return True
    if (y - b == x):
        print (y,b)
        return True
    if (y - c == x):
        print (y,c)
        return True
    if (y - d == x):
        print (y,d)
        return True


    return False

def find_number(x):
    for y in range(1000,10000):
        check_number(y,x)


print(" pick a 4 digit number?")
k = int(input())
find_number(k)
