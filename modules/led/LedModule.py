from machine import Pin
import utime


class LEDModule:
    wifiLed = Pin(16, Pin.OUT)
    wifiGPS = Pin(25, Pin.OUT)

    # Method to control the speed of the LED
    # on and off when connected to a Wi-Fi network
    def wifiConnecting(self):
        while True:
            self.wifiLed.on()
            utime.sleep_ms(500)
            self.wifiLed.off()
            utime.sleep(500)

    # Method to control the speed of the LED
    # on and off when the ESP32 is connected to Wi-Fi internet
    def wifiConnected(self):
        while True:
            self.wifiLed.on()
            utime.sleep_ms(50)
            self.wifiLed.off()
            utime.sleep(50)

    # Method to control the speed of the LED
    # on and off when the ESP32 is connected to the GPS of the Neo-6M module
    def gpsConnecting(self):
        while True:
            self.wifiLed.on()
            utime.sleep_ms(500)
            self.wifiLed.off()
            utime.sleep(500)

    # Method to control the speed of the LED
    # on and off when the ESP32 has a GPS signal from the Neo-6M module
    def gpsConnected(self):
        while True:
            self.wifiLed.on()
            utime.sleep_ms(50)
            self.wifiLed.off()
            utime.sleep(50)