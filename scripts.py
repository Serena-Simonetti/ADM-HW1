# Say "Hello, World!" With Python
string='Hello, World!'
print(string)

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i*i)
        i=i+1

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    else:
        if n<=5:
            print("Not Weird")
        elif n>5 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

# Write a function
def is_leap(year):
    leap = False
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                 return leap
        else:
            return True
    else:
        return leap
            
    
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    string=""
    i=1
    while i<=n:
        string=string+str(i)
        i=i+1
    print(string)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    massimo=max(arr)
    massimo_2=massimo
    while massimo==massimo_2:
        arr.remove(massimo)
        massimo=max(arr)
    print(massimo)
    

# Nested Lists
if __name__ == '__main__':
    lista=[]
    lista_2=[]
    final_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
        lista_2.append(score)
    minimo=min(lista_2)
    lista_2=[i for i in lista_2 if i != minimo]        
    minimo_2=min(lista_2)
    for i in lista:
        nome,punteggio=i
        if punteggio==minimo_2:
            final_list.append(nome)
    final_list.sort()
    for i in final_list:
        print(i)
        
    

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a,b,c=student_marks[query_name]
    media=(a+b+c)/3
    print(f"{media:.2f}")

# Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    array=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n :
                    array.append([i,j,k])
    print(array)  
                
        
        
        
    

# Lists
if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(N):
        comandi=input().split()
        parola=comandi[0]
        
        if parola.startswith("i"):
            index=int(comandi[1])
            value=int(comandi[2])
            my_list.insert(index,value)
        elif parola.startswith("pr"):
            print(my_list)
        elif parola.startswith("rem"):
            my_list.remove(int(comandi[1]))
        elif parola.startswith("a"):
            my_list.append(int(comandi[1]))
        elif parola.startswith("s"):
            my_list.sort()
        elif parola.startswith("po"):
            my_list.pop()
        elif parola.startswith("rev"):
            my_list.reverse()
            
            
            
    
            
    

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla=tuple(integer_list)
    print(hash(tupla))

# sWAP cASE
def swap_case(s):
    stringa=""
    for i in s:
        if i.isupper():
            stringa+=i.lower()
        else:
            stringa+=i.upper()
    return stringa

# String Split and Join

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    print("Hello " + str(first) + " " + str(last) + "! You just delved into python.")

# Find a string
def count_substring(string, sub_string):
    conto=0
    i=0
    while True:
        index=string.find(sub_string,i)
        if index==-1:
            break
        conto+=1
        i=index+1
    return conto

# String Validators
if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if alnum and alpha and digit and lower and upper:
            break
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap

def wrap(string, max_width):
    paragraph=string
    righe=textwrap.fill(paragraph, width=max_width)
    return righe

# Mutations
def mutate_string(string, position, character):
    string=string[:position] +character +string[position+1:]
    return string

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
def function(N, M):
    for i in range(1, N, 2):
        disegno = ".|." * i
        print(disegno.center(M, "-"))
        
    print("WELCOME".center(M, "-"))
    
    for i in range(N-2, 0, -2):
        disegno = ".|." * i
        print(disegno.center(M, "-"))
N, M = map(int, input().split())
function(N, M)

# String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    
    for i in range(1, number+1):
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),  
              hex(i)[2:].upper().rjust(width),  
              bin(i)[2:].rjust(width))  
        

# Alphabet Rangoli
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for i in range(size):
        
        left = alphabet[size-1:size-i-1:-1]  
        center = alphabet[size-i-1]  
        right = alphabet[size-i:size]  
        
        row = "-".join(left + center + right)
        
        
        lines.append(row.center(4*size - 3, "-"))
    pattern = '\n'.join(lines[:size-1]+lines[::-1])
    print(pattern)



# Capitalize!

def solve(s):
    lista=s.split(" ")
    stringa=""
    for i in range(len(lista)):
        if len(lista[i]) > 0:
            nome = lista[i][0].upper() + lista[i][1:]
        else:
            nome = lista[i]
    
        stringa += nome + " "
    
    return stringa

