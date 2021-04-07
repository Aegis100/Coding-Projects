import time
import random
from random import randint
time.sleep(.8)
randomhedgeclimb_starter1 = random.randint(0, 100)
if randomhedgeclimb_starter1 >= 95:
    print ("After multiple attempts, you climb the hedge. What you see amazes you. You see a sprawling maze as far as the eyes can see, within what looks like a meteor crator, with you on the outer edge of it. On the edges you can see faint flickering flames with what looks like buildings by them.")
    print ("Due to the action of climbing the hedge, you are completely exhausted and you pass out lying down on it.")
if randomhedgeclimb_starter1 <= 94 >= 65:
    time.sleep(.8)
    print ("After hours of trying, you almost reach the hedge. Your body strains under the stress of climbing, and you are so close! However, you lose your footing and you fall onto the dirt path on your head. Your vision fades to black. You never wake up.")
    death()
if randomhedgeclimb_starter1 <=64:
    time.sleep(.8)
    print ("After hours of trying, you are unsuccessful in your attempts. You lie exhausted on the ground and go to sleep against an apple tree.")

