import lcm, time, random
from cerberus_lcm import IA

lc = lcm.LCM()

msg = IA()

while True:
    rand = random.uniform(0,1)
    msg.id = 1
    msg.x_position = 5.6 + rand
    msg.y_position = 3.0 - rand
 
    lc.publish("IA", msg.encode())

    time.sleep(0.1)