tid = 0
hour = 0
min = 0
sek = 0
import time

hour = int(input("hvor mye timer "))
min = int(input("hvor mye minutter "))
sek = int(input("hvor mye sekunder "))

def tid():
    min = sek / 60
    min = hour * 60
    return min

print (tid() , "min") 

