def gcd(a,b):
    if a == 0 :
        return b
    elif b == 0:
        return a
    else:
        return gcd(max(a,b) % min(a,b), min(a,b))

def lcm(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return int((a*b)//gcd(a,b))

def factors(n):
    if n < 0:
        n *=(-1)
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,2]
    elif n==3:
        return [1,3]
    else:
        factors = []
        for i in range (1,int(n**.5)):
            if(n % i == 0):
                factors.append(i)
        k = len(factors)
        for i in range (0,k):
            factors.append(int(n/factors[i]))
        return factors

def isPrime(n):
    if n > 15485863:
        return -1
    elif n <2:
        return -2
    else:
        file = open("primes.txt", "r")
        primes = file.read().split()
        file.close()
        s = str(n)
        if s in primes:
            return 1
        else:
            return 0

def numPrimes(m, n):
    if m <0:
        m = 2
    if n <2:
        return 0
    elif m > n:
        return 0
    elif m == n:
        file = open("primes.txt", "r")
        primes = file.read().split()
        file.close()
        if m in primes:
            return 1
        else:
            return 0
    else:
        counter = 0
        file = open("primes.txt", "r")
        primes = file.read().split()
        file.close()
        for i in range(m, n+1):
            if i in primes:
                counter += 1
        return counter

def nthPrime(n):
    if n < 1:
        return -1
    elif n > 1000000:
        return 1
    else:
        file = open("primes.txt", "r")
        primes = file.read().split()
        file.close()
        return primes[n-1]

def maxPrime(a,b):
    if a < 0:
        a = 2
    if b < 2:
        return -2
    f = open("primes.txt", "r")
    file = f.read().split()
    file = list(map(int, file))
    m = -1
    f.close()
    while(b >= a):
        if b in file:
            m = b
            break
        else:
            b -= 1
    return m

def minPrime(a,b):
    if a < 0:
        a = 2
    if b < 2:
        return -2
    f = open("primes.txt", "r")
    file = f.read().split()
    file = list(map(int, file))
    m = -1
    f.close()
    for i in range(a, b+1):
        if i in file:
            m = i
            break
    return m

def primes(a,b):
    if a < 0:
        a = 2
    if b < 2:
        return -2
    f = open("primes.txt", "r")
    file = f.read().split()
    file = list(map(int, file))
    f.close()
    primes = []
    for i in range(a, b+1):
        if i in file:
            primes.append(i)
    primes = tuple(primes)
    return primes
def isDivisible(a,b):
    if b == 0:
        return False
    elif a % b == 0:
        return True
    else:
        return False

def divide(a,b):
    q = a//b
    r = a - b*q
    nums = []
    nums.append(q)
    nums.append(r)
    return nums

def phi(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        counter = 0
    for i in range(1, n):
        if gcd(i,n) == 1:
            counter += 1
    return counter

def tau(n):
    if n < 0:
        n *=(-1)
    if n == 0:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n==3:
        return 4
    else:
        sum= 0
        for i in range (1,n+1):
            if(n % i == 0):
                sum += i
        return sum


def genRedSys(n):
    if n != 0:
        if n < 0:
            n *= (-1)
        if n == 2 or n == 1:
            return [1]
        else:
            residues = []
            for i in range (1,n):
                if(gcd(i,n) == 1):
                    residues.append(i)
        return residues
    else:
        return []

def genCompleteSys(n):
    if n == 0:
        return []
    elif n == 1 or n == -1:
        return [0]
    else:
        if n < 0:
            n *= (-1)
        residues = []
        for i in range (0, n):
            residues.append(i)
        return residues

def multipInverse(a,n):
    if n < 0:
        n *= (-1)
    if(n == 0):
        return 0
    elif gcd(a,n) != 1:
        return 0
    elif n == 1 or n == -1:
        return 1
    else:
        d = 1
        for d in range(1,n):
            if (a*d) % n == 1:
                return d

def solveLinearCongruence(a,b,c,m):
    if m == 0:
        return -1
    elif ((c-b) % gcd(m,a)) == 0:
        d = gcd(a,m)
        a = int(a/d)
        m = int(m/d)
        e = int((c-b)/d)
        inverse = multipInverse(a,m)
        inverse = inverse * e
        return inverse % m
    else:
        return -2



import tkinter as T

help = "Available commands:\n    1. gcd a b\n    2. lcm a b\n    3. factors n\n    4. isPrime n (upto n=15485863)\n    5. nthPrime n (upto n = 1000000)\n    6. divide a b\n    7. isDivisible a b n\n    8. genRedSys n\n    9. multipInverse a m\n    10. solveLinearCongruence a b c d\n    11. maxPrime a b\n    12. minPrime a b\n    13. save_overwrite\n    14. save_append\n    15. primes a b (ultra slow)\n 16. phi n\n 17. tau n"
about = "numExplorer- an number theoretic tool that does some divisibility and congruence operations. It has a record of the first 1 million primes, which allows it to check primality and list primes in a certain range. It also solves linear congruence systems etc. The list of the primes was received from:' ' and the logo was designed using a free tool from logomakr.com. This code comes with absolutely no warranty and no copywright."

window = T.Tk()
window.title("NumExplorer")

COLUMN = T.Label(window)
COLUMN.grid(row=0, column=0)

INPUT = T.Entry(window,fg="red", font="40")
INPUT.grid(row=0,column=1,padx=5,pady=5)
INPUT.focus_set()

RESULTS= T.Text(window,fg="green",font="40")
RESULTS.grid(row=0,column=2,padx=5,pady=5)

def EXEC_CLEAR():
    global OUTPUT
    RESULTS.delete("0.0", T.END)
def EXEC_SHOW_HELP():
    RESULTS.insert("0.0", help)
    RESULTS.see(T.END)
def EXEC_SHOW_ABOUT():
    RESULTS.insert("0.0", about)
    RESULTS.see(T.END)
def EXEC_SAVE():
    global RESULTS
    from tkinter.filedialog import askopenfilename
    file = askopenfilename()
    F = open(file, "w")
    s = RESULTS.get("0.0", T.END)
    F.write(s)
    F.close()
def EXEC_QUIT():
    window.quit()
def EXEC(event):
    if event.char=="\r":
        global RESULTS
        global INPUT
        s = INPUT.get()
        INPUT.delete(0,T.END)
        t = s.split()
        command = t[0]
        del t[0:1]
        if command == "gcd":
            t = list(map(int, t))
            d = gcd(t[0], t[1])
            RESULTS.insert("0.0", d)
            RESULTS.see(T.END)
        elif command == "lcm":
            t = list(map(int, t[0]))
            d = lcm(t[0], t[1])
            RESULTS.insert("0.0", d)
            RESULTS.see(T.END)
        elif command == "divide":
            t = list(map(int, t))
            t = divide(t[0], t[1])
            RESULTS.insert("0.0", t)
            RESULTS.see(T.END)
        elif command == "factors":
            n = int(t[0])
            facts = factors(n)
            RESULTS.insert("0.0", facts)
            RESULTS.see(T.END)
        elif command == "tau":
            n = int(t[0])
            sum = tau(n)
            if sum == -1:
                RESULTS.insert("0.0", "inf")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", sum)
                RESULTS.see(T.END)
        elif command == "isPrime":
            n = int(t[0])
            if isPrime(n) == 0:
                RESULTS.insert("0.0", "NO")
                RESULTS.see(T.END)
            elif isPrime(n) == 1:
                RESULTS.insert("0.0", "YES")
                RESULTS.see(T.END)
            elif isPrime(n) == -1:
                RESULTS.insert("0.0", "Please input a number less than or equal to 15485863")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", "Please input a number greater than or equal to 2")
                RESULTS.see(T.END)
        elif command == "nthPrime":
            n = nthPrime(int(t[0]))
            if n == -1:
                RESULTS.insert("0.0", "This command requires a positive integer")
                RESULTS.see(T.END)
            elif n == 1:
                RESULTS.insert("0.0", "Sorry, only primes upto the 1000000th prime can be computed")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", n)
                RESULTS.see(T.END)
        elif command == "genRedSys":
            n = int(t[0])
            RESULTS.insert("0.0", genRedSys(n))
            RESULTS.see(T.END)
        elif command == "multipInverse":
            t = list(map(int, t))
            d = multipInverse(t[0], t[1])
            RESULTS.insert("0.0", d)
            RESULTS.see(T.END)
        elif command == "solveLinearCongruence":
            t = list(map(int, t))
            t = solveLinearCongruence(t[0], t[1], t[2], t[2])
            if t == -1 or t == -2:
                RESULTS.insert("0.0", "NO SOlUTIONS")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", t)
                RESULTS.see(T.END)
        elif command == "maxPrime":
            t= list(map(int, t))
            temp = maxPrime(t[0], t[1])
            if temp == -2:
                RESULTS.insert("0.0", maxPrime("invalid range"))
                RESULTS.see(T.END)
            elif temp == -1:
                RESULTS.insert("0.0", "no primes in the range")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", temp)
                RESULTS.see(T.END)
        elif command == "primes":
            t = list(map(int, t))
            p = primes(t[0],t[1])
            for q in p:
                RESULTS.insert(T.END, "\n" + str(q))
                RESULTS.see(T.END)
        elif command == "minPrime":
            t= list(map(int, t))
            temp = minPrime(t[0], t[1])
            if temp == -2:
                RESULTS.insert("0.0", "invalid range")
                RESULTS.see(T.END)
            elif temp == -1:
                RESULTS.insert("0.0", "no primes in the range")
                RESULTS.see(T.END)
            else:
                RESULTS.insert("0.0", temp)
                RESULTS.see(T.END)
        elif command == "phi":
            t = list(map(int, t))
            temp = phi(t[0])
            RESULTS.insert("0.0", temp)
            RESULTS.see(T.END)
        elif command == "tau":
            t = list(map(int, t))
            temp = tau(t[0])
            RESULTS.insert("0.0", temp)
            RESULTS.see(T.END)
        elif command == "clear":
            EXEC_CLEAR()
        elif command == "save_append":
            from tkinter.filedialog import askopenfilename
            file = askopenfilename()
            F = open(file, "a")
            s = RESULTS.get("0.0", T.END)
            print(s)
            F.write(s)
            F.close()
        elif command == "save_overwrite":
            from tkinter.filedialog import askopenfilename
            file = askopenfilename()
            F = open(file, "w")
            s = RESULTS.get("0.0", T.END)
            print(s)
            F.write(s)
            F.close()
        elif command == "help":
            EXEC_SHOW_HELP()
        elif command == "about":
            EXEC_SHOW_ABOUT()
        elif command == "exit":
            EXEC_QUIT()
        else:
            RESULTS.insert("0.0", "Unknown command detected: Please type 'help', or click the COMMAND button to view the avaiable commands.")
            RESULTS.see(T.END)

INPUT.bind("<Key>", EXEC)

BUTTON_CLEAR = T.Button(COLUMN, text="CLEAR",fg="red", font="70", command = EXEC_CLEAR)
BUTTON_CLEAR.pack(side=T.TOP,fill=T.X)

BUTTON_HELP = T.Button(COLUMN, text="COMMANDS",fg="red", font="70", command = EXEC_SHOW_HELP)
BUTTON_HELP.pack(side=T.TOP)

BUTTON_EXIT = T.Button(COLUMN, text="EXIT",fg="red", font="70", command = window.quit)
BUTTON_EXIT.pack(side=T.TOP)

BUTTON_SAVE_FILE = T.Button(COLUMN, text="Write to File",fg="red", font="70", command = EXEC_SAVE)
BUTTON_SAVE_FILE.pack(side=T.TOP)

window.iconbitmap(r'logo.ico')
window.mainloop()
