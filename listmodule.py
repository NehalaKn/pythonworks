
l=[]
def create():
    n=int(input("Enter the number of items on the list:"))
    for i in range(n):
        x=int(input("Enter the item:"))
        l.append(x)
    print(l)
def search():
    y=int(input("Enter the item to be searched:"))
    if y in l:
        print("Item found")
    else:
        print("Item not found")
def remove():
    z=int(input("Enter the item to be removed:"))
    if z in l:
        l.remove(z)
        print(l)
    else:
        print("Item not found")
def replace():
    a=int(input("Enter the element to be replaced:"))
    b=int(input("Enter the new element:"))
    for i in range(len(l)):
        if l[i]==a:
            l[i]=b
    print(l)
# create()
# search()
# remove()
# replace()

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
