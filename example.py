# print("haii")

# a=100
# print(a)

# a = 'red'
# b = "hloo"
# print(a)
# print(b)

# """
# s1="haii"
# s2="welcome"
# print(s1+" "+s2)
#

# s1="nehala"
# s2="kn"
# print("full name is:"+s1+" "+s2)
#
#
# a = 10
# b = 15
# print("sum is:",a+b)
#
# x,y,z=10,20,30
# print(x,y,z)
# """
# a=b=c=100
# print(a,b,c)
#
# x=input("enter your name:")
# print(x)
#
# y=input("Enter a number:")
# print(y)

# x=int(input("Enter 1st no:"))
# y=int(input("Enter 2nd no:"))
# print("sum is",x+y)

# x=float(input("Enter 1st no:"))
# y=float(input("Enter 2nd no:"))
# print("sum is",x+y)

# x=int(input("enter 1st number: "))
# y=int(input("enter second number:"))
# print("diff is:",y-x)
# print("mult:",x*y)
# print("div:",x/y)
# print("mode:",x%y)
# print("exponent is",x**y)
# print("floor division:",x//y)
# a=int(input("Enter 1st no:"))
# b=int(input("Enter 2nd no:"))
# a,b=b,a#mutiple value to multiple variables
# print("a=",a,",","b=",b)
#
# print("{}{},{}{}".format("Value of a is:",a,"Value of b is:",b))
#
# a="hai"
# b="how are you"
# print("{}{}".format(a,b))

# x=300
# print(x<500 and x>200)
#
# x=500
# print(x<1000 and x>500)

# x=250
# print(x<1000 or x>500)
# print(x<100 or x>1000)

# x=500
# print(not(x<1000 and x>100))
# print(not(x<100 or x>1000))

# x,y,z=10,30,10
# print(x==y)
# print(x==z)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x<=y)

# x=20
# x+=5
# print(x)
# x-=10
# print(x)
# x*=2
# print(x)
# x/=2
# print(x)

# d=10
# print(type(d))
#
# s='haii'
# print(type(s))
#
# f=20.5
# print(type(f))
#
# c=15j
# print(type(c))
#
# a=False
# print(type(a))
#
# l=[1,2,3,4,5]#list
# print(type(l))
#
# sl=["red",'blue',"yellow"]
# print(type(sl))
#
# st={1,2,3,5}
# print(type(st))
#
# t=('python','c','java','c#')
# print(type(t))
#
# dc={1:'Anu',2:'Anju',3:'Vimal'}
# print(type(dc))

# print('a:{a},b:{b},c:{c}'.format(a=10,b='twenty',c=20.5))
#
# print('a:{0},b:{1},c:{2}'.format(1,"two",3.4))
#
# print('a:{1},b:{2},c:{0}'.format('hai','hloo','welcome'))
# print('{},{}{}'.format(3,4,5))

# name="anu"
# print("hai %s"%name)
#
# name="anju"
# age=20
# print('%s is %d years old'%(name,age))
# print('{0} is {1} years old'.format(name,age))
# print(f"{name} is {age}years old")
#
# mylist=[1,2,3]
# print("list is: %s"%mylist)
#
# a="red"
# print("%s and %s are colours"%('green',a))
#
# x=12
# str ="Variable as integer= %d \n Variable as float=%f"%(x,x)
# print(str)
#
# c=5+2j
# print('real ={0} and imaginary={1}'.format(c.real,c.imag))
#
# n=23
# print("number is {0:f}".format(n))
#
# n=23.237
# print("number is {0:f}".format(n))
# print("number is {0:.2f}".format(n))
# print("number is {0:.1f}".format(n))


# a=int(21)
# b=int(21.2)
# c=int('123')
#  # d=int('12.3')
# print('{},{},{}'.format(a,b,c))
#
# x=float(23)
# y=float(2.4)
# z=float('12')
# u=float('123.5')
# print('{},{},{},{}'.format(x,y,z,u))
#
# s=str('hlo')
# t=str(22)
# r=str(23.2)
# print('{} {} {}'.format(s,t,r))
#
# x=int(input("Enter the 1st no:"))
# y=int(input("Enter the 2nd no:"))
# if x==y:
#     print("no is equal")
# else:
#     print("no is not equal")
#
# x=int(input("Enter the 1st no:"))
# y=int(input("Enter the 2nd no:"))
# if x>y:
#     print(x,"is largest")
# else:
#     print(y,"is largest")

