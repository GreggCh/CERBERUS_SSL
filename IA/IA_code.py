import lcm, time, random
from ..LCM.cerberus_lcm import IA

lc = lcm.LCM()

msg = IA()

while True:
    rand = random.uniform(0,1)
    msg.id = 1
    msg.x_position = 5.6 + rand

    lc.publish("aaa", msg.encode())

    time.sleep(0.1)