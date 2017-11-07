#!/usr/bin/python

import _thread as thread
import time

precedencematrix=[[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,1,0]]
tasktimings=[10,5,6,7,8]
tasknames=["t1","t2","t3","t4","t5"]

# Define a function for the thread
def print_task( threadName, ttime):
   count = 0
   while count < ttime:
      count=count+1
      print("%s: %s" % ( threadName, count ))
   
# Create two threads as follows
try:
   for x in range (len(precedencematrix[0])):
     if precedencematrix[0][x]==0:
      thread.start_new_thread(print_task, (tasknames[0], tasktimings[0],))
   thread.start_new_thread(print_task, (tasknames[1], tasktimings[1],))
   thread.start_new_thread(print_task, (tasknames[2], tasktimings[2],))
   thread.start_new_thread(print_task, (tasknames[3], tasktimings[3],))
   thread.start_new_thread(print_task, (tasknames[4], tasktimings[4],))
except:
   print ("Error: unable to start thread")

while 1:
   pass