# x=int(input("Enter a no:"))
# if x%2==0:
#     print("Even")
# else:
#     print("odd")

# n=int(input("Enter a no:"))
# if n>0:
#     print("positive num")
# elif n<0:
#     print("negative num")
# else:
#     print("Zero")


# print("Natural numbers are")
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# n=int(input("Enter the limit:"))
# print("odd numbers are:")
# i=1
# while i<=n:
#     if i%2==1:
#         print(i)
#     i=i+1
# n=int(input("Enter the no:"))
# sum=1
# while n>0:
#     rm=n%10
#     sum=sum*rm
#     n=n//10
# print(sum)
# n=int(input("Enter the no:"))
# s=0
# t=n
# while n>0:
#     r=n%10
#     s=s+r**3
#     n=n//10
# if t==s:
#     print("Armstrong")
# else:
#     print("not")

# n=int(input("Enter a no:"))
# rev=0
# while n>0:
#     rm=n%10
#     rev=rev*10+rm
#     n=n//10
# print("Reverse is:",rev)


# n=int(input("Enter a no:"))
# r=0
# a=n
# while n>0:
#     m = n%10
#     r = r*10+m
#     n = n//10
# if  a == r:
#    print("The given  no is pallindrome",r)
# else:
#     print("The given no is not pallindrome",r)




# s=input("Enter the string")
# r=""
# a=s
# count=len(s)
# while count>0:
#     r=r+s[count-1]
#     count=count-1
# if a==r:
#    print("Pallindrome")
# else:
#     print("Not")
# i=1
# while i<=10:
#     print(i)
#     if (i==5):
#         break
#     i=i+1

# i=0
# while i<=10:
#     i=i+1
#     if i==5:
#         break
#     print(i)

#
# i=0
# while i<10:
#     i=i+1
#     if i==5:
#         continue
#     print(i)

# while 2==3:
#     pass

# l=[1,2,3]
# for n in l:
#     print(n)

# n=['athira','abhi']
# for a in n:
#     print(a)

# for x in 'hello':
#     print(x)

# a=0
# n=[10,20,30,40]
# for x in n:
#     a=a+x
# print("sum is:",a)
#
# for i in range(3):
#     print("hai")
#
# for i in range(10):
#     print(i)
#
# for i in range(3,10):
#     print(i)
#
# for i in range(2,9,2):
#     print(i)

# l=[2,44,20,49,66,100,29,33,80]
# for i in l:
#     print(i)
#     if i==100:
#         break

# n=int(input("Enter the limit:"))
# print("Even numbers are:")
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

# n=int(input("Enter the limit:"))
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)


# n=int(input("Enter the limit:"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(3,n+1):
#     f=a+b
#     print(f)
#     a=b
#     b=f

# n=int(input("Enter the no:"))
# for i in range(1,11):
#     x=i*n
#     print(i,"*",n,"=",x)

# l=[2,3,4,5]
# for c in l:
#     print(c)
# else:
#     print("No items left")

# n=int(input("Enter the no:"))
# f=0
# for i in range(1,n+1):
#     if n%i==0:
#         f=f+1
# if f==2:
#     print("Prime number ")
# else:
#     print("Not a prime number ")

# l1=['anu','ammu','anju']
# l2=[100,200,300]
# for i in l1:
#     for j in l2:
#         print(i,j)

# n=int(input("Enter the limit:"))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#             print(i)

# n=int(input("Enter the number:"))
# x=1
# while n>0:
#     rem=n%10
#     x=x*rem
#     n=n//10
# print("product is,",x)
#
#
# for i in range(14,0,-2):
#      print(i)

# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()
#
# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# n=int(input("Enter the no of rows:"))
# k=65
# for i in range(n):
#     for j in range(0,i+1):
#         print(chr(k+j),end=' ')
#     print()

# n=int(input("Enter the no of rows:"))
# k=65
# for i in range(n):
#     for j in range(0,n):
#         print(chr(k+j),end=' ')
#     print()
#
# n=int(input("Enter the no of rows:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
#
# n=int(input("Enter the no of rows:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# for i in range(n, 0, -1):
#      for j in range(1,i):
#         print(j, end=' ')
#      print()
#
# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i*j,end=' ')
#     print()


# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
# for i in range(n, 0, -1):
#      for j in range(1,i):
#         print(j, end=' ')
#      print()


# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print()

# str='Good Morning'
# s1=slice(6)
# print(str[s1])
# s2=slice(1,9,3)
# print(str[s2])
# s3=slice(-2,-10,-2)
# print(str[s3])

