#!/usr/bin/python

import threading
import time

precedencematrix=[[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,1,0,0,0,1,1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,0,0],[0,0,0,1,1,1,0]]
tasktimings=[10,5,6,7,8,6,13]
humantasks=[3,2,5]
robottasks=[0,1,4]
taskmutual=[6]
affinity=[1,1,3,4,0,1,3]
ntasks=7

#temporary matrices
temphp=list(humantasks)
temprp=list(robottasks)
tempmp=list(taskmutual)
temppred=list(precedencematrix)

class myThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
       if self.threadID==1:
            assign_human()
       if self.threadID==2:
            assign_robot()
       threadLock.acquire()
       if self.threadID==3:
            assign_both()
       threadLock.release()
threadLock=threading.Lock()
threads = []

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


def assign_task(param):
    max_priority = -999
    if param==0:
        for x in range(len(temphp)):
            p=priority_function(temphp[x])
            if p>max_priority:
                max_priority=p
                task=temphp[x]
        if max_priority>0:
            temphp.remove(task)
            update_pred_matrix(task)
            time.sleep(tasktimings[x])
            return task
        if max_priority <= 0:
            time.sleep(5)
    if param == 1:
        for x in range(len(temprp)):
            p=priority_function(temprp[x])
            if p>max_priority:
                max_priority=p
                task=temprp[x]
        if max_priority>0:
            temprp.remove(task)
            update_pred_matrix(task)
            time.sleep(tasktimings[x])
            return task
        if max_priority <= 0:
            time.sleep(5)
    if param == 2:
        for x in range(len(tempmp)):
            p=priority_function(tempmp[x])
            if p>max_priority:
                max_priority=p
                task=tempmp[x]
        if max_priority>0:
            tempmp.remove(task)
            update_pred_matrix(task)
            time.sleep(tasktimings[x])
            return task
        if max_priority <= 0:
            time.sleep(5)
# Define a function for the thread
#def print_task( threadName, ttime):
   #count = 0
   #while count < ttime:
    #  count=count+1
     # print("%s: %s" % ( threadName, count ))


# Create two threads as follows
def assign_human():
    while temphp:
        t=assign_task(0)
        print("Human task : "+str(t))
def assign_robot():
    while temprp:
        t=assign_task(1)
        print("Robot task : " + str(t))
def assign_both():
    while tempmp:
        t=assign_task(2)
        print("Mutual task : " + str(t))


thread1 = myThread(1, "human")
thread2 = myThread(2, "robot")
thread3 = myThread(3, "human+robot")

thread1.start()
thread2.start()
thread3.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

for t in threads:
    t.join()
#while 1:
 #  pass
exit()