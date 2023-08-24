a=int(input('enter a number'))
b=int(input('enter a number'))
c=int(input('enter a number'))
d=int(input('enter a number'))
e=int(input('enter a number'))
print(a)
print(b)
print(c)
print(d)
print(e)
min =a
if b< min :
    min=b
if c< min :
    min=c
if d< min :
    min=d
if e< min :
    min=e    
#print(min)    
min2=float('inf')

if a>min and a< min2 :
    min2=a
if b>min and b< min2 :
    min2=b
if c>min and c< min2 :
    min2=a
if d>min and d< min2 :
    min2=a
if e>min and e< min2 :
    min2=e

#print(min2)
min3=float('inf')
if a>min2 and a< min3 :
    min3=a
if b>min2 and b< min3 :
    min3=b
if c>min2 and c< min3 :
    min3=c
if d>min2 and  d< min3 :
    min3=d
if e>min2 and e< min3 :
    min3=e

print(min3)