# s='how u doing'
# print(s[:5])
# print(s[5:])
# print(s[2:8])
# print(s[-10:-4])
# print(s[-1:-11:-3])
# print(s[:])
# print(s[::-1])


# l=['red','blue','yellow','green','violet','green']
# print(l[3])
# print(l[-2])
#
# print(l[2:5])
# print(l[::-1])
# print(l[4:])
# print(l[:3])
# l[3]='lavender'
# print(l)
#
# if 'pink' in l:
#     print("Found")
# else:
#     print("Not found")
#
# print("Length is:",len(l))
#
# l.append('pink')
# print(l)
#
# l.insert(2,'rose')
# print(l)
#
# l.remove('pink')
# print(l)
#
# l[4]='rose'
# print(l)
#
# l.remove('rose')
# print(l)
# l.pop()
# print(l)
# l.pop(2)
# print(l)
#
# # l.clear()
# # print(l)
#
# del l[1]
# print(l)
#
# del l
# print(l)

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l1.append(l2)
# print(l1)
# l1.extend(l2)
# print(l1)
# print(l1[5][2])
# l1[5].append(777)
# print(l1)
# l1[5].insert(2,4)
# print(l1)

# l1=[1,2,3,4,5]
# l2=(6,7,8,9,10)
# l1.extend(l2)
# print(l1)

# l3=[100,1,78,54,102,3,90,45]
# l3.sort(reverse=True)
# print(l3)
#
# l=['red','blue','yellow','green','violet','green','Maroon']
# l.sort(reverse=True)
# print(l)

# l1=[1,2,3,4,5]
# l2=l1.copy()
# print(l2)
#
# l3=[6,7]
# l3=l1.copy()
# print(l3)

# l1=[1,2,3,4,5]
# print(max(l1))
# print(min(l1))
# print(sum(l1))

# l=[]
# n=int(input("Enter the limit:"))
# for i in range(1,n+1):
#     a=i*i
#     l.append(a)
# print(l)

# l1=[1,2,3,4]
# l2=['a','b','c']
# print(l1+l2)


# x=['ne','neha','nehala']
# print(min(x))
# print(max(x))

# l=[[1,2],[3,4],[5,6]]
# print(max(l))

# a=[1,2,3,4,5,6]
# b=a.pop(4)
# c=a.pop()
# d=a.pop(-1)
# print(b)
# print(c)
# print(d)
# print(a)

#
# l=[6,60,35,8,90]
# for i in l:
#     if i%5==0:
#         print(i)


# fname=input("Enter 1st name:")
# lname=input("Enter lat name:")
# def fullname(n1,n2):
#     fn=n1+''+n2
#     return fn
# z=fullname(fname,lname)
# print(z)

# def sum():
#     s=x+y
#     return s
# x=int(input("Enter the 1st no:"))
# y=int(input("Enter the 2nd no:"))
# z=sum()
# print("sum is",z)


# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f
# n=int(input("Enter the number:"))
# if n<0:
#     print("Factorial does not exist")
# elif n==0:
#     print("Factorial of 0 is 1")
# else:
#     f1=fact(n)
#     print("Factorial is ",f1)

# def fact(n1):
#     if n1==1:
#         return 1
#     else:
#         return (n1*fact(n1-1))
# n=int(input("Enter the number:"))
# if n<0:
#     print("Factorial does not exist")
# elif n==0:
#     print("Factorial of 0 is 1")
# else:
#     f1=fact(n)
#     print("Factorial is ",f1)


# def display(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# display(10,20,30)
#
# def display(*nums):
#     for i in nums:
#         print(i)
# display(10,20,30,40)

# def display(*args):
#     print("Last no is",args[3])
# display(10,20,30,40)

# def display(n1,*args):
#     for i in args:
#         print(i)
#     print("First no is ",n1)
# display(10,20,30,40)

# def display(c1,c2,c3):
#     print("Third one is",c3)
#
# display(c2="Nehala",c3="Nefitha",c1="Nefiya" )
#

# def display(**kwargs):
#     for k,v in kwargs.items();
#     print("%s==%s"%(k,v))

