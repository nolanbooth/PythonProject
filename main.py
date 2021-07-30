import CoDrone_mini
import time
print("imported!")
drone = CoDrone_mini.CoDrone()
print("CoDrone_Mini created!")
drone.pair()
print("drone paired!")

'''TAKEOFF'''
drone.takeoff()
print("takeoff started...")
time.sleep(1)
drone.set_trim(-25, -38)
print("Trimming")
time.sleep(2)

'''FLIGHT'''
print("drone is hovering!")
drone.set_throttle(100)
print("throttle set to 100%")
time.sleep(1)
drone.hover(3)
time.sleep(1)
drone.set_roll(50)
print("roll set to 50")
time.sleep(1)
drone.set_pitch(-50)
print("pitch set to -50")
time.sleep(1)
print("Non-human controlled flight finished. Duration: 4 seconds")


'''LANDING'''
drone.land()
print("landing...")
time.sleep(3)
print("Landed!")
drone.close()
