# Python program to understand 
# the concept of pool
import multiprocessing
import os
  
def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n*n)
  
if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4,5] # ahi lo hace el mismo proceso
    #myList=(n for n in (10000)) ahi como es mas carga se lo reparte entre mas

  
    # creating a pool object
    p = multiprocessing.Pool()
  
    # map list to target function
    result = p.map(square, mylist)
  
    print(result)