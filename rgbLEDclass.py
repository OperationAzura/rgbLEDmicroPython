from random import randint
from time import sleep
from machine import Pin, PWM

#RGBLed is a class to control rgb leds
class RGBLed:
    def __init__(self, rPinNum=23, gPinNum=21, bPinNum=19, duty=1023, freq=120):
        self.duty = duty #max duty cycle
        self.freq = freq #requency of pwm
        self.rPinNum = rPinNum
        self.gPinNum = gPinNum
        self.bPinNum = bPinNum
        #Pin objects
        self.rPin = Pin(rPinNum, Pin.OUT)
        self.gPin = Pin(gPinNum, Pin.OUT)
        self.bPin = Pin(bPinNum, Pin.OUT)
        #pwm objects
        self.rPWM = PWM(self.rPin)
        self.gPWM = PWM(self.gPin)
        self.bPWM = PWM(self.bPin)
        self.setFreq(self.freq)
        
    #setFreq sets the frequency for each pwm pin
    def setFreq(self, freq):
        self.freq = freq
        self.rPWM.freq(freq)
        self.gPWM.freq(freq)
        self.bPWM.freq(freq)
        
    #setDuty sets the max duty cycle
    def setDuty(self, duty):
        self.duty = duty
    
    def setRDuty(self, duty):
        self.rDuty = duty
        selfrPWM.duty(duty)
        
    def setRFreq(self, freq):
        self.rFreq = freq
        self.rPWM.freq(freq)
    
    def setGDuty(self, duty):
        self.gDuty = duty
        self.gPWM.duty(duty)
        
    def setGFreq(self, freq):
        self.gFreq = freq
        self.gPWM.freq(freq)
    
    def setBDuty(self, duty):
        self.bDuty = duty
        self.bPWM.duty(duty)
        
    def setBFreq(self, freq):
        self.bFreq = freq
        self.bPWM.freq(freq)
        
    #flame attemps to simulate a flame
    def flame(self):
        increment = True
        last = self.duty
        while True:
            if increment:
                last = last + randint(1,10)
            else:
                last = last - randint(1,10)
            if last > self.duty:
                increment = False
            elif last < self.duty / 2:
                increment = True
            r = randint(last - (last // 10), last)
            g = randint(r // 90, r // 11)
            b = randint(0,g-(g // 4))
            s = randint(20, 40 )
            flicker = randint(0, 100)
            if flicker < 5:
                self.flicker(flicker + 5)
            elif flicker == 13 or flicker == 17:
                self.flickerGreen(flicker)
            elif flicker == 23:
                self.flickerBlue(flicker//2)
            self.rPWM.duty(r)
            self.gPWM.duty(g)
            self.bPWM.duty(b)
            sleep((s / 100))
        
    def flicker(self, count):
        for c in range(count):
            r = randint(self.duty// 4, self.duty)
            g = randint(r // 90, r // 11)
            b = randint(0,g // 2)
            s = randint(5, 20 ) #flicker speed
            self.rPWM.duty(r)
            self.gPWM.duty(g)
            self.bPWM.duty(b)
            sleep((s / 100))
            
    def flickerGreen(self, count):
        for c in range(count):
            r = randint(self.duty// 4, self.duty)
            g = randint(r // 20, r // 4)
            b = randint(0,r // 2)
            s = randint(5, 20 ) #flicker speed
            self.rPWM.duty(g)
            self.gPWM.duty(r)
            self.bPWM.duty(b)
            sleep((s / 100))
            
    def flickerBlue(self, count):
        for c in range(count):
            r = randint(self.duty// 2, self.duty)
            g = randint(r // 50, r // 10)
            b = randint(0,g )
            s = randint(5, 20 ) #flicker speed
            self.rPWM.duty(g)
            self.gPWM.duty(b)
            self.bPWM.duty(r)
            sleep((s / 100))

if __name__ == "__main__":
    rgb = RGBLed()
    rgb.flame()