import CoDrone_mini
import time
drone = CoDrone_mini.CoDrone()
time.sleep(1)
drone.pair()
time.sleep(1)
drone.takeoff()
time.sleep(1)
drone.set_trim(-32, -30)
time.sleep(1)
drone.set_roll(-100)
time.sleep(3)
drone.set_pitch(100)

