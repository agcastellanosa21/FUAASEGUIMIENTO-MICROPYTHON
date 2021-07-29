from modules.gps.MicropyGPS import MicropyGPS
from machine import UART
from modules.oled.OledModule import OLEDModule
from modules.oled import Icons
from modules.led.LedModule import LEDModule
import utime


class GPSModule:
    uart = UART(1, baudrate=9600)
    gps = MicropyGPS()

    # Method to read data from the
    # NEO-6M GPS module and perform data serialization
    def read(self):
        while True:
            if self.uart.any():
                LEDModule.gpsConnected()
                buffer = self.uart.readline()
                for line in buffer:
                    self.gps.update(line)

            else:
                LEDModule.gpsConnecting()

    # Method to obtain the longitude captured by the GPS
    def longitude(self):
        return str(self.gps.longitude)

    # Method to obtain the latitude captured by the GPS
    def latitude(self):
        return str(self.gps.latitude)

    # Method to identify if the GPS has a signal
    def hasSignal(self):
        return self.uart.any()

    # Method to show the status on the OLED screen
    # of the signal and data returned by the GPS module
    def displayStatus(self):
        if not self.hasSignal():
            OLEDModule.displayIcon(Icons.Gps(), Icons.WIDTH, Icons.HEIGHT)
            OLEDModule.displayText("Connecting...", 15, 55)
        else:
            OLEDModule.displayIcon(Icons.Gps(), Icons.WIDTH, Icons.HEIGHT)
            OLEDModule.displayText("Lat " + self.latitude(), 0, 56)
            utime.sleep(5)
            OLEDModule.displayIcon(Icons.Gps(), Icons.WIDTH, Icons.HEIGHT)
            OLEDModule.displayText("Lgt " + self.longitude(), 0, 56)
