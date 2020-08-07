import os
import time

dak = int(input("Minute :  "))
saniye = (dak * 60)
kapa = 5

os.system("shutdown -s -f -t {}".format(dak))
while saniye > 5:
	saniye -= 1
	print("Time remaining :",saniye)
	time.sleep(1)
while saniye <= 5:
	print("Last {} seconds to close".format(saniye))
	time.sleep(1)








