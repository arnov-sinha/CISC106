#!/usr/bin/env python
ssdldj
#While Loop example

tempCounter = -1 # used to store values of the counter.

def counter():
  '''
    This function is used as a counter from 1 - 10.
    Parameters: none.
    return : counter result of type int.
  '''
  tempCounter = 1
  while tempCounter < 10 :  # You can also put the expression in parenthesis
    print("Temp Counter is now :" + str(tempCounter))
    tempCounter = tempCounter + 1  # increments the counter by 1
  #the code underneath would work only if the while loop is completed.
  
  return tempCounter # returns the result to the main flow. 

'''
How to run:

>>>counter()

'''
  
