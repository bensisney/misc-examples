from threading import Thread
from time import sleep
import random

def printRandom():
    answer = 3
    print(f"T1: I'm going to try and randomly guess the number {answer}!")
    while True:
        number = random.randint(0,5)
        if number == answer:
            print(f'T1: {number} is equal to {answer}! Thread Complete')
            break   
        else:
            print(f'T1: {number} is not equal to {answer}, trying again.')
        sleep(random.randint(1,3))

def countUp():
    count = 10
    print(f"T2: I'm counting to {count}")
    for x in range(count):
        print(f'T2: Count is {x}')
        sleep(random.randint(1,3))
    print(f"T2:Done counting to {count}")

thread_1 = Thread(target=printRandom)
thread_2 = Thread(target=countUp)

try:
    while True:
        thread_1.start()
        thread_2.start()
        
        # Wait for Threads to Finish
        thread_1.join()
        thread_2.join()       
        break
except KeyboardInterrupt:
    print('Stopping Program')

