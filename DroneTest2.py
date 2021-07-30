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

'''TAKEOFF'''
drone.takeoff()
print("takeoff started")
time.sleep(1)
drone.set_trim(-10, -10)
time.sleep(1)
print("trim set!")
drone.hover(2)
print("takeoff complete!")
time.sleep(1)
drone.set_roll(40)

'''FLIGHT''' 
print("flight started")
time.sleep(1)
print("flip started")
drone.flip()
print("flip complete")
time.sleep(1)
drone.set_pitch(100)
print("drone returning!")
time.sleep(1)
drone.hover(2)
time.sleep(1)
#drone.fly_circle()
#print("circle started")
#time.sleep(15)
#print("circle complete!")
#drone.hover(3)
#time.sleep(1)
print("Landing started")

'''LANDING'''
drone.land()
print("landing started")
time.sleep(2)
print("landing complete!")
time.sleep(2)
print("NON-human flight complete! Lasted about 9 seconds.")
time.sleep(1)
counter = 0
while counter < 2:
    print(":O")
    counter += 1
