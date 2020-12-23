import keyboard
import time 

def run():
	x = 0 
	while True:
		for i in range(60):
			print (str(i+1))
			time.sleep(1)
		x = x + 1 
		keyboard.write(str(x))

run()