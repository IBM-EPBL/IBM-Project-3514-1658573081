import random
temperature = random.randint(100,150)
humidity = random.randint(100,150) 
while (temperature>102):
 print("HIGH TEMPERATURE DETECTED ! ALARM !")
 temperature-=2
