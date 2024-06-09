import time
from random import rd

time = 0
while True:
	rand_num = random.randint(1, 4)

p = input("Install System? yes/no >>>")
if p == "yes":
	for i in range(4):
		print("Install")
		time.sleep(time + rand_num)
		print("Install.")
		time.sleep(time + rand_num)
		print("Install..")
		time.sleep(time + rand_num)
		print("Install...")
	for g in range(5):
		print("Installing Package [#]")
		time.sleep(time + rand_num)
		print("Installing Package [########]")
		time.sleep(time + rand_num)
		print("Installing Package [######################]")
		time.sleep(time + rand_num)
		print("Installing Package [####################################]")
		time.sleep(time + rand_num)
		print("Installing Package [####################################]")
		time.sleep(time + rand_num)
		print("Package Install good")
		time.sleep(time + rand_num)
elif p == "no":
	break