import random

def multiplication():
    while True:
        A = random.randint(1,9)                 #stores a random integer A between 1 and 9
        B = random.randint(1,9)                 #stores a random integer B between 1 and 9
        C = A * B                               #multiplies A and B together as C
        print(f'A: {A}, C: {C}')                #Prints A and C for every result until C = 4

        if C == 4:                              #If C = 4 , print ‘Success!’ and the results for A and B
            print(f'Success! A: {A} B: {B}')    
            break


multiplication()