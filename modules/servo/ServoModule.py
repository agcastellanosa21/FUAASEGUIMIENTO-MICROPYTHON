import machine


class ServoModule:
    frequency = 50

    # Left servo motor OUT Pins definitions
    servoLeftPinOut1 = machine.Pin(12, machine.Pin.OUT)
    servoLeftPinOut2 = machine.Pin(13, machine.Pin.OUT)
    # Left servo motor PWM definitions
    servoLeftPwm1 = machine.PWM(servoLeftPinOut1, freq=frequency)
    servoLeftPwm2 = machine.PWM(servoLeftPinOut2, freq=frequency)

    # Right servo motor OUT Pins definitions
    servoRightPinOut1 = machine.Pin(14, machine.Pin.OUT)
    servoRightPinOut2 = machine.Pin(15, machine.Pin.OUT)
    # Right servo motor PWM definitions
    servoRightPwm1 = machine.PWM(servoRightPinOut1, freq=frequency)
    servoRightPwm2 = machine.PWM(servoRightPinOut2, freq=frequency)

    # Constructor method of the class
    def __init__(self):
        # The builder turns off the servomotors
        self.stop()

    # This method takes care of stopping the servomotors
    def stop(self):
        # Left servomotor off
        self.servoLeftPinOut1.off()
        self.servoLeftPinOut2.off()
        # Right servomotor off
        self.servoRightPinOut1.off()
        self.servoRightPinOut2.off()

    # Method of moving the servomotor forward
    def forward(self):
        # Left and Right OUT 2 OFF
        self.servoLeftPinOut2.off()
        self.servoRightPinOut2.off()
        # Left and Right OUT 1 ON
        self.servoLeftPinOut1.on()
        self.servoRightPinOut1.on()

    # Method of moving the servo motors backwards
    def back(self):
        # Left and Right OUT 1 OFF
        self.servoLeftPinOut1.off()
        self.servoRightPinOut1.off()
        # Left and Right OUT 2 ON
        self.servoLeftPinOut2.on()
        self.servoRightPinOut2.on()
