# from time import sleep
# from threading import Thread
# def task():
#     print("Wait for the moment")
#     sleep(3)#milliseconds
#     print("This is from another thread")
# # task()
# th=Thread(target=task())
# th.start()
# from time import sleep
# from threading import Thread
# def task(sleep_time,msg):
#     print("Wait for the moment")
#     sleep(sleep_time)#milliseconds
#     print(msg)
# # task()
# th=Thread(target=task,args=(3,"Haii welcome to new thread msg"))
# th.start()
import time
import threading
def cal_sqre(num):
    print("Calculate the square root of the given number")
    for n in num:
        time.sleep(0.3)
        print("Square is:",n*n)
def cal_cube(num):
    print("Calculate the cube of the given number")
    for n in num:
        time.sleep(0.3)
        print("Cube is:",n*n*n)
arr=[4,5,6,7,2]
t1=time.time()
cal_sqre(arr)
cal_cube(arr)
print("Total time taken by the thread is:",time.time()-t1)


import time
import threading
def cal_sqre(num):
    print("\nCalculate the square root of the given number")
    for n in num:
        time.sleep(0.3)
        print("Square is:",n*n)
def cal_cube(num):
    print("Calculate the cube of the given number")
    for n in num:
        time.sleep(0.3)
        print("Cube is:",n*n*n)
arr=[4,5,6,7,2]
t1=time.time()
th1=threading.Thread(target=cal_sqre,args=(arr,))
th2=threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("Total time taken by the thread is:",time.time()-t1)