# Merge the Tools!
def merge_the_tools(string, k):
    n=len(string)
    i=0
    for i in range(0,n,k):
        parte = string[i:i+k]
        stringa_vuota=""
        for l in parte:
            if l not in stringa_vuota:
                stringa_vuota+=l            
        print(stringa_vuota)
        
        i += k
    


# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        numero_20 = []
        for i in l:
            numero = i[-10:]
            numero_2 = "+91 " + numero[:5] + " " + numero[5:]
            numero_20.append(numero_2)  
        return f(numero_20)
    
    return fun

# The Minion Game
def minion_game(string):
    vowels = "AEIOU"
    points_stuart = 0
    points_kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            points_kevin += len(string) - i
        else:
            points_stuart += len(string) - i
    
    if points_kevin > points_stuart:
        print("Kevin",points_kevin)
    elif points_stuart > points_kevin:
        print("Stuart", points_stuart)
    else:
        print("Draw")
        
            
            

# itertools.product()
from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
result=product(A,B)
for i in result:
    print(f"({i[0]}, {i[1]})", end=' ')

# itertools.permutations()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
hp=input().split()
S=hp[0]
k=int(hp[1])
result=list(permutations(S,k))
result.sort()
for i in result:
    print("".join(i))

# itertools.combinations()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
dato=input().split()
S=dato[0]
S = ''.join(sorted(S))
k=int(dato[1])
for i in range(1,k+1):
    result=list(combinations(S,i))
    for el in result:
        j="".join(el)
        
        print(j)    
        
    
    

# Introduction to Sets
def average(array):
    insieme=set(array)
    somma=sum(insieme)
    N=len(insieme)
    media=somma/N
    return media
    

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = list(map(int, input().split()))
N = int(input())
b = list(map(int, input().split()))
a=set(a)
b=set(b)
intersezione=a.intersection(b)
for i in intersezione:
    a.discard(i)
    b.discard(i)
c=a.union(b)
lista=[]
for i in c:
    lista.append(i)
lista.sort()
for i in lista:
    print(i)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m= map(int, input().split()) # n for the array, m for the sets
array=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
happiness=0
for i in array:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)

# Polar Coordinates
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
zeta=complex(input())
print(abs(zeta))
print(cmath.phase(zeta))

# Find Angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=float(input())
BC=float(input())
angolo=math.atan2(AB,BC)
angolo=round(math.degrees(angolo))
print(f"{angolo}{chr(176)}")

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
list_shoe_size = list(map(int, input().split()))
N = int(input())
desired_and_price = []
for _ in range(N):
    taglia, prezzo = map(int, input().split())
    desired_and_price.append((taglia, prezzo))
cont = Counter(list_shoe_size)
prezzo_tot = 0
for i, j in desired_and_price:
    if cont[i] > 0:
        prezzo_tot += j
        cont[i] -= 1
print(prezzo_tot)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
group_A = defaultdict(list)
for i in range(1, n + 1):
    parola = input().strip()
    group_A[parola].append(i)
for _ in range(m):
    parola = input().strip()
    if parola in group_A:
        print(" ".join(map(str, group_A[parola])))
    else:
        print(-1)


# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
columns = input().strip().split()
Student = namedtuple('Student', columns)
total_marks = 0
for _ in range(N):
    values = input().strip().split()
    student = Student(values[0], values[1], values[2], values[3])
    total_marks += int(student.MARKS)

average_marks = total_marks / N
print(f"{average_marks:.2f}")
        
        
        
    

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N=int(input())
D=OrderedDict()
for _ in range(N):
    info = input().rsplit(" ", 1)
    item_name = info[0]
    net_price = int(info[1])
    if item_name in D:
        D[item_name] += net_price
    else:
        D[item_name] = net_price
for i,j in D.items():
    print(i,j)

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
parole=[]
for _ in range(n):
    parole.append(input().strip()) 
# Crea un Counter per contare la frequenza delle parole
counter_parole = Counter(parole)
# Stampa il numero di parole distinte
print(len(counter_parole))
# Stampa la frequenza di ciascuna parola nell'ordine in cui appare nel Counter
for parola in counter_parole:
    print(counter_parole[parola], end=" ")

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    info = input().split()
    method = info[0]
    if len(info)>1:
        value = info[1]
    if method == "append":
        d.append(value)
    elif method == "appendleft":
        d.appendleft(value)
    elif method == "pop":
        d.pop()
    elif method == "popleft":
        d.popleft()
