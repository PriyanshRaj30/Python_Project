import time
from plyer import notification
if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Please Drink Water Now!!",
 			message ="Hey there, my aqua-craving friend! Time to quench that thirst and give your body the hydration it deserves.So grab a glass. ",
 			#app_icon = r'L:\Codsonal\Python\Project\Water Remainder\glass.ico',
 			timeout= 15
 			)
 		#time.sleep(0.5*60*60)
 		time.sleep(600)	
