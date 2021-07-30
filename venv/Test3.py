import CoDrone_mini
import time
print("imports complete!")
time.sleep(1)
drone = CoDrone_mini.CoDrone()
print("drone created!")
time.sleep(1)
drone.pair()
print("drone paired!")
time.sleep(2)

drone.takeoff()
time.sleep(1)
drone.set_trim(-35, -32)
time.sleep(1)
drone.hover(2)
drone.fly_circle()
time.sleep(10)
drone.land()