# l=[]
# def create():
#     n=int(input("Enter the number of items on the list:"))
#     for i in range(n):
#         x=int(input("Enter the item:"))
#         l.append(x)
#     print(l)
# def search():
#     y=int(input("Enter the item to be searched:"))
#     if y in l:
#         print("Item found")
#     else:
#         print("Item not found")
# def remove():
#     z=int(input("Enter the item to be removed:"))
#     if z in l:
#         l.remove(z)
#         print(l)
#     else:
#         print("Item not found")
# def replace():
#     a=int(input("Enter the element to be replaced:"))
#     b=int(input("Enter the new element:"))
#     for i in range(len(l)):
#         if l[i]==a:
#             l[i]=b
#     print(l)
# create()
# search()
# remove()
# replace()
#
# while True:
#     ch=int(input("1.Create \n2.Search \n3.Remove \n4.Replace \n Enter your choice:"))
#     if ch==1:
#         create()
#     if ch==2:
#         search()
#     if ch==3:
#         remove()
#     if ch==4:
#         replace()
#     else:
#         break;

# txt="apple,banana,grapes,orange"
# z=txt.split(",",2)
# print(z)

# print(100==100)
# print(100 is 100)
# print("ss" is "ss")
# p=[100]
# q=[100]
# print(p is q)
# s=lambda a:a+10
# b=s(60)
# print(b)
# print(s(20))

# x=lambda a,b:a*b
# print("Product is",x(2,3))

# odd=lambda x:(x%2==1)
# n=int(input("Enter the no:"))
# h=odd(n)
# if h:
#     print("odd")
# else:
#     print("even")
#
# l=[1,2,3,4,5]
# x=list(filter(lambda x:(x%2==0),l))
# print(x)

# l=[12,3,5,678,23,2]
# odd=list(filter(lambda x:(x%2==1),l))
# print(odd)

# l=[16,12,4,6,78,42,50]
# a=list(map(lambda x:(x*2),l))
# print(a)

# from functools import reduce
# l=[1,2,3,4,5]
# p=reduce(lambda x,y:x*y,l)
# print(p)

# class student:
#     name='anu'
# obj=student()
# print(obj.name)

# class A:
#     def display(self):
#         print('simple function')
#     def sum(s,a,b):
#         print('sum is:',a+b)
#
# obj=A()
# obj.display()
# obj.sum(12,34)

# class B:
#     def fact(self,n):
#         f=1
#         for i in range(1,n+1):
#             f=f*i
#         print("Factorial is",f)
# obj=B()
# obj.fact(5)
#
# class B:
#     def fact(self):
#         f=1
#         n=int(input("Enter the no:"))
#         for i in range(1,n+1):
#             f=f*i
#         print("Factorial is",f)
# obj=B()
# obj.fact()

# class A:
#     def display():
#         print("Without self variable")
#     def check(self):
#         print("With self variable")
#
# ob=A()
# # ob.display()
# ob.check()

# ob=A
# ob.display()

# class student:
#     def __init__(self):
#         print("Non-parameterized constructor")
# ob=student()

# class student():
#     def __init__(self,name):
#         print("Name is",name)
# ob=student("nehala")

# class student:
#     def __init__(self,name,id):
#         self.n=name
#         self.id=id
#         print("Name of the student is",self.n+" and id is",self.id)
#     def display(self):
#         print("Name is",self.n)
#         print("Id is ",self.id)
# ob=student("Nehala",27)
# ob.display()

# class student:
#     def __init__(self,name,age):
#         self.n=name
#         self.age=age
# ob=student("Nehala",20)
# print("Name is",ob.n)
# print("Age is ",ob.age)

# class student:
#     def __init__(s,name,age):
#         s.n=name
#         s.age=age
#     def display(x):
#         print("Name is:",x.n)
#         print("Age is:",x.age)
# ob=student("Nehala",20)
# ob.display()

# class student:
#     def __init__(s,name,age):
#         s.n=name
#         s.age=age
#     def display(x):
#         print("Name is:",x.n)
#         print("Age is:",x.age)
# ob=student("Nehala",20)
# ob.display()
# ob.age=21
# print("Age is changed to",ob.age)
# ob.display()

# class object:
#     a=0
#     def __init__(s):
#         object.a=object.a+1
# ob=object()
# ob2=object()
# print("Count:",object.a)

# class product:
#     def __init__(s,a,b):
#         s.a=a
#         s.b=b
#     def display(x):
#         print("Product is ",x.a*x.b)
# n=int(input("Enter the 1st no:"))
# m=int(input("Enter the 2nd no:"))
# ob=product(n,m)
# ob.display()

# class student:
#     def __init__(self):
#         print("Object created")
#     def __del__(self):
#         print("Object deleted")
# ob=student()
# del ob

