from machine import Pin
import network
import utime
from config import Config
import OledModule
import Icons

wifiLed = Pin(16, Pin.OUT)
wifi = network.WLAN(network.STA_IF)


# Method to activate WiFi module
def on():
    wifi.active(True)
    # Display wifi active icon on display


# Method to disable WiFi module
def off():
    wifi.active(False)
    # Hide wifi active icon on display


# Method to connect to a WiFi network with values
# defined in the config file
def connect():
    on()
    # Connect to wifi network
    wifi.connect(Config.value("wifiName"), Config.value("wifiPass"))
    # Check if connection was established
    while not isConnected():
        print("Connecting to wifi network...")
        # Wifi connecting LED indicator
        connectingIndicator()

    # Print ip address
    print("Assigned ip address: " + ipAddress())
    # Activate wifi connected led indicator
    while isConnected():
        # Wifi connected LED indicator
        connectedIndicator()


# Method verifies if connection
# to a Wi-Fi network is established
# @return bool
def isConnected():
    return wifi.isconnected()


# Find the assigned ip address
# @return str
def ipAddress():
    # Check if connection was established
    if isConnected():
        return str(wifi.ifconfig()[0])

    return ""


# Method to indicate that a connection
# with the Wi-Fi is being sought
def connectingIndicator():
    wifiLed.on()
    utime.sleep_ms(500)
    wifiLed.off()
    utime.sleep_ms(500)


# Method to indicate that a connection
# with the Wi-Fi has been established
def connectedIndicator():
    wifiLed.on()
    utime.sleep_ms(50)
    wifiLed.off()
    utime.sleep_ms(50)


# This method shows the status of the WIFI connection on the OLED screen
def displayStatus():
    if not isConnected():
        OledModule.displayIcon(Icons.Wifi(), 39, 0)
        OledModule.displayText("Connecting...", 15, 55)
    else:
        OledModule.displayIcon(Icons.Wifi(), 39, 0)
        OledModule.displayText("Ip " + ipAddress(), 0, 55)
