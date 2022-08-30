# import examplemodule as exxmod
# exxmod.display()
# exxmod.sum()
#
#
# na=exxmod.student['name']
# ag=exxmod.student['age']
# ma=exxmod.student['mark']
#
# print(na)
# print(ag)
# print(ma)

# import platform
# print(platform.system())

# import math
# print(math.sqrt(64))

# from examplemodule import student
# print("name is:",student['name'])
#
#
# from examplemodule import sum
# sum()
#
# from examplemodule import *
# display()
# sum()
# print("name is :",student['name'])

# import listmodule
# while True:
#     ch=int(input("1.Create \n2.Search \n3.Remove \n4.Replace \n Enter your choice:"))
#     if ch==1:
#         listmodule.create()
#     if ch==2:
#         listmodule.search()
#     if ch==3:
#         listmodule.remove()
#     if ch==4:
#         listmodule.replace()
#     else:
#         break;

from listmodule import *
while True:
    ch=int(input("1.Create \n2.Search \n3.Remove \n4.Replace \n Enter your choice:"))
    if ch==1:
        create()
    if ch==2:
        search()
    if ch==3:
        remove()
    if ch==4:
        replace()
    else:
        break;




