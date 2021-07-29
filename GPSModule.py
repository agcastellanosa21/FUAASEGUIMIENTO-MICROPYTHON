from MicropyGPS import MicropyGPS
from machine import UART, Pin
import OledModule
import Icons
from config import Config
import utime
import urequests
import WifiModule

gpsLed = Pin(2, Pin.OUT)
uart = UART(1, baudrate=9600)
gps = MicropyGPS()


# Method to read data from the
# NEO-6M GPS module and perform data serialization
def read():
    while not hasSignal():
        # GPS connecting LED indicator
        connectingIndicator()

    while hasSignal():
        # Activate GPS connected led indicator
        connectedIndicator()
        # Read GPS data and update geo
        buffer = uart.readline()
        for line in buffer:
            gps.update(line)

        # We update the location through the api
        updateGeo()


# Method to obtain the longitude captured by the GPS
def longitude():
    return str(gps.longitude)


# Method to obtain the latitude captured by the GPS
def latitude():
    return str(gps.latitude)


# Method to identify if the GPS has a signal
def hasSignal():
    return uart.any()


# Method to indicate that a connection
# with the GPS is being sought
def connectingIndicator():
    gpsLed.on()
    utime.sleep_ms(500)
    gpsLed.off()
    utime.sleep_ms(500)


# Method to indicate that a connection
# with the GPS has been established
def connectedIndicator():
    gpsLed.on()
    utime.sleep_ms(50)
    gpsLed.off()
    utime.sleep_ms(50)


# Method to show the status on the OLED screen
# of the signal and data returned by the GPS module
def displayStatus():
    if not hasSignal():
        OledModule.displayIcon(Icons.Gps(), 40, 0)
        OledModule.displayText("Connecting...", 15, 55)
    else:
        OledModule.displayIcon(Icons.Gps(), 40, 0)
        OledModule.displayText("Lat " + latitude(), 0, 56)
        utime.sleep(5)
        OledModule.displayIcon(Icons.Gps(), 40, 0)
        OledModule.displayText("Lgt " + longitude(), 0, 56)


# Method to update the location in the database,
# by means of a rest api
# Method to update the location in the database,
# by means of a rest api
def updateGeo():
    url = Config.value("updateGeoUrl")
    url = str(url) + str("/" + longitude() + "/" + latitude() + "/" + Config.value("vehicle"))
    request = urequests.get(url)
    response = request.text
    print(response)
