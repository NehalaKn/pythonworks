# # n=int(input("Enter the no of rows:"))
# # for i in range(1,n+1):
# #     for j in range(i,0,-1):
# #         print(j,end=' ')
# #     print()
# #
# #
# #
# # for i in range(5):
# #     for j in range(5):
# #         if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
# #             print("*", end="")
# #         else:
# #             print(end=" ")
# #     print()
#
#
#
# n=int(input("Enter the no of rows:"))
# print("The 8 Star Pattern")
# for i in range(1, n * 2):#1,7
#     if i == 1 or i == n or i == n * 2 - 1:#1,4,7
#         for j in range(1, n + 1):#1,4
#             if j == 1 or j == n:#1,4
#                 print(end = ' ')
#             else:
#                 print('*', end = '')
#     else:
#         for k in range(1, n + 1):#1,4
#             if k == 1 or k == n:#1,4
#                 print('*', end = '')
#             else:
#                 print(end = ' ')
#     print()
#
#
#
#
#
#
#
#
# n = int(input('Enter number of row: '))#5
# for i in range(1, n+1):#1,5
#     for j in range(1,n-i+1):#1,4
#         print(" ", end="")
#     for j in range(1, 2*i):#1,3
#         if j==1 or j==2*i-1:#1,3,5
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n-1,0, -1):
#     for j in range(1,n-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         if j==1 or j==2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# f=open("file.txt",'r')
# print(f.read())
# # # print(f.readline())
# # print(f.read(2))
# for i in f:
#     print(i)
# f.close()

# f=open("file.txt",'w')
# f.write("haii..how are you")
# f.close()
#
# f=open("file.txt",'r')
# print(f.read())

# f=open("file.txt",'r')
# f.seek(10)
# print(f.read())

# def test(fname):
#     with open(fname) as f:
#         contents=f.readline()
#         print(contents)
# test('file.txt')
# def test(fname):
#     with open(fname) as f:
#         contents=f.readlines()
#         print(contents)
# test('file.txt')

# from shutil import copyfile
# copyfile('file.txt','copy.txt')

# days={"Mon",'Tue','Wed'}
# print(list(enumerate(days)))
# print(list(enumerate(days,5)))

# def file_length(fname):
#     with open(fname) as f:
#         for index,value in enumerate(f,1):
#             pass
#     return index
# print("Length is",file_length('file.txt'))

# class A:
#     def __init__(self,name,age):
#         self.name=name#public
#         self.__age=age#private
#         # self._age=age#protected
#     def display(self):
#         print(self.name)
#         print(self.__age)
# ob=A("Nehala",21)
# ob.display()
# print(ob.name)
# print(ob._A__age)
# # print(ob.__age)#Error

stack = ["Red", "White", "Green"]
stack.append("Black")
stack.append("Blue")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print('\nInitial stack')
print(stack)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:',stack)
print()
print('\n')

queue = ["Red", "White", "Green"]
queue.append("Black")
queue.append("Blue")
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("\nInitial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)