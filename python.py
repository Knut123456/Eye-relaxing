import time

from playsound import playsound


tid = 0
hour = 0
min = 0
sek = 0
tidsek = 0
tid1 = 0
tidsek1 = 0

hour = float(input("hvor mye timer " ))
min = float(input("hvor mye minutter "))
sek = float(input("hvor mye sekunder "))


hour1 = float(input("hvor mye timer etter den første timer "))
min1 = float(input("hvor mye minutter etter den første timer "))
sek1 = float(input("hvor mye sekunder etter den første timer "))

def tid():
    total_min = (hour * 60) + min + (sek / 60)    
    time.sleep(1)
    sek -= 1
    return total_min

def tidsek():
    total_sek = (hour * 60 * 60) + (min * 60) + sek 
    return total_sek

def tid1():
    total_minutes = (hour1 * 60) + min1 + (sek1 / 60)
    return total_minutes

def tidsek1():
    total_sek = (hour1 * 60 * 60) + (min1 * 60) + sek1 
    return total_sek


 



 
while True:
    print (tid() , "min") 
    time.sleep(tidsek())
    playsound('Alarm Clock.mp3')
    print ("tiden er nå ferdig")
    time.sleep(tidsek1())
    print (tid1() , "min etter første") 
    playsound('Alarm Clock.mp3')
    print ("ferdig med andre alarm")