# class A:
#     def displayA(self):
#         print("Base class")
# class B(A):
#     def displayB(self):
#         print("Derived class")
# ob=B()
# ob.displayA()
# ob.displayB()

# class A:
#     def read(s):
#          s.a=int(input("Enter 1st no:"))
#          s.b=int(input("Enter 2nd no:"))
# class B(A):
#     def sum(x):
#         print("Sum is ",x.a+x.b)
# ob=B()
# ob.read()
# ob.sum()

# class A:
#     def read(s):
#          s.a=int(input("Enter 1st no:"))
#          s.b=int(input("Enter 2nd no:"))
# class B(A):
#     def sum(x):
#         x.s=x.a+x.b
#         print("Sum is ",x.s)
# class C(B):
#     def average(y):
#         y.av=y.s/2
#         print("Average is",y.av)
# ob=C()
# ob.read()
# ob.sum()
# ob.average()

# class A:
#     def personal(s):
#         s.name=input("Enter the name:")
#         s.age=int(input("Enter the age:"))
#         s.ph=int(input("Enter the phone no:"))
# class B:
#     def education(e):
#         e.qu=input("Qualification:")
#         e.ma=int(input("Enter the marks:"))
#         e.un=input("Enter the name of university studied:")
# class C(A,B):
#     def student(l):
#         print("                 ")
#         print("Student details")
#         print("                         ")
#         print("Name:",l.name)
#         print("Age:",l.age)
#         print("Phone number:",l.ph)
#         print("Qualification:",l.qu)
#         print("Marks:",l.ma)
#         print("University:",l.un)
# ob=C()
# ob.personal()
# ob.education()
# ob.student()

# class A:
#     def read(s):
#          s.a=int(input("Enter 1st no:"))
#          s.b=int(input("Enter 2nd no:"))
# class B(A):
#     def sum(x):
#         x.s=x.a+x.b
#         print("Sum is ",x.s)
# class C(A):
#     def average(y):
#         print("Average is",(y.a+y.b)/2)
# class D(A):
#     def product(z):
#         print("Product is",z.a*z.b)
# ob=B()
# ob.read()
# ob.sum()
# ob1=C()
# ob1.read()
# ob1.average()
# ob2=D()
# ob2.read()
# ob2.product()

# from abc import ABC, abstractmethod
# class Polygon(ABC):#abstract class
#     @abstractmethod
#     def sides(self):#abstract method
#         pass
#     def display(self):
#         print("Non abstract method")
# class Triangle(Polygon):
#     def sides(self):
#         print("Triangle has 3 sides")
# t=Triangle()
# t.sides()
# t.display()

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("hello")
# ob=Human()
# ob.sayhello()
# ob.sayhello("kiran")

# def add(datatype,*args):
#     if datatype=="int":
#         answer=0
#     if datatype=="str":
#         answer=''
#     for x in args:
#         answer=answer+x
#         print(answer)
# add('int',5,6)
# add('str','hi','geeks')


# class Rectangle():
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def getArea(self):
#         print(self.length*self.breadth,"is area of the rectangle")
# class Square(Rectangle):
#     def __init__(self,side):
#         self.side=side
#     def getArea(self):
#         print(self.side*self.side," is area of square")
# s=Square(4)
# s.getArea()

# class Computer():
#     def __init__(self,computer1,ram1):
#         self.computer2=computer1
#         self.ram2=ram1
# class Mobile(Computer):
#     def __init__(self,computer,ram,storage):
#         super().__init__(computer,ram)
#         self.storage=storage
# Apple=Mobile('Apple',2,64)
# print("The mobile is",Apple.computer2)
# print("The ram is",Apple.ram2)
# print("The storage is",Apple.storage)

# l=[i*i for i in range(1,5)]
# print(l)

# l=[i for i in range(1,10) if i%2==0]
# print(l)

# l=[x for x in "how u doing" if x in "a,f,d,i,x,j,g,l,w"]
# print(l)

# l=[3,3.9,'hai',21,44.3]
# l3=[s for s in l if type(s)==int]
# print(l3)

# l=[12,2,-9.5,-2,99,-8,22]
# k=[x for x in l if x>0]
# print(k)

# str=["Anu","Binu","Celin","Dona","Eric"]
# l1=[fst[0] for fst in str]
# print(l1)

# clrs=['red','pink','white','green','yellow']
# newlst=[x for x in clrs if 'i' in x]
# print(newlst)
# newlst1=[x for x in clrs if x!="green"]
# print(newlst1)
# newlst2=[x.upper() for x in clrs]
# print(newlst2)
# newlst3=['hii' for x in clrs]
# print(newlst3)

