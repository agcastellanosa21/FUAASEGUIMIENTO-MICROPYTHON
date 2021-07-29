import network
import utime
from config import Config
from modules.oled.OledModule import OLEDModule
from modules.oled import Icons
from modules.led.LedModule import LEDModule


class WifiModule:
    wifi = network.WLAN(network.STA_IF)

    # Method to activate WiFi module
    def on(self):
        self.wifi.active(True)
        # Display wifi active icon on display

    # Method to disable WiFi module
    def off(self):
        self.wifi.active(False)
        # Hide wifi active icon on display

    # Method to connect to a WiFi network with values
    # defined in the config file
    def connect(self):
        self.on()
        # Activate wifi connecting led indicator
        LEDModule.wifiConnecting()
        # Connect to wifi network
        self.wifi.connect(Config.value("wifiName"), Config.value("wifiPass"))
        # Check if connection was established
        while not self.isConnected():
            print("Connecting to wifi network...")
            utime.sleep(1)

        # Print ip address
        print("Assigned ip address: " + self.ipAddress())
        # Activate wifi connected led indicator
        LEDModule.wifiConnected()

    # Method verifies if connection
    # to a Wi-Fi network is established
    # @return bool
    def isConnected(self):
        return self.wifi.isconnected()

    # Find the assigned ip address
    # @return str
    def ipAddress(self):
        # Check if connection was established
        if self.isConnected():
            return str(self.wifi.ifconfig()[0])

        return ""

    # This method shows the status of the WIFI connection on the OLED screen
    def displayStatus(self):
        if not self.isConnected():
            OLEDModule.displayIcon(Icons.Wifi(), Icons.WIDTH, Icons.HEIGHT)
            OLEDModule.displayText("Connecting...", 15, 55)
        else:
            OLEDModule.displayIcon(Icons.Wifi(), Icons.WIDTH, Icons.HEIGHT)
            OLEDModule.displayText("Ip " + self.ipAddress(), 0, 55)