print(" ".join(d))

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
data=list(map(int, input().split()))
mese=data[0]
giorno=data[1]
anno=data[2]
nome_giorni_ing=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
nome_giorno=calendar.weekday(anno, mese, giorno)
print(nome_giorni_ing[nome_giorno])

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    a, b =input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e) 
            
    except ValueError as b:
        print("Error Code:", b)

# Incorrect Regex
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T=int(input())
for _ in range(T):
    S = input().strip()
    if '++' in S or '*+' in S or '.*+' in S or '.+' in S:
        print(False)
    else:
        print(True)
    

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
s=set()
c=0
for _ in range(N):
    country=str(input())
    if country not in s:
        s.add(country)
        c+=1
print(c)

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(N):
    data=list(input().split())
    command=data[0]
    if len(data)>1:
        numero=int(data[1])
    if command=="pop":
        if s:
            s.pop()
    elif command=="remove":
        s.remove(numero)
    elif command=="discard":
        s.discard(numero)
somma=0
for i in s:
    somma+=i
print(somma)

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int, input().split()))
b=int(input())
french=set(map(int, input().split()))
out=len(english.union(french))
print(out)

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int, input().split()))
b=int(input())
french=set(map(int, input().split()))
out=len(english.intersection(french))
print(out)

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int ,input().split()))
m=int(input())
french=set(map(int ,input().split()))
out=len(english.difference(french))
print(out)

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int, input().split()))
m=int(input())
french=set(map(int, input().split()))
out=len(english.symmetric_difference(french))
print(out)

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int, input().split()))
N=int(input())
for _ in range(N):
    data=list(input().split())
    command=data[0]
    number=int(data[1])
    other=set(map(int, input().split()))
    if command.startswith("int"):
        A.intersection_update(other)
    elif command.startswith("up"):
        A.update(other)
    elif command.startswith("sy"):
        A.symmetric_difference_update(other)
    elif command.startswith("di"):
        A.difference_update(other)
somma=0
for i in A:
    somma+=i
print(somma)

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
K=int(input())
lista=list(map(int, input().split()))
contatore=Counter(lista)
for i,j in contatore.items():
    if j==1:
        print(i)

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    n=int(input())
    A=set(map(int, input().split()))
    m=int(input())
    B=set(map(int, input().split()))
    C=B.intersection(A)
    if C==A:
        print(True)
    else:
        print(False)

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int, input().split()))
n=int(input())
c=[]
for _ in range(n):
    B=set(map(int, input().split()))
    if A>B:
        c.append(True)
    else:
        c.append(False)
cont=0
for i in c:
    if i:
        cont+=1
if cont==len(c):
    print(True)
else:
    print(False)
        

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
from collections import Counter
counter = Counter(s)
sorted_characters = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
for char, count in sorted_characters[:3]:
    print(f"{char} {count}")

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    cube_deque = deque(cubes)
    last_cube = float('inf')
    is_possible = True
    
    while cube_deque:
        if cube_deque[0] >= cube_deque[-1]:
            current_cube = cube_deque.popleft()
        else:
            current_cube = cube_deque.pop()
        
        if current_cube > last_cube:
            is_possible = False
            break
        
        last_cube = current_cube
    
    if is_possible:
        print("Yes")
    else:
        print("No")

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    dt1 = datetime.strptime(t1, format_string)
    dt2 = datetime.strptime(t2, format_string)
    
    delta_seconds = abs(int((dt1 - dt2).total_seconds()))
    return str(delta_seconds)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
voti = []
for _ in range(X):
    voti.append(list(map(float, input().split())))
student_scores = zip(*voti)
for i in student_scores:
    media = sum(i) / X
    print(f"{media:.1f}")


# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())
    arr.sort(key=lambda x: x[k])
    for i in arr:
        print(" ".join(map(str, i)))

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
lower=""
upper=""
digit=""
for i in S:
    if i.isupper():
        upper+=i
    elif i.islower():
        lower+=i
    elif i.isdigit():
        digit+=i
upper="".join(sorted(upper))
lower="".join(sorted(lower))
digit="".join(sorted(digit, key=lambda x: (int(x) % 2 == 0, x)))
print(lower+upper+digit)

# Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    sequence=[]
    a, b=0,1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r"^[+-]?(\d*\.\d+|\d+\.\d*)$"
T = int(input())
for _ in range(T):
    S = input().strip()
    if re.match(pattern, S):
        try:
            float(S)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)

    

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S=input()
pattern = r"([a-zA-Z0-9])\1"
trovato = re.search(pattern, S)
if trovato:
    print(trovato.group(1))
else:
    print("-1")

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S=input().strip()
pattern=r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"
match=re.findall(pattern,S)
if match:
    for i in match:
        print(i)
else:
    print("-1")
    

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
k = input()
matches = list(re.finditer(f'(?={k})', S))
if matches:
    for i in matches:
        print((i.start(), i.start() + len(k) - 1))
else:
    print((-1, -1))

# Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for _ in range(N):
    stringa=input()
    pattern = r"^[789]\d{9}$"
    match=re.findall(pattern, stringa)
    if match:
        print("YES")
    else:
        print("NO")

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
n=int(input())
pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
for _ in range(n):
    nome, emai=email.utils.parseaddr(input().strip())
    match=re.match(pattern, emai)
    if match:
        print(nome+" <"+emai+">")

# Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
css_code = []
for _ in range(n):
    css_code.append(input())
css_code = "\n".join(css_code)
inside_braces = re.findall(r'\{([^}]*)\}', css_code, re.DOTALL)
css_properties = " ".join(inside_braces)
hex_pattern = r'#[0-9a-fA-F]{3}(?![0-9a-fA-F])|#[0-9a-fA-F]{6}(?![0-9a-fA-F])'
matches = re.findall(hex_pattern, css_properties)
for i in matches:
    print(i)

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    massimo=0
    c=0
    for i in candles:
        if i>massimo:
            massimo=i
    for i in candles:
        if i==massimo:
            c+=1
    return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    if ((x1>x2) & (v1>v2)) | ((x1<x2) & (v1<v2)):
        return "NO"
    elif v1 != v2:
        if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
            return "YES"
        else:
            return "NO"
    else:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    shared=5
    liked=0
    cumulative=0
    for _ in range(n):
        liked=shared//2
        shared=liked*3
        cumulative+=liked
    return cumulative
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    somma = sum(int(digit) for digit in n)
    total_sum = somma * k
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))
    return total_sum
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    value=arr[-1]
    i=n-2
    while i>=0 and arr[i]> value:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1
  
    arr[i+1]=value
    print(" ".join(map(str, arr)))
        
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    for i in range(1, n):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j] >value:
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=value
        
        print(" ".join(map(str, arr)))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        people_with_index = []
        for index, person in enumerate(people):
            people_with_index.append((index,) + tuple(person))
        people_with_index.sort(key=lambda person: (int(person[3]), person[0]))
        lista=[]
        for i in people_with_index:
            lista.append(f(i[1:]))
        return lista
    return inner

# Arrays

def arrays(arr):
    b=numpy.array(arr, float)
    b_reversed=b[::-1]
      
    return b_reversed


# Shape and Reshape
import numpy
lista=[]
lista.append(input().split())
a=numpy.array(lista,int)
print(numpy.reshape(a, (3,3)))


# Transpose and Flatten
import numpy
data=input().split()
N=int(data[0])
M=int(data[1])
lista_rows=[]
for _ in range(N):
    lista_rows.append(list(map(int, input().split())))
a=numpy.array(lista_rows)
lista=numpy.transpose(a)
print(lista)
print(a.flatten())

# Concatenate
import numpy
data=input().split()
N=int(data[0])
M=int(data[1])
P=int(data[2])
lista_1=[]
lista_2=[]
for _ in range(N):
    lista_1.append(list(map(int, input().split())))
for _ in range(M):
    lista_2.append(list(map(int, input().split())))
array_1=numpy.array(lista_1)
array_2=numpy.array(lista_2)
print(numpy.concatenate((array_1, array_2), axis=0))

# Zeros and Ones
import numpy
dim=tuple(map(int, input().split()))
print(numpy.zeros(dim, dtype=int))
print(numpy.ones(dim, dtype=int))

# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
data=input().split()
N=int(data[0])
M=int(data[1])
print(numpy.eye(N, M, k=0))


# Array Mathematics
import numpy as np
data=input().split()
N=int(data[0])
M=int(data[1])
lista_A = [list(map(int, input().split())) for _ in range(N)]
lista_B = [list(map(int, input().split())) for _ in range(N)]
a = np.array(lista_A)
b = np.array(lista_B)
add = np.add(a, b)
print(add)
sub = np.subtract(a, b)
print(sub)
mul = np.multiply(a, b)
print(mul)
div = np.floor_divide(a, b)
print(div)
mod = np.mod(a, b)
print(mod)
poww = np.power(a, b)
print(poww)

# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')
A=list(map(float, input().split()))
A=numpy.array(A)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))


# Sum and Prod
import numpy
data=input().split()
N=int(data[0])
M=int(data[1])
A=[list(map(int, input().split())) for _ in range(N)]
summ=numpy.sum(A, axis=0)
print(numpy.prod(summ))

# Min and Max
import numpy
data=input().split()
N=int(data[0])
M=int(data[1])
A=[list(map(int, input().split())) for _ in range(N)]
minimo=numpy.min(A, axis=1)
print(numpy.max(minimo))

# Mean, Var, and Std
import numpy
data=input().split()
N=int(data[0])
M=int(data[1])
lista_A=[]
for _ in range(N):
    lista=list(map(int, input().split()))
    lista_A.append(lista)
A=numpy.array(lista_A)
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
std=numpy.std(A, axis=None)
if std==int(std):
    print(f"{std:.1f}")
else:
    print(f"{std:.11f}")

# Dot and Cross
import numpy
N=int(input())
lista_A=[]
lista_B=[]
for _ in range(N):
    lista_1=list(map(int, input().split()))
    lista_A.append(lista_1)
for _ in range(N):
    lista_1=list(map(int, input().split()))    
    lista_B.append(lista_1)
print(numpy.dot(lista_A, lista_B))

# Inner and Outer
import numpy
A=list(map(int, input().split()))
B=list(map(int, input().split()))
print(numpy.inner(A,B))
print(numpy.outer(A,B))


# Polynomials
import numpy
P=list(map(float, input().split()))
x=float(input())
print(numpy.polyval(P, x))

# Linear Algebra
import numpy
N=int(input())
matrix_A=[]
for _ in range(N):
    A=list(map(float, input().split()))
    matrix_A.append(A)
matrix_A=numpy.array(matrix_A)
print(round(numpy.linalg.det(matrix_A), 2))

# XML 1 - Find the Score

def get_attr_number(node):
    score=len(node.attrib)
    
    for i in node:
        score+=get_attr_number(i)
    return score
            

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")
    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")
N=int(input())
html="\n".join(input() for _ in range(N))
parser=MyHTMLParser()
parser.feed(html)

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
  
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
    def handle_comment(self, data):
        pass

n=int(input())
html="\n".join(input() for _ in range(n))
parser = MyHTMLParser()
parser.feed(html)

# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T=int(input())
for _ in range(T):
    uid = input().strip()
    if len(uid) != 10:
        print("Invalid")
        continue
    if not uid.isalnum():
        print("Invalid")
        continue
    if len(set(uid)) != len(uid):
        print("Invalid")
        continue
    uppercase_count=len(re.findall(r'[A-Z]', uid))
    digit_count=len(re.findall(r'\d', uid))
    if uppercase_count >= 2 and digit_count >= 3:
        print("Valid")
    else:
        print("Invalid")

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for _ in range(N):
    card_number = input().strip()
    pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    
    if not re.match(pattern, card_number):
        print("Invalid")
        continue
    
    clean = card_number.replace("-", "")
    if re.search(r"(\d)\1{3,}", clean):
        print("Invalid")
        continue
    
    print("Valid")

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string = ""
for col in range(m):
    for row in range(n):
        string += matrix[row][col]
string = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', string)
print(string)

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
text = "\n".join(lines)
text = re.sub(r'(?<= )&&(?= )', 'and', text)
text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
print(text)

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    for i in elem:
        depth(i, level)
    if level > maxdepth:
        maxdepth = level

