'''import keyword
print(keyword.kwlist)

a=True
print(a)

a=0
print(bool(a))
print(type(a))
print(bool(0.1))
print(int())
print(float())

a=3+5j
print(a)

a=3j+4
print(a)

a=6j
print(a)

a='Hello World!' 
print(a)

a=This is a multi-line string.
print(a)

a=[10,2.3,True,'Hello World!']
print(a[0])
a.append('Python')
print(a)
a.pop(0)
print(a)
print(a[-2])
a=(10,2.2,True,'hi')
print(a,type(a))

a={10,20,30}
print(a)

a={10,True,False}
print(a)

a={'a':10}
print(a['a'])

a={'a': 10,'b':20}
print(a.values())

a={'a':[10,20,30],'b':40}
print(a['a'][-1])'''

'''a="hello"
print(a[2:3+1:1])
print(a[-3:-2+1:1])'''

'''a="Good Morning"
print(a[7:10+1:1])
print(a[-5:-2+1:1])'''

'''a="hello"
print(a[3:0:-1])
print(a[-2:-5:-1])
print(a[::-1])'''

'''a="Good Morning"
print(a[1:5+1:2])
print(a[5::3])
print(a[-7::3])
print(a[-11:-6:2])
print(a[-2:-8:-3])
print(a[10:4-1:-3])'''

'''a=list(input("enter:"))
print(type(a))'''

'''a=list(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter:"))
print(type(a))'''

'''a=eval(input("enter:"))
    print(a,type(a))'''

'''if a%2==0:
    print("Even")
else:
    print("Odd")'''

'''a=eval(input("enter:"))
if len(a)==5:
    print('yes')
else:
     print('no')'''

'''ch=input("enter:")
if "A"<=ch<="Z":
    print("upper")
elif "a"<=ch<="z":
    print("lower")
else:
    print("not an alphabet")'''


'''un=input("enter username:")
if un=="admin":
    print("correct username")
    pw=input("enter password:")
    if pw=="ad@in":
        print("login successful")
    else:
        print("incorrect password")
else:
    print("incorrect username")'''

'''username='admin'
password='ad@in'
un=input("enter username:")
if un==username:
    print("correct username")
    pw=input("enter password:")
    if pw==password:
        print("login successful")
    else:
        print("incorrect password")
else:
        print("incorrect username")'''


'''i=1
while i<=100:
    print(i)
    i+=1'''

'''i=2;
while i<=50:
    print(i)
    i+=2'''

'''i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1'''

'''i=1
while i<=50:
    if i%2!=0:
        print(i)
    i+=1'''

'''n=int(input("enter a number:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print("reverse:",rev)'''

'''for i in range(1,100):
        print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i, "even")'''

'''l=[10,20,30]
for i in l:
    print(i)'''

'''s=input("enter:")
out=" "
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''


'''s=input("enter:")
rev=" "
for i in s:
    rev=i+rev   
print(rev)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=" ")
    print()'''

'''for i in range(1,10):
    for j in range(1,i+1):
        print('*',end=" ")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('$',end=" ")
        else:
            print('@',end=" ")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print('$',end=" ")
        elif i<j:
            print('',end=" ")
    print()'''



