import tkinter as tk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

red=11
green=13
Yellow=15
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(Yellow,GPIO.OUT)

def RedLight():
    GPIO.output(green,GPIO.LOW)
    GPIO.output(Yellow,GPIO.LOW)
    GPIO.output(red,GPIO.HIGH)
    print("Turn on red LED")

def GreenLight():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(Yellow,GPIO.LOW)
    GPIO.output(green,GPIO.HIGH)
    print("Turn on green LED")
    
def BlueLight():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(Yellow,GPIO.HIGH) 
    print("Turn on blue LED")

def Quit():
        GPIO.output(red,GPIO.LOW)
        GPIO.output(green,GPIO.LOW)
        GPIO.output(Yellow,GPIO.LOW)
        GPIO.cleanup()
        window.destroy()

window = tk.Tk()
window.title('Task 5.2C')


button = tk.Button(window, text = 'Turn RED', command = RedLight, bg = 'red', height = 1, width = 30)
button.pack()
button = tk.Button(window, text = 'Turn GREEN',  command = GreenLight, bg = 'green', height = 1, width = 30)
button.pack()
button = tk.Button(window, text = 'Turn YELLOW', command = BlueLight, bg = 'blue', height = 1, width = 30)
button.pack()
exitbutton = tk.Button(window, text = 'QUIT', command = Quit, bg = 'grey', height = 1, width = 30)
exitbutton.pack()
window.mainloop()
