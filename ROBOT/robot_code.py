import lcm
from ..LCM.cerberus_lcm import IA

def handler(channel, data):
    msg = IA.decode(data)
    #posteriormente irei tirar o "team" como exemplo de modificação
    print(f"""
        channel :  {channel}
        id :   {msg.id}
        x_position : {msg.x_position}
    """)

lc = lcm.LCM()

subscriber = lc.subscribe("IA", handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass