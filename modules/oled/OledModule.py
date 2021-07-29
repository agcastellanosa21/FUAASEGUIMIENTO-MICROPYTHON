from machine import Pin, SoftI2C
from SSD1306 import SSD1306_I2C
from framebuf import FrameBuffer


class OLEDModule:
    # Define OLED resolution size 128x64 pixels
    width = 128
    height = 64

    # ESP32 OLED Pin assignment
    i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
    display = SSD1306_I2C(width, height, i2c)

    # This method displays text on the OLED screen
    def displayText(self, text, column, row):
        self.display.text(text, column, row)
        self.display.show()

    # This method displays icons on the OLED screen
    # according to the row and column defined in the parameter step.
    def displayIcon(self, icon, column, row):
        buffer = bytearray(icon)
        frame = FrameBuffer(buffer, 50, 50)
        self.display.fill(0)
        self.display.framebuf.blit(frame, column, row)
        self.display.show()
