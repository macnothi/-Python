from machine import Pin, Timer

led = Pin("LED",Pin.OUT) # will work on Pico W only
tim = Timer()

# timer callback
# The callback must take one argument, which is passed the Timer object. 
# The callback argument shall be specified. 
# Otherwise an exception will occur upon timer expiration
def tick(t):
    global led
    led.toggle()

# start timer at 2.5Hz, calling tick periodic
tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
