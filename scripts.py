#Say "Hello, World!" With Python
string='Hello, World!'
print(string)

#Python If-Else
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
#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#Loops
if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i*i)
        i=i+1
#Write a function
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
#Print Function
if __name__ == '__main__':
    n = int(input())
    string=""
    i=1
    while i<=n:
        string=string+str(i)
        i=i+1
    print(string)

###

#List Comprehensions
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

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    massimo=max(arr)
    massimo_2=massimo
    while massimo==massimo_2:
        arr.remove(massimo)
        massimo=max(arr)
    print(massimo)
#Nested Lists
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
#Finding the percentage
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
#Lists
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
#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla=tuple(integer_list)
    print(hash(tupla))

###
#sWAP cASE
def swap_case(s):
    stringa=""
    for i in s:
        if i.isupper():
            stringa+=i.lower()
        else:
            stringa+=i.upper()
    return stringa
#String Split and Join
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#What's Your Name?
def print_full_name(first, last):
    print("Hello " + str(first) + " " + str(last) + "! You just delved into python.")
#Mutations
def mutate_string(string, position, character):
    string=string[:position] +character +string[position+1:]
    return string
#Find a string
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
#String Validators
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
#Text Alignment
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
#Text Wrap
def wrap(string, max_width):
    paragraph=string
    righe=textwrap.fill(paragraph, width=max_width)
    return righe
#Designer Door Mat
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
#String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    
    for i in range(1, number+1):
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),  
              hex(i)[2:].upper().rjust(width),  
              bin(i)[2:].rjust(width))
#Alphabet Rangoli
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
#Capitalize!
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
#The Minion Game
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
#Merge the Tools!
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
####


#Introduction to Sets
def average(array):
    insieme=set(array)
    somma=sum(insieme)
    N=len(insieme)
    media=somma/N
    return media
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
#No Idea!
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
#Symmetric Difference
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
#Set .add()
N=int(input())
s=set()
c=0
for _ in range(N):
    country=str(input())
    if country not in s:
        s.add(country)
        c+=1
print(c)
