import machine

frequency = 50
duty = 115

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


# This method takes care of stopping the servomotors
def stop():
    # Left servomotor off
    servoLeftPinOut1.off()
    servoLeftPinOut2.off()
    # Right servomotor off
    servoRightPinOut1.off()
    servoRightPinOut2.off()


# Method of moving the servomotor forward
def forward():
    stop()
    # Left and Right OUT 2 OFF
    servoLeftPinOut2.off()
    servoRightPinOut2.off()
    # Left and Right OUT 1 ON
    servoLeftPinOut1.on()
    servoRightPinOut1.on()
    # Duty Servomotor
    servoLeftPwm1.duty(duty)
    servoRightPwm1.duty(duty)


# Method of moving the servo motors backwards
def back():
    stop()
    # Left and Right OUT 1 OFF
    servoLeftPinOut1.off()
    servoRightPinOut1.off()
    # Left and Right OUT 2 ON
    servoLeftPinOut2.on()
    servoRightPinOut2.on()
    # Duty Servomotor
    servoLeftPwm2.duty(duty)
    servoRightPwm2.duty(duty)
