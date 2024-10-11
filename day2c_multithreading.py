# multithreading = used to perform multiple tasks concurrently
# usage threading.Thread(target=function, args=(args))


import threading
import time


def cook_the_noodles(noodle, minutes):
    time.sleep(6)
    print(f"You finished cooking the {noodle} for {minutes} minutes")

def open_packet():
    time.sleep(2)
    print("You open the packet")
    
def serve_noodles():
    time.sleep(8)
    print("You served the noodles! Itadakimasu!")
    
    # Note: If there is only 1 argument, you need to supply args with a comma **args=("Mi goreng",)
chore1 = threading.Thread(target=cook_the_noodles, args=("Mi goreng", "3"))
chore1.start()
chore2 = threading.Thread(target=open_packet)
chore2.start()
chore3 = threading.Thread(target=serve_noodles)
chore3.start()

# this is needed for the program to wait all the chore to complete before executing the print below
chore1.join()
chore2.join()
chore3.join()

print("All steps completed!")