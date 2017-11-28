#!/usr/bin/python

import _thread as thread
import time

precedencematrix=[[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,1,0,0,0,1,1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,0,0],[0,0,0,1,1,1,0]]
tasktimings=[10,5,6,7,8,6,13]
taskpool=[0,1,2,3,4,5,6]
taskmutual=[6]
affinity=[1,1,3,4,0,1,3]
temppool=taskpool
ntasks=7
temppred=precedencematrix

def update_pred_matrix(t_num):
    for x in range(ntasks):
        if temppred[x][t_num] == 1:
            temppred[x][t_num]=0


def check_affinity(t_num):
    return affinity[t_num]

def calc_dependencies(t_num):
     temp = 0
     for x in range(ntasks):
         if temppred[x][t_num]==1:
            temp=temp+1
     return temp

def precedence_check(t_num):
    temp = 0
    for x in range(ntasks):
        if temppred[t_num][x] == 1:
            temp = temp + 1
    if temp>=1:
        return 0
    else:
        return 1
def mutual (t_num):
    if t_num in taskmutual:
        return 1
    else:
        return 0
def priority_function(t_num):
        p=((1/tasktimings[t_num])*0.6+calc_dependencies(t_num)*0.2+check_affinity(t_num)*0.1+mutual(t_num)*0.5)*precedence_check(t_num)
        return p
def update_temppool(t_num):
    temppool.remove(t_num)
def assign_task():
    max_priority = -999
    for x in range(len(temppool)):
        p=priority_function(temppool[x])
        if p>max_priority:
            max_priority=p
            task=temppool[x]
    update_pred_matrix(task)
    temppool.remove(task)
    print (max_priority)
    return task
# Define a function for the thread
#def print_task( threadName, ttime):
   #count = 0
   #while count < ttime:
    #  count=count+1
     # print("%s: %s" % ( threadName, count ))


# Create two threads as follows





try:
    for x in range(ntasks):
        p = assign_task()
        print (p)
        print ("-------------")
   
  # thread.start_new_thread(print_task, (tasknames[1], tasktimings[1],))
  # thread.start_new_thread(print_task, (tasknames[2], tasktimings[2],))
  # thread.start_new_thread(print_task, (tasknames[3], tasktimings[3],))
  # thread.start_new_thread(print_task, (tasknames[4], tasktimings[4],))
except:
   print ("Error: unable to start thread")

#while 1:
 #  pass
exit()