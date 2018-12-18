#!/usr/bin/python

import RPi.GPIO as GPIO  
from time import sleep

class my_lcd:

    global LCD_WIDTH, LCD_CHR, LCD_CMD, LCD_LINE_1, LCD_LINE_2
    global LCD_LINE_3, LCD_LINE_4, E_PULSE, E_DELAY
    
    LCD_WIDTH, LCD_CHR, LCD_CMD = 20, True, False
    LCD_LINE_1, LCD_LINE_2, LCD_LINE_3, LCD_LINE_4 = 0x80, 0xC0, 0x94, 0xD4
    E_PULSE, E_DELAY = 0.0005, 0.0005
    def __init__(self, pin_rs, pin_e, pins_db):
        
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_db = pins_db

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_e, GPIO.OUT)  
        GPIO.setup(self.pin_rs, GPIO.OUT)  
        for pin in self.pins_db:  
            GPIO.setup(pin, GPIO.OUT)  
        self.lcd_init()
        self.lcd_clear()

    
    def lcd_init(self):
        
        command=[0x33,0x32,0x06,0x0C,0x01]
        for i in range(len(command)):
            self.lcd_byte(command[i], LCD_CMD)
        #self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
        #self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
        #self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
        #self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
        #self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
        #self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display

        sleep(E_DELAY)

    def lcd_clear(self):

        self.lcd_byte(0x01, LCD_CMD)

    def lcd_byte(self,bits,mode):
        """ Send command to LCD """  
  
        sleep(0.001)  
        bits=bin(bits)[2:].zfill(8)          
        GPIO.output(self.pin_rs, mode)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i], True)  
  
        self.lcd_toggle_enable()
        
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4,8):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i-4], True)  

        self.lcd_toggle_enable()
  
        
    def lcd_toggle_enable(self):
        # Toggle enable
        sleep(E_DELAY)
        GPIO.output(self.pin_e, True)
        sleep(E_PULSE)
        GPIO.output(self.pin_e, False)
        sleep(E_DELAY)

    def lcd_string(self,message,line):
        # Send string to display
         
        message = message.ljust(LCD_WIDTH," ")
         
        self.lcd_byte(line, LCD_CMD)
         
        for i in range(LCD_WIDTH):
            self.lcd_byte(ord(message[i]),LCD_CHR)


lcd = my_lcd(4,5,[6,13,19,26])
lcd.lcd_string("hii there", LCD_LINE_1)
lcd.lcd_string("hii there", LCD_LINE_2)
lcd.lcd_string("hii there", LCD_LINE_3)
lcd.lcd_string("hii there", LCD_LINE_4)
sleep(2)
lcd.lcd_clear()