from modules.wifi.WifiModule import WifiModule
#from modules.gps.GPSModule import GPSModule
from modules.servo.ServoModule import ServoModule
import _thread
import utime


def displayModuleStatus():
    while True:
        WifiModule.displayStatus()
        utime.sleep(5)
        #GPSModule.displayStatus()
        #utime.sleep(10)


def servoMotorStart():
    while True:
        ServoModule.forward()
        utime.sleep(5)
        ServoModule.back()
        utime.sleep(5)


# Connect to WiFi network
_thread.start_new_thread(WifiModule.connect())
# Connect to GPS
#_thread.start_new_thread(GPSModule.read())
# Start Servomotors
_thread.start_new_thread(servoMotorStart())
displayModuleStatus()
