def forLoop(n):

    for i in range(0,n): # Its gonna start counting from 0 to n-1 here, n is not counted
        print(str(i+1), ": time in loop")

        #Break example. if you wanted to break from the loop in case a condition
        #is fulfilled
        
        if( i == n-2): 
            break


#For running the code
forLoop(10)

'''
Output of the code:

1 : time in loop
2 : time in loop
3 : time in loop
4 : time in loop
5 : time in loop
6 : time in loop
7 : time in loop
8 : time in loop
9 : time in loop
10 : time in loop'''
