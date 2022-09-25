#pip install playsound
from random import randrange
from playsound import playsound

while(True):
	temp= random.randint(0,100)
	humidity = random.randint(0,100)
	if(temp > 40 and humidity >40):
		playsound('alarm.wav')