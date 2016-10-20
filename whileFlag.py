# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 06:58:04 2016

This program shows how to use while Loop when you dont have a condition in mind 
and want to use while loop indefinetly

@author: arnov
"""

'''
We define a flag variable of type boolean. This can be a global or local 
variable. 
'''
flag = False 
counter = 1 # Is used to calculate the no of times while loop has run.

while flag == False:
    # syntax-> while <condition> :
    print("The while loop has run ", str(counter), " times till now.")
    print("Do you want to continue with the while loop?")
    reply = str(input())
    '''
    The following takes in the user input. notice i have put both cases of Y and N
    and also a condition incase someone enters something else. Its a good habit.
    '''
    if reply == 'N' or reply == 'n':
        flag = True
    elif reply == 'Y' or reply == 'y' :
        flag = False
    else :
        print("Enter Y/N only.")
        reply = str(input())    
    counter = counter + 1

print("While loop ended. final counter tally:" , str(counter))


'''
Output of the Program:

The while loop has run  1  times till now.
Do you want to continue with the while loop?
asd
Enter Y/N only.
y
The while loop has run  2  times till now.
Do you want to continue with the while loop?
Y
The while loop has run  3  times till now.
Do you want to continue with the while loop?
N
While loop ended. final counter tally: 4
'''