# l=[x if x!='pink' else 'blue' for x in clrs]
# print(l)

# l=[lambda a=a:a*10 for a in range(1,10)]
# for i in l:
#     print(i())

# try:
#     x=int(input("Enter 1st no:"))
#     y=int(input("Enter 2nd no"))
#     z=x/y
#     print(z)
# except Exception as e:
#     print("Exception",e)
# # except ZeroDivisionError as x:
# #     print(x)
# # except ValueError as y:
# #     print(y)
# import re
#
# s='sat mat rat hat cat 34567 890 9875 3784 378 49 02987'
# l=re.findall(r'[spr]',s)
# print(l)
# l1=re.findall(r'[spr]a',s)
# print(l1)
# l1=re.findall(r'[spr]at',s)
# print(l1)
# l1=re.findall(r'[^spr]at',s)
# print(l1)
# l1=re.findall(r'\d{1,2}',s)
# print(l1)
# l1=re.findall(r'\d{2,3}',s)
# print(l1)
# l1=re.findall(r'\d{3}',s)
# print(l1)
# l1=re.findall(r'\b\d{3}',s)
# print(l1)
# l=re.findall(r'\b\d{3}\b',s)
# print(l)
#
# t='The rain in Spain is at 10am'
# x=re.search('\s',t)
# print(x)
# print(x.start())
# y=re.search('\d',t)
# print(y)
# print(y.start())
# z=re.search('Spain',t)
# print(z)
# print(z.start())
# a=re.search('sun',t)
# print(a)
# print(a.start())
# s='The girl is very clever'
# x=re.search('^The.*clever$',s)
# if x:
#     print('yes')
# else:
#     print('no')
# x=re.search('^The.*clevers$',s)
# if x:
#     print('yes')
# else:
#     print('no')

# s='rose and jasmine are flowers'
# # x=re.split(' ',s)
# # print(x)
# # y=re.split('\s',s)
# # print(x)
# x=re.split(',',s)
# print(x)
# y=re.split(' ',s,3)
# print(y)
# import re
#
# t="rose and white are colours"
# x=re.sub('\s','*',t)
# print(x)
# y=re.sub('\s','*',t,2)
# print(y)

# import re

# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
#
# def check(email):
#     if (re.search(regex, email)):
#         print("Valid Email")
#     else:
#         print("Invalid Email")
#
# email =input("Enter the email id")
# check(email)
#
# import re
#
#
# def isValid(s):
#     # 1) Begins with 0 or 91
#     # 2) Then contains 7 or 8 or 9.
#     # 3) Then contains 9 digits
#     Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
#     return Pattern.match(s)
#
#
# # Driver Code
# s =int(input("Enter the phone no:"))
# if (isValid(s)):
#     print("Valid Number")
# else:
#     print("Invalid Number")

# regex = '^[6-9]\d{9}$'


# def check(ph):
#     if (re.search(regex,ph)):
#         print("Valid Phone number")
#     else:
#         print("Invalid Phone number")
#
# ph=input("Enter the phone number:")
# check(ph)

# import re
#
# regex ="^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
#
#
# def check(pin):
#     if (re.search(regex,pin)):
#         print("Valid Pincode")
#     else:
#         print("Invalid Pincode")
#
# pin=input("Enter the Pincode:")
# check(pin)
# import re
#
#
# # Function to validate the pin code
# # of India.
# def isValidPinCode(pinCode):
#     # Regex to check valid pin code
#     # of India.
#     regex =
#
#     # Compile the ReGex
#     p = re.compile(regex);
#
#     # If the pin code is empty
#     # return false
#     if (pinCode == ''):
#         return False;
#
#     # Pattern class contains matcher() method
#     # to find matching between given pin code
#     # and regular expression.
#     m = re.match(p, pinCode);
#
#     # Return True if the pin code
#     # matched the ReGex else False
#     if m is None:
#         return False
#     else:
#         return True
#
#
#     num1 = "132103";

#     print(num1, ": ", isValidPinCode(num1));
#
#     # Test case 2:
#     num2 = "201 305";
#     print(num2, ": ", isValidPinCode(num2));
#
#     # Test case 3:
#     num3 = "014205";
#     print(num3, ": ", isValidPinCode(num3));
#
#     # Test case 4:
#     num4 = "1473598";
#     print(num4, ": ", isValidPinCode(num4));


