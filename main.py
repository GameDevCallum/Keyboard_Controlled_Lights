from phue import Bridge
import random

bridge = Bridge("192.168.1.90")

bridge.connect()

bridge.get_api()

bridge.set_light(2, 'on', True)
bridge.set_light(2, "hue", random.randrange(0, 65535))
