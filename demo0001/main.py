import string
import random
import threading

def randomCodes():
    chars = string.ascii_letters + string.digits
    for i in range(20):
        print(threading.current_thread().name + ' : ' +''.join([random.choice(chars) for i in range(32)]))

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=randomCodes, name='Thread'+str(i+1))
        t.start()
        t.join()
