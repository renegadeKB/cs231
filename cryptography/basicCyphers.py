


def findDiffieKey(g,p,A,B):
    xList = []
    yList = []
    for i in range(0,p):
        if(pow(g,i)%p == A):
            xList.append(i)
        elif(pow(g,i)%p == B):
            yList.append(i)
    
    for x in xList:
        for y in yList:
            if pow(B,x)%p == pow(A,y)%p:
                print("x = ",x,"y = ",y)



findDiffieKey(17,61,46,5)

findDiffieKey(17,41,46,5)





def isPrime(x):
    if(x-int(x) == 0):
        x =int(x)
        for y in range(2, x):
            if x % y == 0:
                return False
        return True
    return False

def findPrimes(e,n):
    p = 0
    q = 0
    i = e+1
    while i < n:
        if(isPrime(i)):
            j = n/i
            if(isPrime(j)):
                print(i,j)
                return(i,j)
                #primes.append(i,j)
                break
        i+=1

    if(i == n):
        print("whoops")
    

p,q = findPrimes(31,4461)
message = [2677, 4254, 1152, 4645, 4227, 1583, 2252, 426, 3492, 4227, 3889, 1789, 4254, 1704, 1301, 4227, 1420, 1789, 1821, 1466, 4227, 2252, 3303, 1420, 2234, 4227, 4227, 1789, 1420, 1420, 4402, 1466, 4070, 3278, 3278, 414, 414, 414, 2234, 1466, 1704, 1789, 2955, 4254, 1821, 4254, 4645, 2234, 1704, 2252, 3282, 3278, 426, 2991, 2252, 1604, 3278, 1152, 4645, 1704, 1789, 1821, 4484, 4254, 1466, 3278, 1512, 3602, 1221, 1872, 3278, 1221, 1512, 3278, 4254, 1435, 3282, 1152, 1821, 2991, 1945, 1420, 4645, 1152, 1704, 1301, 1821, 2955, 1604, 1945, 1221, 2234, 1789, 1420, 3282, 2991, 4227, 4410, 1821, 1301, 4254, 1466, 3454, 4227, 4410, 2252, 3303, 4645, 4227, 3815, 4645, 1821, 4254, 2955, 2566, 3492, 4227, 3563, 2991, 1821, 1704, 4254]

def findD(e,n,p,q):
    d = 2
    while((((5**d) % 4661)**e) %4661 != 5):
        d+=1
    #while((e*d)%((p-1)*(q-1)) != 1):
       # d+=1
    decoded = ""
    for word in message:
        decoded+= chr((word**d)%4661)
    
    return(decoded)
print(findD(31,4461,p,q))

