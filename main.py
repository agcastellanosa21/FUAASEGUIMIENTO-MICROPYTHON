import WifiModule
import GPSModule
import ServoModule
import _thread
import utime


# This method shows on the OLED screen the connection status of the GPS and Wi-Fi network,
# they alternate by means of a delay of 10 seconds
def checkStatus():
    while True:
        _thread.start_new_thread(WifiModule.displayStatus, ())
        utime.sleep(10)
        _thread.start_new_thread(GPSModule.displayStatus, ())
        utime.sleep(10)


# Start Wifi Connection
_thread.start_new_thread(WifiModule.connect, ())
# Start GPS Geocoding
_thread.start_new_thread(GPSModule.read, ())
# Power On Servomotors
_thread.start_new_thread(ServoModule.forward, ())
# Check GPS and WiFi connection status
_thread.start_new_thread(checkStatus, ())
