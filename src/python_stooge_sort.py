#Python Stooge Sort - A Python Implementation of Stooge Sort


#Imports
import random
import datetime

#Functions
def order_elements(list):
    global comparisons

    if list[0] > list[1]:
        list_0=list[0]
        list[0]=list[1]
        list[1]=list_0

    comparisons+=1
    return(list)

def stooge_sort(list):
    if len(list) <= 3:
        list[:len(list)-1]=order_elements(list[:len(list)-1])
        list[1:len(list)]=order_elements(list[1:len(list)])
        list[:len(list)-1]=order_elements(list[:len(list)-1])
    else:
        list[:len(list)-1]=stooge_sort(list[:len(list)-1])
        list[1:len(list)]=stooge_sort(list[1:len(list)])
        list[:len(list)-1]=stooge_sort(list[:len(list)-1])

    return(list)
    
#Global Variables
list=[]
comparisons=0
time_info=[0,0]

#Main Program
for list_length in range(3,101):
    file_txt=open("output.txt","a")
    list=random.sample(range(1,101),list_length)
    comparisons=0

    time_info[0]=datetime.datetime.now()
    list=stooge_sort(list)
    time_info[1]=datetime.datetime.now()

    print("\n\nList Length: {list_length}\nComparisons: {comparisons}\nElapsed Time: {elapsed_time}".format(list_length=len(list),comparisons=comparisons,elapsed_time=str(time_info[1]-time_info[0])))
    file_txt.write("\n\nList Length: {list_length}\nComparisons: {comparisons}\nElapsed Time: {elapsed_time}".format(list_length=len(list),comparisons=comparisons,elapsed_time=str(time_info[1]-time_info[0])))
    file_txt.close()